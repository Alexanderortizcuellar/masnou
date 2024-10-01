from PyQt5 import QtCore, QtGui
import typing
from copy import deepcopy


# pyright: reportIncompatibleMethodOverride=none
# pyright: reportAttributeAccessIssue=none


class FilaModel(QtCore.QAbstractListModel):
    def __init__(self, fila_data):
        super().__init__()
        self.fila_data = fila_data

    def rowCount(self, parent: QtCore.QModelIndex) -> int:
        return len(self.fila_data)

    def data(self, index: QtCore.QModelIndex, role: int):
        if role == QtCore.Qt.DisplayRole:
            return self.fila_data[index.row()]

    def setData(self, index: QtCore.QModelIndex, value: typing.Any, role: int) -> bool:
        if role == QtCore.Qt.EditRole:
            row = index.row()
            self.fila_data[row] = value
        return False


class PairingModel(QtCore.QAbstractTableModel):
    def __init__(self, parent, rounds_data: list) -> None:
        super().__init__(parent)
        self.pairing_data = rounds_data
        self.headers = ["Primera fila", "Segunda fila"]

    def rowCount(self, index):
        return len(self.pairing_data)

    def columnCount(self, index):
        return len(self.headers)

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
            return self.pairing_data[index.row()][index.column()]

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self.headers[section]

    def flags(self, index) -> QtCore.Qt.ItemFlags:
        return (
            QtCore.Qt.ItemIsSelectable
            | QtCore.Qt.ItemIsEnabled
            | QtCore.Qt.ItemIsEditable
        )

    def setData(self, index, value, role):
        if role == QtCore.Qt.EditRole:
            row = index.row()
            column = index.column()
            self.pairing_data[row][column] = value
        return False

    def removeRows(self, position, rows, parent=QtCore.QModelIndex()):
        self.beginRemoveRows(parent, position, position + rows - 1)
        self.pairing_data.pop(position)
        self.endRemoveRows()
        self.layoutChanged.emit()
        return True

    def insertRows(self, position, rows, parent=QtCore.QModelIndex()):
        self.beginInsertRows(parent, position, position + rows - 1)
        length = len(self.headers)
        self.pairing_data.insert(position, [0 for _ in range(length)])
        self.endInsertRows()
        self.layoutChanged.emit()
        return True


class RoundsModel(QtCore.QAbstractTableModel):
    def __init__(self, parent, rounds_data: list) -> None:
        super().__init__(parent)
        self.rounds_data = rounds_data
        self.add_blank_column()
        self.headers = ["Spot", "Id", "Name", "Vs.", "Id", "Name"]

    def dicts_to_list(self, dicts):
        return [[d[key] for key in self.headers] for d in dicts]

    def add_blank_column(self):
        for round in self.rounds_data:
            round.insert(3, "")

    def rowCount(self, index):
        return len(self.rounds_data)

    def columnCount(self, index):
        return len(self.headers)

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
            return self.rounds_data[index.row()][index.column()]
        if role == QtCore.Qt.BackgroundRole:
            if index.column() == 3:
                return QtGui.QBrush(QtGui.QColor(205, 205, 205))
        if role == QtCore.Qt.FontRole:
            if index.column() == 3:
                return QtGui.QFont("Arial", 10, QtGui.QFont.Bold)

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self.headers[section]


class RoundsModelHistory(QtCore.QAbstractTableModel):
    def __init__(self, parent, rounds_data: list) -> None:
        super().__init__(parent)
        self.rounds_data = deepcopy(rounds_data)
        # print(self.rounds_data)
        print(hex(id(self.rounds_data)))
        self.add_blank_column()
        self.headers = ["Spot", "Id", "Name", "score", "Vs.", "score", "Id", "Name"]

    def dicts_to_list(self, dicts):
        return [[d[key] for key in self.headers] for d in dicts]

    def add_blank_column(self):
        for round in self.rounds_data:
            round.insert(4, "")

    def rowCount(self, index):
        return len(self.rounds_data)

    def columnCount(self, index):
        return len(self.headers)

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
            return self.rounds_data[index.row()][index.column()]

        if role == QtCore.Qt.BackgroundRole:
            if index.column() == 4:
                return QtGui.QBrush(QtGui.QColor(205, 205, 205))
        if role == QtCore.Qt.FontRole:
            if index.column() == 4:
                return QtGui.QFont("Arial", 10, QtGui.QFont.Bold)

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self.headers[section]


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, parent, table_data) -> None:
        super().__init__(parent)
        self.table_data = table_data
        self.headers = ["Id", "Nombre", "Puntos"]

    def rowCount(self, index):
        return len(self.table_data)

    def columnCount(self, index):
        return len(self.headers)

    def data(self, index, role):
        value = self.table_data[index.row()][index.column()]
        if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
            if isinstance(value, float):
                if value == 0.5:
                    return "\u00bd"
                return str(value).replace(".5", "\u00bd")
            return str(value)

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self.headers[section]

    def flags(self, index) -> QtCore.Qt.ItemFlags:
        return (
            QtCore.Qt.ItemIsSelectable
            | QtCore.Qt.ItemIsEnabled
            | QtCore.Qt.ItemIsEditable
        )

    def setData(self, index, value, role):
        if role == QtCore.Qt.EditRole:
            row = index.row()
            column = index.column()
            self.table_data[row][column] = value
        return False

    def removeRows(self, position, rows, parent=QtCore.QModelIndex()):
        self.beginRemoveRows(parent, position, position + rows - 1)
        self.table_data.pop(position)
        self.endRemoveRows()
        self.layoutChanged.emit()
        return True

    def insertRows(self, position, rows, parent=QtCore.QModelIndex()):
        self.beginInsertRows(parent, position, position + rows - 1)
        legth = len(self.headers)
        self.table_data.insert(position, ["" for _ in range(legth)])
        self.endInsertRows()
        self.layoutChanged.emit()
        return True


class PlayersModel(QtCore.QAbstractTableModel):
    def __init__(self, parent, players_data) -> None:
        super().__init__(parent)
        self.players_data = players_data
        self.headers = self.players_data[0] if len(self.players_data) > 0 else []
        if len(self.headers) > 0 and self.headers in self.players_data:
            self.players_data.remove(self.headers)
        self.parent = parent

    def rowCount(self, index):
        return len(self.players_data)

    def columnCount(self, index):
        return len(self.headers)

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
            return self.players_data[index.row()][index.column()]

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self.headers[section]

    def flags(self, index) -> QtCore.Qt.ItemFlags:
        return (
            QtCore.Qt.ItemIsSelectable
            | QtCore.Qt.ItemIsEnabled
            | QtCore.Qt.ItemIsEditable
        )

    def setData(self, index, value, role):
        if role == QtCore.Qt.EditRole:
            row = index.row()
            column = index.column()
            self.players_data[row][column] = value
        return False

    def removeRows(self, position, rows, parent=QtCore.QModelIndex()):
        self.beginRemoveRows(parent, position, position + rows - 1)
        self.players_data.pop(position)
        self.endRemoveRows()
        self.layoutChanged.emit()
        return True

    def insertRows(self, position, rows, parent=QtCore.QModelIndex()):
        self.beginInsertRows(parent, position, position + rows - 1)
        length = len(self.headers)
        row_data = ["" for _ in range(length)]
        row_data[0] = 0 # pyright: ignore
        self.players_data.insert(position, row_data)
        self.endInsertRows()
        self.layoutChanged.emit()
        return True
