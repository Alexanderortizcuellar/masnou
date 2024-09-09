# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\ASUS\programming\qt_programs\masnou\masnou.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1021, 820)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.navigator = QtWidgets.QStackedWidget(self.centralwidget)
        self.navigator.setStyleSheet("QLineEdit,QDateEdit {\n"
"    padding:8px;\n"
"    font-size:15px;\n"
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
"")
        self.navigator.setObjectName("navigator")
        self.main = QtWidgets.QWidget()
        self.main.setObjectName("main")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.main)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_5 = QtWidgets.QFrame(self.main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_5.setStyleSheet("QLineEdit,QDateEdit {\n"
"    padding:8px;\n"
"    font-size:15px;\n"
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
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_8.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.frame_5)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 35))
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_8.addWidget(self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(20, 90, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_8.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setStyleSheet("margin-bottom:9px")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_8.addWidget(self.label_4)
        self.menu_btn_create = QtWidgets.QPushButton(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.menu_btn_create.setFont(font)
        self.menu_btn_create.setObjectName("menu_btn_create")
        self.verticalLayout_8.addWidget(self.menu_btn_create)
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_8.addWidget(self.pushButton_10)
        self.menu_btn_go_tour = QtWidgets.QPushButton(self.frame_5)
        self.menu_btn_go_tour.setEnabled(False)
        self.menu_btn_go_tour.setObjectName("menu_btn_go_tour")
        self.verticalLayout_8.addWidget(self.menu_btn_go_tour)
        self.menu_btn_finish = QtWidgets.QPushButton(self.frame_5)
        self.menu_btn_finish.setEnabled(False)
        self.menu_btn_finish.setObjectName("menu_btn_finish")
        self.verticalLayout_8.addWidget(self.menu_btn_finish)
        self.menu_btn_quit = QtWidgets.QPushButton(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.menu_btn_quit.setFont(font)
        self.menu_btn_quit.setObjectName("menu_btn_quit")
        self.verticalLayout_8.addWidget(self.menu_btn_quit)
        spacerItem1 = QtWidgets.QSpacerItem(20, 150, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem1)
        self.horizontalLayout_6.addWidget(self.frame_5)
        self.board_container = QtWidgets.QFrame(self.main)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.board_container.setFont(font)
        self.board_container.setStyleSheet("")
        self.board_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.board_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.board_container.setObjectName("board_container")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.board_container)
        self.verticalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.puzzle_title = QtWidgets.QLabel(self.board_container)
        self.puzzle_title.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(9)
        font.setStrikeOut(False)
        self.puzzle_title.setFont(font)
        self.puzzle_title.setStyleSheet("font: 75 15pt \"MS Shell Dlg 2\";")
        self.puzzle_title.setAlignment(QtCore.Qt.AlignCenter)
        self.puzzle_title.setObjectName("puzzle_title")
        self.verticalLayout_9.addWidget(self.puzzle_title)
        self.horizontalLayout_6.addWidget(self.board_container)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 2)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        self.navigator.addWidget(self.main)
        self.tournament = QtWidgets.QWidget()
        self.tournament.setObjectName("tournament")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tournament)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.tournament)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tournament_title = QtWidgets.QLabel(self.frame_2)
        self.tournament_title.setText("")
        self.tournament_title.setObjectName("tournament_title")
        self.verticalLayout_4.addWidget(self.tournament_title)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.score_table = QtWidgets.QTableView(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.score_table.setFont(font)
        self.score_table.setObjectName("score_table")
        self.horizontalLayout_3.addWidget(self.score_table)
        self.rondas_main_table = QtWidgets.QTableView(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rondas_main_table.setFont(font)
        self.rondas_main_table.setShowGrid(True)
        self.rondas_main_table.setGridStyle(QtCore.Qt.SolidLine)
        self.rondas_main_table.setSortingEnabled(True)
        self.rondas_main_table.setObjectName("rondas_main_table")
        self.horizontalLayout_3.addWidget(self.rondas_main_table)
        self.fila_list = QtWidgets.QListView(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fila_list.setFont(font)
        self.fila_list.setObjectName("fila_list")
        self.horizontalLayout_3.addWidget(self.fila_list)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout_4.addWidget(self.frame_3)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tournament)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.update_button = QtWidgets.QPushButton(self.groupBox_3)
        self.update_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.update_button.setObjectName("update_button")
        self.horizontalLayout_2.addWidget(self.update_button)
        self.edit_players_button = QtWidgets.QPushButton(self.groupBox_3)
        self.edit_players_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.edit_players_button.setObjectName("edit_players_button")
        self.horizontalLayout_2.addWidget(self.edit_players_button)
        self.ver_fila_button = QtWidgets.QPushButton(self.groupBox_3)
        self.ver_fila_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ver_fila_button.setObjectName("ver_fila_button")
        self.horizontalLayout_2.addWidget(self.ver_fila_button)
        self.ver_rondas_button = QtWidgets.QPushButton(self.groupBox_3)
        self.ver_rondas_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ver_rondas_button.setObjectName("ver_rondas_button")
        self.horizontalLayout_2.addWidget(self.ver_rondas_button)
        self.finish_button = QtWidgets.QPushButton(self.groupBox_3)
        self.finish_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.finish_button.setObjectName("finish_button")
        self.horizontalLayout_2.addWidget(self.finish_button)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.navigator.addWidget(self.tournament)
        self.fila_page = QtWidgets.QWidget()
        self.fila_page.setObjectName("fila_page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.fila_page)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame = QtWidgets.QFrame(self.fila_page)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.fila_list_main = QtWidgets.QListView(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fila_list_main.setFont(font)
        self.fila_list_main.setObjectName("fila_list_main")
        self.horizontalLayout_4.addWidget(self.fila_list_main)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.add_fila_btn = QtWidgets.QPushButton(self.frame_4)
        self.add_fila_btn.setObjectName("add_fila_btn")
        self.verticalLayout_6.addWidget(self.add_fila_btn)
        self.del_fila_btn = QtWidgets.QPushButton(self.frame_4)
        self.del_fila_btn.setObjectName("del_fila_btn")
        self.verticalLayout_6.addWidget(self.del_fila_btn)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_6.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_6.addWidget(self.pushButton_5)
        self.sort_fila_btn = QtWidgets.QPushButton(self.frame_4)
        self.sort_fila_btn.setObjectName("sort_fila_btn")
        self.verticalLayout_6.addWidget(self.sort_fila_btn)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem3)
        self.save_changes_fila = QtWidgets.QPushButton(self.frame_4)
        self.save_changes_fila.setObjectName("save_changes_fila")
        self.verticalLayout_6.addWidget(self.save_changes_fila)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem4)
        self.horizontalLayout_4.addWidget(self.frame_4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout_5.addWidget(self.frame)
        self.navigator.addWidget(self.fila_page)
        self.players_page = QtWidgets.QWidget()
        self.players_page.setObjectName("players_page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.players_page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.players_page)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.players_table = QtWidgets.QTableView(self.players_page)
        self.players_table.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.players_table.setObjectName("players_table")
        self.verticalLayout_2.addWidget(self.players_table)
        self.groupBox = QtWidgets.QGroupBox(self.players_page)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.players_save_changes = QtWidgets.QPushButton(self.groupBox)
        self.players_save_changes.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.players_save_changes.setObjectName("players_save_changes")
        self.horizontalLayout.addWidget(self.players_save_changes)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.navigator.addWidget(self.players_page)
        self.rondas_page = QtWidgets.QWidget()
        self.rondas_page.setObjectName("rondas_page")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.rondas_page)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.tabWidget = QtWidgets.QTabWidget(self.rondas_page)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.rondas_table = QtWidgets.QTableView(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rondas_table.setFont(font)
        self.rondas_table.setObjectName("rondas_table")
        self.verticalLayout_7.addWidget(self.rondas_table)
        self.tabWidget.addTab(self.tab, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tab2)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.rondas_history_table = QtWidgets.QTableView(self.tab2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rondas_history_table.setFont(font)
        self.rondas_history_table.setObjectName("rondas_history_table")
        self.verticalLayout_11.addWidget(self.rondas_history_table)
        self.tabWidget.addTab(self.tab2, "")
        self.verticalLayout_10.addWidget(self.tabWidget)
        self.groupBox_2 = QtWidgets.QGroupBox(self.rondas_page)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.rondas_save_changes = QtWidgets.QPushButton(self.groupBox_2)
        self.rondas_save_changes.setObjectName("rondas_save_changes")
        self.horizontalLayout_5.addWidget(self.rondas_save_changes)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.verticalLayout_10.addWidget(self.groupBox_2)
        self.navigator.addWidget(self.rondas_page)
        self.details_page = QtWidgets.QWidget()
        self.details_page.setObjectName("details_page")
        self.navigator.addWidget(self.details_page)
        self.stats_page = QtWidgets.QWidget()
        self.stats_page.setObjectName("stats_page")
        self.navigator.addWidget(self.stats_page)
        self.problema_page = QtWidgets.QWidget()
        self.problema_page.setObjectName("problema_page")
        self.navigator.addWidget(self.problema_page)
        self.verticalLayout.addWidget(self.navigator)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1021, 26))
        self.menubar.setObjectName("menubar")
        self.menu_Archivo = QtWidgets.QMenu(self.menubar)
        self.menu_Archivo.setObjectName("menu_Archivo")
        self.menu_Torneos = QtWidgets.QMenu(self.menubar)
        self.menu_Torneos.setObjectName("menu_Torneos")
        self.menu_Players = QtWidgets.QMenu(self.menubar)
        self.menu_Players.setObjectName("menu_Players")
        self.menu_About = QtWidgets.QMenu(self.menubar)
        self.menu_About.setObjectName("menu_About")
        self.menu_Navegacion = QtWidgets.QMenu(self.menubar)
        self.menu_Navegacion.setObjectName("menu_Navegacion")
        self.menu_Ir_a = QtWidgets.QMenu(self.menu_Navegacion)
        self.menu_Ir_a.setObjectName("menu_Ir_a")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_Cargar_Juagadores = QtWidgets.QAction(MainWindow)
        self.action_Cargar_Juagadores.setObjectName("action_Cargar_Juagadores")
        self.action_Acerca_de = QtWidgets.QAction(MainWindow)
        self.action_Acerca_de.setObjectName("action_Acerca_de")
        self.action_Ajustes = QtWidgets.QAction(MainWindow)
        self.action_Ajustes.setObjectName("action_Ajustes")
        self.action_Nuevo_Torneo = QtWidgets.QAction(MainWindow)
        self.action_Nuevo_Torneo.setObjectName("action_Nuevo_Torneo")
        self.action_Terminar_Torneo = QtWidgets.QAction(MainWindow)
        self.action_Terminar_Torneo.setObjectName("action_Terminar_Torneo")
        self.action_Crear_tabla = QtWidgets.QAction(MainWindow)
        self.action_Crear_tabla.setObjectName("action_Crear_tabla")
        self.action_Torneo_Actual = QtWidgets.QAction(MainWindow)
        self.action_Torneo_Actual.setEnabled(False)
        self.action_Torneo_Actual.setObjectName("action_Torneo_Actual")
        self.action_Editar_Jugadores = QtWidgets.QAction(MainWindow)
        self.action_Editar_Jugadores.setEnabled(False)
        self.action_Editar_Jugadores.setObjectName("action_Editar_Jugadores")
        self.action_Rondas = QtWidgets.QAction(MainWindow)
        self.action_Rondas.setEnabled(False)
        self.action_Rondas.setObjectName("action_Rondas")
        self.action_Detalles = QtWidgets.QAction(MainWindow)
        self.action_Detalles.setEnabled(False)
        self.action_Detalles.setObjectName("action_Detalles")
        self.actionE_stadisticas = QtWidgets.QAction(MainWindow)
        self.actionE_stadisticas.setObjectName("actionE_stadisticas")
        self.action_Exportar = QtWidgets.QAction(MainWindow)
        self.action_Exportar.setObjectName("action_Exportar")
        self.action_Exportar_2 = QtWidgets.QAction(MainWindow)
        self.action_Exportar_2.setObjectName("action_Exportar_2")
        self.action_Cargar_Torneo = QtWidgets.QAction(MainWindow)
        self.action_Cargar_Torneo.setObjectName("action_Cargar_Torneo")
        self.action_Men = QtWidgets.QAction(MainWindow)
        self.action_Men.setObjectName("action_Men")
        self.menu_Archivo.addAction(self.action_Cargar_Juagadores)
        self.menu_Archivo.addAction(self.action_Cargar_Torneo)
        self.menu_Torneos.addAction(self.action_Nuevo_Torneo)
        self.menu_Torneos.addAction(self.action_Terminar_Torneo)
        self.menu_Torneos.addAction(self.action_Exportar_2)
        self.menu_Players.addAction(self.action_Crear_tabla)
        self.menu_Players.addAction(self.action_Exportar)
        self.menu_About.addAction(self.action_Ajustes)
        self.menu_About.addAction(self.action_Acerca_de)
        self.menu_Ir_a.addAction(self.action_Torneo_Actual)
        self.menu_Ir_a.addAction(self.action_Editar_Jugadores)
        self.menu_Ir_a.addAction(self.action_Rondas)
        self.menu_Ir_a.addAction(self.action_Detalles)
        self.menu_Ir_a.addAction(self.actionE_stadisticas)
        self.menu_Ir_a.addAction(self.action_Men)
        self.menu_Navegacion.addAction(self.menu_Ir_a.menuAction())
        self.menubar.addAction(self.menu_Archivo.menuAction())
        self.menubar.addAction(self.menu_Torneos.menuAction())
        self.menubar.addAction(self.menu_Players.menuAction())
        self.menubar.addAction(self.menu_Navegacion.menuAction())
        self.menubar.addAction(self.menu_About.menuAction())

        self.retranslateUi(MainWindow)
        self.navigator.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Masnou Manager"))
        self.label_2.setText(_translate("MainWindow", "Torneos Recientes"))
        self.label_4.setText(_translate("MainWindow", "Opciones"))
        self.menu_btn_create.setText(_translate("MainWindow", "Crear Torneo"))
        self.pushButton_10.setToolTip(_translate("MainWindow", "<html><head/><body><p>Cargar un torneo en modo de lectura</p></body></html>"))
        self.pushButton_10.setText(_translate("MainWindow", "Cargar Torneo"))
        self.menu_btn_go_tour.setText(_translate("MainWindow", "Ir a Torneo Activo"))
        self.menu_btn_finish.setText(_translate("MainWindow", "Terminar Torneo Activo"))
        self.menu_btn_quit.setText(_translate("MainWindow", "Salir"))
        self.puzzle_title.setText(_translate("MainWindow", "Problema del Dia"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Opciones"))
        self.update_button.setText(_translate("MainWindow", "Actualizar"))
        self.edit_players_button.setText(_translate("MainWindow", "Editar jugadores"))
        self.ver_fila_button.setText(_translate("MainWindow", "Ver Fila"))
        self.ver_rondas_button.setText(_translate("MainWindow", "Ver Rondas"))
        self.finish_button.setText(_translate("MainWindow", "Terminar Torneo"))
        self.add_fila_btn.setText(_translate("MainWindow", "Añadir"))
        self.del_fila_btn.setText(_translate("MainWindow", "Borrar"))
        self.pushButton_4.setText(_translate("MainWindow", "Mover Arriba"))
        self.pushButton_5.setText(_translate("MainWindow", "Mover Abajo"))
        self.sort_fila_btn.setText(_translate("MainWindow", "Sortear"))
        self.save_changes_fila.setText(_translate("MainWindow", "Guardar Cambios"))
        self.label.setText(_translate("MainWindow", "Jugadores"))
        self.groupBox.setTitle(_translate("MainWindow", "Opciones"))
        self.pushButton.setText(_translate("MainWindow", "Importar Jugadores"))
        self.players_save_changes.setText(_translate("MainWindow", "Aceptar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Rondas Actuales"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "Historial de Rondas"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Opciones"))
        self.rondas_save_changes.setText(_translate("MainWindow", "Guardar Cambios"))
        self.menu_Archivo.setTitle(_translate("MainWindow", "&Archivo"))
        self.menu_Torneos.setTitle(_translate("MainWindow", "&Torneo"))
        self.menu_Players.setTitle(_translate("MainWindow", "&Jugadores"))
        self.menu_About.setTitle(_translate("MainWindow", "&Ayuda"))
        self.menu_Navegacion.setTitle(_translate("MainWindow", "&Navegacion"))
        self.menu_Ir_a.setTitle(_translate("MainWindow", "&Ir a"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_Cargar_Juagadores.setText(_translate("MainWindow", "Cargar &Juagadores"))
        self.action_Acerca_de.setText(_translate("MainWindow", "&Acerca"))
        self.action_Ajustes.setText(_translate("MainWindow", "&Ajustes"))
        self.action_Nuevo_Torneo.setText(_translate("MainWindow", "&Nuevo Torneo"))
        self.action_Nuevo_Torneo.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.action_Terminar_Torneo.setText(_translate("MainWindow", "&Terminar Torneo"))
        self.action_Crear_tabla.setText(_translate("MainWindow", "&Crear tabla"))
        self.action_Torneo_Actual.setText(_translate("MainWindow", "&Torneo Actual"))
        self.action_Editar_Jugadores.setText(_translate("MainWindow", "&Editar Jugadores"))
        self.action_Rondas.setText(_translate("MainWindow", "&Rondas"))
        self.action_Detalles.setText(_translate("MainWindow", "&Detalles"))
        self.actionE_stadisticas.setText(_translate("MainWindow", "E&stadísticas"))
        self.action_Exportar.setText(_translate("MainWindow", "&Exportar"))
        self.action_Exportar_2.setText(_translate("MainWindow", "&Exportar"))
        self.action_Cargar_Torneo.setText(_translate("MainWindow", "&Cargar Torneo"))
        self.action_Men.setText(_translate("MainWindow", "&Menú"))
import images_rc
