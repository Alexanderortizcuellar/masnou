from PyQt5 import QtCore, QtGui, QtWidgets
from updatedlg_ui import Ui_Form
from functools import partial
import gc


class UpdateDialog(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent, table_data, update_func):
        super().__init__(parent)
        self.setupUi(self)
        self.table_data = table_data
        self.update_func = update_func
        self.frame_layout = QtWidgets.QGridLayout()
        self.checks_layout = QtWidgets.QHBoxLayout()
        self.spots_container.setLayout(self.frame_layout)
        self.checks_container.setLayout(self.checks_layout)
        self.create_tables()
        self.accept_btn.clicked.connect(self.accept)

    def create_tables(self):
        for i in range(self.frame_layout.count()):
            self.frame_layout.itemAt(i).widget().deleteLater()  # type: ignore
        for i, row in enumerate(self.table_data):
            col_num = i % 5
            row_num = i // 5
            print(row_num, col_num)
            button = QtWidgets.QPushButton(f"{row[0]}\n\n{row[2]}\n Vs. \n{row[4]}")
            button.setToolTip(str(row[2] + " Vs. " + row[4]))
            button.setSizePolicy(
                QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
            )
            button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))  # type: ignore
            button.setStyleSheet(
                """QPushButton {background-color: #f6f6f6;border: 1px solid black;
                                border-radius: 5px;font-size: 20px;padding: 10px;}
                QPushButton:hover {background-color: #e6e6e6;}
                QPushButton:pressed {background-color: #90C7A9;}
                QPushButton:focus {border: 1px solid blue;}
                """
            )
            button.clicked.connect(partial(self.handle_click, row))
            self.frame_layout.addWidget(button, row_num, col_num)

    def handle_click(self, data):
        for i in range(self.checks_layout.count()):
            self.checks_layout.itemAt(i).widget().deleteLater() # type: ignore
        player1_box = QtWidgets.QCheckBox(data[2])
        player1_box.setObjectName("player-0")
        player1_box.setAutoExclusive(True)
        player2_box = QtWidgets.QCheckBox(data[4])
        player2_box.setObjectName("player-1")
        player2_box.setAutoExclusive(True)
        draw = QtWidgets.QCheckBox("Tablas")
        draw.setObjectName("draw-2")
        player1_box.setFont(QtGui.QFont("Arial", 17))
        player2_box.setFont(QtGui.QFont("Arial", 17))
        draw.setFont(QtGui.QFont("Arial", 17))
        player1_box.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        player2_box.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        draw.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        draw.setAutoExclusive(True)
        self.checks_layout.addWidget(player1_box)
        self.checks_layout.addWidget(draw)
        self.checks_layout.addWidget(player2_box)
        self.checks_container.setTitle(f"Seleccione el ganador de la mesa: {data[0]}")

    def accept(self):
        for i in range(self.checks_layout.count()):
            item = self.checks_layout.itemAt(i)
            if item is not None:
                w = item.widget()
                if w is not None:
                    if w.isChecked():
                        self.update_func(
                            {
                                "spot": int(
                                    self.checks_container.title().split(":")[1].strip()
                                ),
                                "winner": int(w.objectName().split("-")[1].strip())
                            }
                        )
                        self.close()
                        self.destroy()
                        del self
                        gc.collect()
                    else:
                        continue
                    return
                QtWidgets.QMessageBox.about(self, "Masnou", "Debe escoger un jugador")
                return
            QtWidgets.QMessageBox.about(self, "Masnou", "Debe escoger un jugador")
            return
        QtWidgets.QMessageBox.about(self, "Masnou", "Debe escoger un jugador")
        return
