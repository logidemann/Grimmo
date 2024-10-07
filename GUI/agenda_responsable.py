from ui_agenda_responsable import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class agenda_responsable(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Agenda de Responsables")
        
        self.icon_name_widget.setHidden(True)
        
        self.accueil_1.clicked.connect(self.switch_to_accueilPage)
        self.accueil_2.clicked.connect(self.switch_to_accueilPage)
        
        self.agenda_1.clicked.connect(self.switch_to_agendaPage)
        self.agenda_2.clicked.connect(self.switch_to_agendaPage)
        
        self.visites_1.clicked.connect(self.switch_to_visitesPage)
        self.visites_2.clicked.connect(self.switch_to_visitesPage)
        
        self.biens_1.clicked.connect(self.switch_to_biensPage)
        self.biens_2.clicked.connect(self.switch_to_biensPage)
        
        self.clients_1.clicked.connect(self.switch_to_clientsPage)
        self.clients_2.clicked.connect(self.switch_to_clientsPage)
        
        self.statistique_1.clicked.connect(self.switch_to_statistiquesPage)
        self.statistiques_2.clicked.connect(self.switch_to_statistiquesPage)
        
        self.parametre_1.clicked.connect(self.switch_to_parametrePage)
        self.parametre_2.clicked.connect(self.switch_to_parametrePage)
    
        
    def switch_to_accueilPage(self):
        self.stackedWidget.setCurrentIndex(0)
        
    def switch_to_agendaPage(self):
        self.stackedWidget.setCurrentIndex(1)
        
    def switch_to_visitesPage(self):
        self.stackedWidget.setCurrentIndex(2)
        
    def switch_to_biensPage(self):
        self.stackedWidget.setCurrentIndex(3)
        
    def switch_to_clientsPage(self):
        self.stackedWidget.setCurrentIndex(4)
        
    def switch_to_statistiquesPage(self):
        self.stackedWidget.setCurrentIndex(5)
        
    def switch_to_parametrePage(self):
        self.stackedWidget.setCurrentIndex(6)