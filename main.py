from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt


class PlayerModel(QtCore.QAbstractListModel):
    def __init__(self, parent, players: list = []):
        super(PlayerModel, self).__init__(parent)
        self.parent = parent
        self.players = players

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.players[index.row()]
        if role == Qt.EditRole:
            return self.players[index.row()]
        if role == Qt.TextAlignmentRole:
            if self.parent.objectName() == "white":
                return Qt.AlignRight
            return Qt.AlignLeft

    def rowCount(self, index):
        return len(self.players)

    def flags(self, index):
        if index.isValid():
            return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable
        return Qt.NoItemFlags

    def setData(self, index, value, role):
        if index.isValid() and role == Qt.EditRole:
            self.players[index.row()] = value
            self.dataChanged.emit(index, index)
            return True
        return False

    def mimeData(self, indexes):
        data = QtCore.QMimeData()
        if indexes:
            data.setText(
                "\n".join([self.data(index, Qt.DisplayRole) for index in indexes])
            )
        return data

    def insertRows(self, position: int, rows: int, parent=QtCore.QModelIndex()):
        self.beginInsertRows(parent, position, position + rows - 1)
        self.players.insert(position, "")
        self.endInsertRows()
        self.layoutChanged.emit()
        return True

    def removeRows(self, position: int, rows: int, parent=QtCore.QModelIndex()):
        self.beginRemoveRows(parent, position, position + rows - 1)
        self.players.pop(position)
        self.endRemoveRows()
        self.layoutChanged.emit()
        return True


class PlayersList(QtWidgets.QListView):
    def __init__(self, parent=None):
        super(PlayersList, self).__init__(parent)
        self.setStyleSheet("border: 4px solid gray;border-radius:6px;background-color:steelblue;padding: 10px;")
        self.parent = parent
        self.setObjectName("players")
        self.setFont(QtGui.QFont("Roboto", 15))
        self.setAcceptDrops(True)
        players = [
            "orlando marulanda",
            "pedro perez",
            "julian hernandez",
            "gonzalo gonzalez",
            "jose hernandez",
            "arsin perez",
            "luis perez casas",
            "Darwin Marulanda",
        ]
        self.model: QtCore.QAbstractListModel = PlayerModel(self, players)
        self.setModel(self.model)
        self.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.setEditTriggers(
            QtWidgets.QListView.DoubleClicked | QtWidgets.QListView.SelectedClicked
        )

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        drag = QtGui.QDrag(self)
        mime = QtCore.QMimeData()
        current_index = self.indexAt(event.pos())
        if current_index.isValid():
            current_item_string = self.model.data(current_index, Qt.EditRole)
            mime.setText(current_item_string + str(current_index.row()))
            drag.setMimeData(mime)
            drag.exec(Qt.MoveAction)

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)

    def dragMoveEvent(self, event):
        event.accept()

    def dropEvent(self, event: QtGui.QDropEvent):
        event.setDropAction(QtCore.Qt.LinkAction)
        if event.source() == self:
            event.ignore()
            return
        if event.mimeData().hasText():
            source_widget = event.source()
            text = event.mimeData().text()
            source_index = int(text[-1])
            text = text.replace(str(source_index), "")
            self.model.insertRows(self.model.rowCount(0), 1)
            self.model.setData(
                self.model.index(self.model.rowCount(0) - 1), text, Qt.EditRole
            )
            source_widget.model.removeRows(source_index, 1)
            source_widget.layoutChanged.emit(source_widget.model.rowCount(0))

        super().dropEvent(event)

    def dragEnterEvent(self, event: QtGui.QDragEnterEvent):
        super().dragEnterEvent(event)
        event.accept()

    def enterEvent(self, event):
        super().enterEvent(event)
        self.setCursor(QtCore.Qt.OpenHandCursor)


class ColorList(QtWidgets.QListView):
    layoutChanged = QtCore.pyqtSignal(int)
    def __init__(self, parent=None, color="white"):
        super(ColorList, self).__init__(parent)
        self.setStyleSheet("border: 4px solid gray;border-radius:6px;background-color:steelblue")
        self.setFont(QtGui.QFont("Roboto", 14))
        self.setObjectName(color)
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.model: QtCore.QAbstractListModel = PlayerModel(self, [])
        self.setModel(self.model)
        self.setEditTriggers(
            QtWidgets.QListView.DoubleClicked | QtWidgets.QListView.SelectedClicked
        )

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        index = self.indexAt(event.pos())
        if index.isValid():
            drag = QtGui.QDrag(self)
            mime = QtCore.QMimeData()
            current_item_string = self.model.data(index, Qt.EditRole)
            mime.setText(current_item_string + str(index.row()))
            drag.setMimeData(mime)
            drag.exec(Qt.MoveAction)


    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)

    def dragMoveEvent(self, event):
        event.accept()

    def dropEvent(self, event: QtGui.QDropEvent):
        event.setDropAction(QtCore.Qt.LinkAction)
        if event.mimeData().hasText():
            text = event.mimeData().text()
            target_index = self.indexAt(event.pos())
            source_widget = event.source()
            source_index = int(text[-1])
            text = text.replace(str(source_index), "")
            if source_widget.objectName() == "players":
                if target_index.isValid():
                    # returning item
                    target_item = self.model.data(target_index, Qt.EditRole)
                    source_widget.model.setData(
                        source_widget.model.index(source_index),
                        target_item,
                        Qt.EditRole,
                    )
                    # setting item
                    self.insert(target_index, text)
                else:
                    self.add_end(target_index, text)
                    print("about to remove row: ", source_index)
                    source_widget.model.removeRows(source_index, 1)

            else:
                if self.objectName() == source_widget.objectName():
                    if target_index.isValid():
                        target_text = self.model.data(target_index, Qt.EditRole)
                        self.insert(target_index, text)
                        self.insert(self.model.index(source_index), target_text)
                    else:
                        event.ignore()
                else:
                    if target_index.isValid():
                        target_text = self.model.data(target_index, Qt.EditRole)
                        self.insert(target_index, text)
                        source_widget.model.removeRows(source_index, 1)
                        # send back to players # to do
                    else:
                        # Todo when invalid index

                        pass
                source_widget.layoutChanged.emit(source_widget.model.rowCount(0))
        self.layoutChanged.emit(self.model.rowCount(0))
        self.resize_to_fit()
        super().dropEvent(event)

    def dragEnterEvent(self, event: QtGui.QDragEnterEvent):
        super().dragEnterEvent(event)
        event.accept()

    def add_end(self, index, text):
        print("[*] inserting at end", text)
        self.model.insertRows(len(self.model.players), 1)
        self.model.setData(
            self.model.index(len(self.model.players) - 1), text, Qt.EditRole
        )

    def insert(self, index, text):
        print("[*] inserting", text)
        self.model.setData(index, text, Qt.EditRole)
    
    def resize_to_fit(self):
        max_width = 0
        for i in range(self.model.rowCount(0)):
            max_width = max(max_width, len(self.model.data(self.model.index(i), Qt.DisplayRole)))
        self.setMinimumWidth(max_width * 10)


class TableContextMenu(QtWidgets.QMenu):
    def __init__(self, parent):
        super().__init__(parent)
        self.add_action = QtWidgets.QAction(self)


class Pairer(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Pairer, self).__init__(parent)
        QtGui.QFontDatabase.addApplicationFont("fonts/Roboto-Medium.ttf")
        self.setAcceptDrops(True)
        self.setMouseTracking(True)
        self.setWindowTitle("Pairer")
        self.resize(500, 500)
        self.boxlayout = QtWidgets.QHBoxLayout()
        self.boxlayout.setSpacing(0)
        self.boxlayout.setStretch(0, 0)
        self.boxlayout.setStretch(1, 1)
        self.setLayout(self.boxlayout)
        self.players = PlayersList(self)
        self.right_frame = QtWidgets.QFrame()
        self.right_layout = QtWidgets.QVBoxLayout()
        self.right_layout.setSpacing(0)
        self.right_frame.setLayout(self.right_layout)
        self.boxlayout.addWidget(self.players)
        self.boxlayout.addWidget(self.right_frame)

        self.colors_layout = QtWidgets.QHBoxLayout()
        self.colors_frame = QtWidgets.QFrame()
        self.colors_frame.setLayout(self.colors_layout)

        self.right_layout.addWidget(self.colors_frame)
        self.right_bottom = QtWidgets.QFrame()
        self.right_bottom_layout = QtWidgets.QVBoxLayout()
        self.right_bottom.setLayout(self.right_bottom_layout)
        self.right_layout.addWidget(self.right_bottom)
        self.white_frame = QtWidgets.QFrame()
        self.white_layout = QtWidgets.QVBoxLayout()
        self.white_frame.setLayout(self.white_layout)
        self.colors_layout.addWidget(self.white_frame)
        self.black_frame = QtWidgets.QFrame()
        self.black_layout = QtWidgets.QVBoxLayout()
        self.black_frame.setLayout(self.black_layout)
        self.colors_layout.addWidget(self.black_frame)
        self.white_label = QtWidgets.QLabel("White")
        self.black_label = QtWidgets.QLabel("Black")
        self.white_layout.addWidget(self.white_label)
        self.black_layout.addWidget(self.black_label)
        self.white_layout.setContentsMargins(0, 0, 0, 0)
        self.black_layout.setContentsMargins(0, 0, 0, 0)
        self.white = ColorList(self, "white")
        self.black = ColorList(self, "black")
        self.white.layoutChanged.connect(lambda x: self.white_label.setText(f"white players ({x})"))
        self.black.layoutChanged.connect(lambda x: self.black_label.setText(f"black players ({x})"))
        self.white.setAlternatingRowColors(True)
        self.black.setAlternatingRowColors(True)
        self.white_layout.addWidget(self.white)
        self.black_layout.addWidget(self.black)
        self.button_clear = QtWidgets.QPushButton("Clear")
        self.right_bottom_layout.addWidget(self.button_clear)


class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.pairer = Pairer()
        self.setCentralWidget(self.pairer)


app = QtWidgets.QApplication([])
window = Window()
window.show()
app.exec_()
