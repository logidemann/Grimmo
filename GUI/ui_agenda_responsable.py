# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'agenda_responsable.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(764, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(234, 231, 220);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"background-color: rgb(142, 141, 138);\n"
"}\n"
"\n"
"QPushButton{\n"
"color:white;\n"
"height: 30px;\n"
"border:none;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color:#F5FAFE;\n"
"color:rgb(142, 141, 138);\n"
"font-weight:bold;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(40, 0))
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(u":/images/00241_Real_Estate_logo_happy_house-04.webp"))

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.accueil_1 = QPushButton(self.icon_only_widget)
        self.accueil_1.setObjectName(u"accueil_1")
        icon = QIcon()
        icon.addFile(u":/images/logo_dashboard.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/images/logo_dashboard_gris.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.accueil_1.setIcon(icon)
        self.accueil_1.setCheckable(True)
        self.accueil_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.accueil_1)

        self.agenda_1 = QPushButton(self.icon_only_widget)
        self.agenda_1.setObjectName(u"agenda_1")
        icon1 = QIcon()
        icon1.addFile(u":/images/logo_agenda.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/images/logo_agenda_gris.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.agenda_1.setIcon(icon1)
        self.agenda_1.setCheckable(True)
        self.agenda_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.agenda_1)

        self.visites_1 = QPushButton(self.icon_only_widget)
        self.visites_1.setObjectName(u"visites_1")
        icon2 = QIcon()
        icon2.addFile(u":/images/47973.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/images/logo_visites_gris.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.visites_1.setIcon(icon2)
        self.visites_1.setCheckable(True)
        self.visites_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.visites_1)

        self.biens_1 = QPushButton(self.icon_only_widget)
        self.biens_1.setObjectName(u"biens_1")
        icon3 = QIcon()
        icon3.addFile(u":/images/logo_biens.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/images/logo_biens_gris.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.biens_1.setIcon(icon3)
        self.biens_1.setCheckable(True)
        self.biens_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.biens_1)

        self.clients_1 = QPushButton(self.icon_only_widget)
        self.clients_1.setObjectName(u"clients_1")
        icon4 = QIcon()
        icon4.addFile(u":/images/logo_client.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/images/logo_client_gris.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.clients_1.setIcon(icon4)
        self.clients_1.setCheckable(True)
        self.clients_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.clients_1)

        self.statistique_1 = QPushButton(self.icon_only_widget)
        self.statistique_1.setObjectName(u"statistique_1")
        icon5 = QIcon()
        icon5.addFile(u":/images/logo_statistique.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/images/logo_statistique_gris.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.statistique_1.setIcon(icon5)
        self.statistique_1.setCheckable(True)
        self.statistique_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.statistique_1)

        self.parametre_1 = QPushButton(self.icon_only_widget)
        self.parametre_1.setObjectName(u"parametre_1")
        icon6 = QIcon()
        icon6.addFile(u":/images/logo_parametre.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6.addFile(u":/images/logo_parametre_gris.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.parametre_1.setIcon(icon6)
        self.parametre_1.setCheckable(True)
        self.parametre_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.parametre_1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 173, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pushButton_7 = QPushButton(self.icon_only_widget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        icon7 = QIcon()
        icon7.addFile(u":/images/logo_connxion.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_7.setIcon(icon7)
        self.pushButton_7.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pushButton_7)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setStyleSheet(u"QWidget{\n"
"background-color: rgb(142, 141, 138);\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton{\n"
"color:white;\n"
"text-align:left;\n"
"height: 30px;\n"
"border:none;\n"
"padding-left:10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color:#F5FAFE;\n"
"color:rgb(142, 141, 138);\n"
"font-weight:bold;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 20, -1)
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 0))
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/images/00241_Real_Estate_logo_happy_house-04.webp"))

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_name_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.accueil_2 = QPushButton(self.icon_name_widget)
        self.accueil_2.setObjectName(u"accueil_2")
        self.accueil_2.setIcon(icon)
        self.accueil_2.setCheckable(True)
        self.accueil_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.accueil_2)

        self.agenda_2 = QPushButton(self.icon_name_widget)
        self.agenda_2.setObjectName(u"agenda_2")
        self.agenda_2.setIcon(icon1)
        self.agenda_2.setCheckable(True)
        self.agenda_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.agenda_2)

        self.visites_2 = QPushButton(self.icon_name_widget)
        self.visites_2.setObjectName(u"visites_2")
        self.visites_2.setIcon(icon2)
        self.visites_2.setCheckable(True)
        self.visites_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.visites_2)

        self.biens_2 = QPushButton(self.icon_name_widget)
        self.biens_2.setObjectName(u"biens_2")
        self.biens_2.setIcon(icon3)
        self.biens_2.setCheckable(True)
        self.biens_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.biens_2)

        self.clients_2 = QPushButton(self.icon_name_widget)
        self.clients_2.setObjectName(u"clients_2")
        self.clients_2.setIcon(icon4)
        self.clients_2.setCheckable(True)
        self.clients_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.clients_2)

        self.statistiques_2 = QPushButton(self.icon_name_widget)
        self.statistiques_2.setObjectName(u"statistiques_2")
        self.statistiques_2.setIcon(icon5)
        self.statistiques_2.setCheckable(True)
        self.statistiques_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.statistiques_2)

        self.parametre_2 = QPushButton(self.icon_name_widget)
        self.parametre_2.setObjectName(u"parametre_2")
        self.parametre_2.setIcon(icon6)
        self.parametre_2.setCheckable(True)
        self.parametre_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.parametre_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 173, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.pushButton_11 = QPushButton(self.icon_name_widget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setIcon(icon7)
        self.pushButton_11.setCheckable(True)

        self.verticalLayout_4.addWidget(self.pushButton_11)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        self.verticalLayout_5 = QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.header_widget = QWidget(self.main_menu)
        self.header_widget.setObjectName(u"header_widget")
        self.horizontalLayout_4 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.menu = QPushButton(self.header_widget)
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"border:none;")
        icon8 = QIcon()
        icon8.addFile(u":/images/logo_menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menu.setIcon(icon8)
        self.menu.setIconSize(QSize(20, 20))
        self.menu.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.menu)

        self.horizontalSpacer = QSpacerItem(135, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit = QLineEdit(self.header_widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.pushButton_16 = QPushButton(self.header_widget)
        self.pushButton_16.setObjectName(u"pushButton_16")
        icon9 = QIcon()
        icon9.addFile(u":/images/logo_recherche.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_16.setIcon(icon9)
        self.pushButton_16.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.pushButton_16)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(135, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.pushButton_17 = QPushButton(self.header_widget)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setStyleSheet(u"border:none;")
        icon10 = QIcon()
        icon10.addFile(u":/images/logo_compte.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_17.setIcon(icon10)

        self.horizontalLayout_4.addWidget(self.pushButton_17)


        self.verticalLayout_5.addWidget(self.header_widget)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.accueil_page = QWidget()
        self.accueil_page.setObjectName(u"accueil_page")
        self.label_4 = QLabel(self.accueil_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(170, 240, 191, 51))
        font1 = QFont()
        font1.setPointSize(20)
        self.label_4.setFont(font1)
        self.stackedWidget.addWidget(self.accueil_page)
        self.agenda_page = QWidget()
        self.agenda_page.setObjectName(u"agenda_page")
        self.label_5 = QLabel(self.agenda_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(180, 250, 191, 51))
        self.label_5.setFont(font1)
        self.stackedWidget.addWidget(self.agenda_page)
        self.visites_page = QWidget()
        self.visites_page.setObjectName(u"visites_page")
        self.label_6 = QLabel(self.visites_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(210, 230, 191, 51))
        self.label_6.setFont(font1)
        self.stackedWidget.addWidget(self.visites_page)
        self.biens_page = QWidget()
        self.biens_page.setObjectName(u"biens_page")
        self.label_7 = QLabel(self.biens_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(190, 230, 191, 51))
        self.label_7.setFont(font1)
        self.stackedWidget.addWidget(self.biens_page)
        self.clients_page_2 = QWidget()
        self.clients_page_2.setObjectName(u"clients_page_2")
        self.label_8 = QLabel(self.clients_page_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(150, 230, 221, 51))
        self.label_8.setFont(font1)
        self.stackedWidget.addWidget(self.clients_page_2)
        self.statistique_page = QWidget()
        self.statistique_page.setObjectName(u"statistique_page")
        self.label_10 = QLabel(self.statistique_page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(160, 260, 241, 51))
        self.label_10.setFont(font1)
        self.stackedWidget.addWidget(self.statistique_page)
        self.parametre_page = QWidget()
        self.parametre_page.setObjectName(u"parametre_page")
        self.label_9 = QLabel(self.parametre_page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(170, 230, 191, 51))
        self.label_9.setFont(font1)
        self.stackedWidget.addWidget(self.parametre_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menu.toggled.connect(self.icon_only_widget.setHidden)
        self.menu.toggled.connect(self.icon_name_widget.setVisible)
        self.parametre_1.toggled.connect(self.parametre_2.setChecked)
        self.statistique_1.toggled.connect(self.statistiques_2.setChecked)
        self.clients_1.toggled.connect(self.clients_2.setChecked)
        self.biens_1.toggled.connect(self.biens_2.setChecked)
        self.visites_1.toggled.connect(self.visites_2.setChecked)
        self.agenda_1.toggled.connect(self.agenda_2.setChecked)
        self.agenda_2.toggled.connect(self.agenda_1.setChecked)
        self.visites_2.toggled.connect(self.visites_1.setChecked)
        self.biens_2.toggled.connect(self.biens_1.setChecked)
        self.clients_2.toggled.connect(self.clients_1.setChecked)
        self.statistiques_2.toggled.connect(self.statistique_1.setChecked)
        self.parametre_2.toggled.connect(self.parametre_1.setChecked)
        self.accueil_1.toggled.connect(self.accueil_2.setChecked)
        self.accueil_2.toggled.connect(self.accueil_1.setChecked)
        self.pushButton_7.toggled.connect(MainWindow.close)
        self.pushButton_11.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.accueil_1.setText("")
        self.agenda_1.setText("")
        self.visites_1.setText("")
        self.biens_1.setText("")
        self.clients_1.setText("")
        self.statistique_1.setText("")
        self.parametre_1.setText("")
        self.pushButton_7.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"SideBar", None))
        self.accueil_2.setText(QCoreApplication.translate("MainWindow", u"Accueil", None))
        self.agenda_2.setText(QCoreApplication.translate("MainWindow", u"Agenda", None))
        self.visites_2.setText(QCoreApplication.translate("MainWindow", u"Visites", None))
        self.biens_2.setText(QCoreApplication.translate("MainWindow", u"Biens", None))
        self.clients_2.setText(QCoreApplication.translate("MainWindow", u"Clients", None))
        self.statistiques_2.setText(QCoreApplication.translate("MainWindow", u"Statistiques", None))
        self.parametre_2.setText(QCoreApplication.translate("MainWindow", u"Param\u00e8tre", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"D\u00e9connexion", None))
        self.menu.setText("")
        self.pushButton_16.setText("")
        self.pushButton_17.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Accueil page", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Agenda page", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Visites page", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Biens page", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Clients page", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Statistiques page", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Param\u00e8tre page", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())