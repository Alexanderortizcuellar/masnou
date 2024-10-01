from table_ui import Ui_Dialog
from PyQt5 import QtCore, QtWidgets


class CreateTableDlg(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.populate_players()
        self.ok_btn = self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok)
        self.ok_btn.setEnabled(False)
        self.buttonBox.accepted.connect(self.save_changes)
        self.buttonBox.rejected.connect(self.reject)
        self.player1.currentTextChanged.connect(self.toggle_accept)
        self.player2.currentTextChanged.connect(self.toggle_accept)

    def populate_players(self):
        players = self.parent.masnou_manager.get_cola_names()
        self.player1.addItems(players)
        self.player2.addItems(players)

    def toggle_accept(self):
        if self.player1.currentText() == self.player2.currentText():
            self.ok_btn.setEnabled(False)
        else:
           self.ok_btn.setEnabled(True) 
    def validate(self):
        if self.player1.currentText() == self.player2.currentText():
            return False
        return True

    def save_changes(self):
        if self.validate():
            self.parent.add_group([self.player1.currentIndex(), self.player2.currentIndex()])
            self.close()
            return True
        QtWidgets.QMessageBox.warning(self, "Masnou", "Jugador 1 y 2 no pueden ser iguales")
        return False

