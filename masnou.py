from PyQt5 import QtWidgets, QtCore, QtGui
import sys

# from openpyxl import Workbook, load_workbook
from masnou_ui import Ui_MainWindow
import images_rc # pyright: ignore
from models import FilaModel, PlayersModel, RoundsModel, RoundsModelHistory, TableModel
from tournament_dlg import TournamentDialog
from puzzles import to_svg
from masnou_logic import Masnou
import enum
from update_dlg import UpdateDialog


class Pages(enum.Enum):
    Menu = 0
    Tournament = 1
    Fila = 2
    Players = 3
    Ronda = 4
    Details = 5
    Stats = 6


# pyright: reportIncompatibleMethodOverride=none
# pyright: reportAttributeAccessIssue=none


class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tournament_active = False
        self.toolBar.setFixedHeight(40)
        self.new_tournament_btn = QtWidgets.QToolButton()
        self.new_tournament_btn.setIcon(
            QtGui.QIcon(":/images/images/new-tournament.png")
        )
        self.new_tournament_btn.setToolTip("Nuevo torneo")
        self.new_tournament_btn.setFixedSize(QtCore.QSize(60, 50))
        self.new_tournament_btn.setIconSize(QtCore.QSize(50, 50))
        self.players_toolbutton = QtWidgets.QToolButton()
        self.players_toolbutton.setIcon(QtGui.QIcon(":/images/images/players.png"))
        self.players_toolbutton.setToolTip("Ver o editar jugadores")
        self.players_toolbutton.setFixedSize(QtCore.QSize(60, 50))
        self.players_toolbutton.setIconSize(QtCore.QSize(50, 50))
        self.update_toolbutton = QtWidgets.QToolButton()
        self.update_toolbutton.setIcon(QtGui.QIcon(":/images/images/update.png"))
        self.update_toolbutton.setToolTip("Actualizar torneo")
        self.update_toolbutton.setFixedSize(QtCore.QSize(60, 50))
        self.update_toolbutton.setIconSize(QtCore.QSize(50, 50))
        self.delete_toolbutton = QtWidgets.QToolButton()
        self.delete_toolbutton.setIcon(QtGui.QIcon(":/images/images/delete.png"))
        self.delete_toolbutton.setToolTip("Eliminar Torneo")
        self.delete_toolbutton.setFixedSize(QtCore.QSize(60, 50))
        self.delete_toolbutton.setIconSize(QtCore.QSize(50, 50))
        self.navigate_toolbutton = QtWidgets.QToolButton()
        self.navigate_toolbutton.setIcon(QtGui.QIcon(":/images/images/delete.png"))
        self.navigate_toolbutton.setToolTip("Navigator")
        self.navigate_toolbutton.setFixedSize(QtCore.QSize(60, 50))
        self.navigate_toolbutton.setIconSize(QtCore.QSize(50, 50))
        self.toolBar.addWidget(self.new_tournament_btn)
        self.toolBar.addWidget(self.players_toolbutton)
        self.toolBar.addWidget(self.update_toolbutton)
        self.toolBar.addWidget(self.delete_toolbutton)
        self.toolBar.addWidget(self.navigate_toolbutton)
        self.toolBar.setFixedHeight(50)
        self.navigator.setCurrentIndex(Pages.Menu.value)
        self.new_tournament_btn.clicked.connect(self.new_tournament)
        self.edit_players_button.clicked.connect(
            lambda: self.navigator.setCurrentIndex(Pages.Players.value)
        )
        self.ver_fila_button.clicked.connect(lambda: self.navigator.setCurrentIndex(2))
        self.ver_rondas_button.clicked.connect(
            lambda: self.navigator.setCurrentIndex(Pages.Ronda.value)
        )
        self.finish_button.clicked.connect(self.finish_tournament)
        self.finish_button.setEnabled(False)
        # toolbox screen bindings
        self.players_toolbutton.clicked.connect(
            lambda: self.navigator.setCurrentIndex(Pages.Players.value)
        )
        self.update_toolbutton.clicked.connect(
            self.update_tournament
        )
        # menu screen bindings
        self.menu_btn_create.clicked.connect(self.new_tournament)
        self.menu_btn_quit.clicked.connect(self.close)
        # players screen bindings
        self.players_save_changes.clicked.connect(
            lambda: self.navigator.setCurrentIndex(Pages.Tournament.value)
        )
        # fila screen bindings
        self.save_changes_fila.clicked.connect(
            lambda: self.navigator.setCurrentIndex(Pages.Tournament.value)
        )
        # actions screen bindings
        self.action_Editar_Jugadores.triggered.connect(
            lambda: self.navigator.setCurrentIndex(Pages.Players.value)
        )
        self.action_Torneo_Actual.triggered.connect(
            lambda: self.navigator.setCurrentIndex(Pages.Tournament.value)
        )
        self.action_Men.triggered.connect(
            lambda: self.navigator.setCurrentIndex(Pages.Menu.value)
        )
        self.players_model = PlayersModel(
            self,
            [
                ["Name", "Surname", "Age", "City", "Rating"],
                ["John", "Doe", 25, "New York", 7.5],
                ["Jane", "Doe", 30, "Chicago", 6.0],
                ["John", "Doe", 35, "Los Angeles", 8.0],
            ],
        )
        # ronda screen bindings
        self.rondas_save_changes.clicked.connect(
            lambda: self.navigator.setCurrentIndex(Pages.Tournament.value)
        )
        # models
        self.fila_model_main = FilaModel([])
        self.fila_model = FilaModel([])
        self.score_model = TableModel(self, [])
        self.rounds_model = RoundsModel(self, [])
        self.score_table.setModel(self.score_model)
        self.players_table.setModel(self.players_model)
        self.players_table.verticalHeader().setVisible(False)
        self.players_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.players_table.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.players_table.setSortingEnabled(True)
        self.players_table.resizeColumnsToContents()
        self.players_table.customContextMenuRequested.connect(
            self.players_table_customContextMenuRequested
        )   

        self.fila_list_main.setModel(self.fila_model)
        self.fila_list.setModel(self.fila_model)
        self.fila_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.fila_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        # rondas MAIN table settings
        self.rondas_main_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.rondas_main_table.setColumnHidden(1, True)
        self.rondas_main_table.setColumnHidden(4, True)
        self.rondas_main_table.resizeColumnToContents(0)
        self.rondas_main_table.horizontalHeader().setStretchLastSection(True)
        self.rondas_main_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        # rondas table settings
        self.rondas_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.rondas_table.resizeColumnToContents(0)
        self.rondas_table.verticalHeader().setVisible(False)
        # rondas history table settings
        self.rondas_history_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.rondas_history_table.resizeColumnToContents(0)
        self.rondas_history_table.verticalHeader().setVisible(False)
        self.rondas_history_table.setColumnHidden(1, True)
        self.rondas_history_table.setColumnHidden(5, True)
        # score table settings
        self.score_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.score_table.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.score_table.verticalHeader().setVisible(False)
        self.score_table.resizeColumnToContents(0)
        self.score_table.customContextMenuRequested.connect(
            self.score_table_customContextMenuRequested
        )
        self.score_table.horizontalHeader().setStretchLastSection(True)
        self.score_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        # chess board svg
        self.labelImage = QtWidgets.QLabel()
        self.labelImage.setAlignment(QtCore.Qt.AlignCenter)
        board_data = to_svg()
        board_image = QtGui.QImage.fromData(board_data["svg"])
        self.labelImage.setPixmap(QtGui.QPixmap(board_image))
        self.board_container.layout().addWidget(self.labelImage)
        self.board_container.setContentsMargins(0, 0, 0, 0)
        self.puzzle_title.setText(f"Problema del Día {board_data["turn"]} mueven.")
        self.masnou_manager = Masnou()
        # update button defined after the masnou manager is instantiated
        self.update_button.clicked.connect(self.update_tournament)
    
    def setup_tournament(self):
        # self.masnou_manager.create_tournament(self.model.players_data)
        self.rounds_model = RoundsModel(self, self.masnou_manager.groups_to_table())
        self.rondas_main_table.setModel(self.rounds_model)
        self.rondas_main_table.verticalHeader().setVisible(False)
        self.fila_model = FilaModel(self.masnou_manager.get_cola_names())
        self.fila_model_main = FilaModel(self.masnou_manager.get_cola_names())
        self.fila_list_main.setModel(self.fila_model_main)
        print(self.masnou_manager.get_cola_names())
        self.fila_list.setModel(None)
        self.fila_list.setModel(self.fila_model)
        self.players_model = PlayersModel(
            self,
            [
                ["Name", "Surname", "Age", "City", "Rating"],
                ["John", "Doe", 25, "New York", 7.5],
                ["Jane", "Doe", 30, "Chicago", 6.0],
                ["John", "Doe", 35, "Los Angeles", 8.0],
            ],
        )
        self.rounds_model_main = RoundsModel(self, self.masnou_manager.groups_to_table())
        self.rondas_table.setModel(self.rounds_model_main)
        # setup setting needed after resetting the models
        self.rondas_main_table.setColumnHidden(1, True)
        self.rondas_main_table.setColumnHidden(4, True)

    def update_tournament(self):
        self.update_dialog = UpdateDialog(None, self.masnou_manager.groups_to_table(), self.handle_update)
        self.update_dialog.show()
    
    def handle_update(self, data):
        self.masnou_manager.update(spot=data.get("spot", 0), winner=data.get("winner", 0))
        self.rounds_model = RoundsModel(self, self.masnou_manager.groups_to_table())
        self.rondas_main_table.setModel(self.rounds_model)
        self.rondas_main_table.resizeColumnsToContents()
        self.rondas_table.resizeColumnsToContents()
        self.fila_model = FilaModel(self.masnou_manager.get_cola_names())
        print(self.masnou_manager.get_cola_names())
        self.fila_list.setModel(None)
        self.fila_list.setModel(self.fila_model)
        self.score_model = TableModel(self, self.masnou_manager.temp_table())
        self.score_table.setModel(self.score_model)
        self.rounds_history_model = RoundsModelHistory(self, self.masnou_manager.rounds_history)
        self.rondas_history_table.setModel(self.rounds_history_model)
        self.rondas_history_table.setColumnHidden(1, True)
        self.rondas_history_table.setColumnHidden(6, True)
        self.rondas_history_table.resizeColumnToContents(0)
        # self.rondas_history_table.resizeColumnToContents(2)
        self.rondas_history_table.horizontalHeader().setStretchLastSection(True)
        self.rondas_history_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.rondas_history_table.resizeColumnToContents(3)
        self.rondas_history_table.resizeColumnToContents(4)
        self.rondas_history_table.resizeColumnToContents(5)
        self.fila_model_main = FilaModel(self.masnou_manager.get_cola_names())
        self.fila_list_main.setModel(self.fila_model_main)
        self.rounds_model_main = RoundsModel(self, self.masnou_manager.groups_to_table())
        self.rondas_table.setModel(self.rounds_model_main)

    def new_tournament(self):
        if self.tournament_active:
            msg = QtWidgets.QMessageBox.question(
                self,
                "Masnou",
                "Hay un torneo activo. Estas seguro de cerrar el torneo?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            )
            if msg == QtWidgets.QMessageBox.Yes:
                self.dialog = TournamentDialog(self)
                self.dialog.show()
            else:
                return
        else:
            self.dialog = TournamentDialog(self)
            self.dialog.show()

    def remove_player(self):
        index = self.players_table.currentIndex()
        if index == -1:
            return
        self.model.removeRows(index.row(), 1)

    def add_player(
        self,
    ):
        index = self.players_table.currentIndex()
        if index == -1:
            return
        self.model.insertRows(len(self.model.players_data), 1)

    def players_table_customContextMenuRequested(self, event: QtCore.QEvent) -> None:
        menu = QtWidgets.QMenu(self)
        remove_action = menu.addAction("Remove")
        add_action = menu.addAction("Add")
        action = menu.exec_(QtGui.QCursor.pos())
        if action == remove_action:
            self.remove_player()
        elif action == add_action:
            self.add_player()

    def score_table_customContextMenuRequested(self, event: QtCore.QEvent):
        menu = QtWidgets.QMenu(self)
        hide_list = menu.addAction("Esconder Fila")
        add_action = menu.addAction("Actualizar")
        # go_details = menu.addAction("Ver Detalles")
        action = menu.exec_(QtGui.QCursor.pos())
        if action == hide_list:
            pass
        elif action == add_action:
            pass

    def finish_tournament(self):
        self.tournament_active = False

    def cancel_tournament(self):
        self.tournament_active = False
        self.players_table.setModel(None)
        self.fila_list.setModel(None)
        self.score_table.setModel(None)
        self.finish_button.setEnabled(False)
        self.masnou_manager

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        if self.tournament_active:
            msg = QtWidgets.QMessageBox.question(
                self,
                "Masnou",
                "Hay un torneo activo. Estas seguro de cerrar el torneo?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            )
        else:
            msg = QtWidgets.QMessageBox.question(
                self,
                "Masnou",
                "Estas seguro de cerrar la aplicacion?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            )
        if msg == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


style = """ 
QTableView:QLineEdit {
    color:red
}
QHeaderView::section {
    background-color: #4CAF50;  /* Green background */
    color: white;               /* White text */
    padding: 5px;
    border: 1px solid #dddddd;
    font-weight: bold;
    font-size: 16px;
    text-align: center;

}

QTableCornerButton::section {
    background-color: #4CAF50;  /* Green background for top-left corner */
    border: 1px solid #dddddd;
}
"""
app = QtWidgets.QApplication(sys.argv)
#style = load_stylesheet()
app.setStyleSheet(style)
window = Window()
window.show()
app.exec_()
