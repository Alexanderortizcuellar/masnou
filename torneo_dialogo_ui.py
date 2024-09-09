# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\ASUS\programming\qt_programs\masnou\torneo_dialogo.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(887, 831)
        Form.setMinimumSize(QtCore.QSize(500, 500))
        Form.setStyleSheet("QLineEdit,QDateEdit, QComboBox {\n"
"    padding:8px;\n"
"    font-size:16px;\n"
"    border-radius:5px;\n"
"    border:1px solid rgba(0,0,0,0.4);\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size:15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    padding: 8px auto;\n"
"    min-width:45px;\n"
"}\n"
"\n"
"QTableView {\n"
"    font-size:23px;\n"
"}\n"
"")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tour_navigator = QtWidgets.QStackedWidget(Form)
        self.tour_navigator.setStyleSheet("")
        self.tour_navigator.setObjectName("tour_navigator")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.frame = QtWidgets.QFrame(self.page)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.tour_name = QtWidgets.QLineEdit(self.frame)
        self.tour_name.setObjectName("tour_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.tour_name)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.tour_organizer = QtWidgets.QLineEdit(self.frame)
        self.tour_organizer.setObjectName("tour_organizer")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.tour_organizer)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.tour_place = QtWidgets.QLineEdit(self.frame)
        self.tour_place.setObjectName("tour_place")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.tour_place)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.tour_date = QtWidgets.QDateEdit(self.frame)
        self.tour_date.setCalendarPopup(True)
        self.tour_date.setObjectName("tour_date")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.tour_date)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.verticalLayout.addWidget(self.frame)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.frame_2 = QtWidgets.QFrame(self.page)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.next_screen = QtWidgets.QPushButton(self.frame_2)
        self.next_screen.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.next_screen.setStyleSheet("QPushButton {\n"
"    font-size:17px;\n"
"    border:1px solid black;\n"
"    width:100px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border:1px solid blue;\n"
"    background-color: rgba(0, 85, 255, 40);\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    border:1px solid blue;\n"
"}")
        self.next_screen.setObjectName("next_screen")
        self.horizontalLayout.addWidget(self.next_screen)
        self.verticalLayout.addWidget(self.frame_2)
        self.tour_navigator.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.player_table = QtWidgets.QTableView(self.page_2)
        self.player_table.setObjectName("player_table")
        self.verticalLayout_2.addWidget(self.player_table)
        self.frame_3 = QtWidgets.QFrame(self.page_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.previous_screen = QtWidgets.QPushButton(self.frame_3)
        self.previous_screen.setObjectName("previous_screen")
        self.horizontalLayout_2.addWidget(self.previous_screen)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.frame_3)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.tour_navigator.addWidget(self.page_2)
        self.verticalLayout_3.addWidget(self.tour_navigator)

        self.retranslateUi(Form)
        self.tour_navigator.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Nuevo Torneo"))
        self.label_5.setText(_translate("Form", "Opciones de Torneo"))
        self.label.setText(_translate("Form", "Nombre"))
        self.tour_name.setText(_translate("Form", "Torneo Masnou Excalibur"))
        self.label_2.setText(_translate("Form", "Organizador"))
        self.label_3.setText(_translate("Form", "Lugar"))
        self.tour_place.setText(_translate("Form", "Excalibur"))
        self.label_4.setText(_translate("Form", "Fecha"))
        self.label_7.setText(_translate("Form", "Color"))
        self.comboBox.setItemText(0, _translate("Form", "Blancas"))
        self.comboBox.setItemText(1, _translate("Form", "Negras"))
        self.next_screen.setText(_translate("Form", "Siguiente"))
        self.label_6.setText(_translate("Form", "Tabla de Jugadores"))
        self.previous_screen.setText(_translate("Form", "Regresar"))
