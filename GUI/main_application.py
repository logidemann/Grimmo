from ui_main_application import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton

class main_application(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Grimmo Application")
      
        self.accueil_1.clicked.connect(self.switch_to_acceuil_page)
        self.accueil_2.clicked.connect(self.switch_to_accueil_page)
        
        self.agenda_1.clicked.connect(self.switch_to_agenda_page)
        self.agenda_2.clicked.connect(self.switch_to_agenda_page)
        
        self.visites_1.clicked.connect(self.switch_to_visites_page)
        self.visites_2.clicked.connect(self.switch_to_visites_page)
        
        self.biens_1.clicked.connect(self.switch_to_biens_page)
        self.biens_2.clicked.connect(self.switch_to_biens_page)
        
        self.clients_1.clicked.connect(self.switch_to_clients_page)
        self.clients_2.clicked.connect(self.switch_to_clients_page)
        
        self.agents_1.clicked.connect(self.switch_to_agents_page)
        self.agents_2.clicked.connect(self.switch_to_agents_page)
        
        self.statistique_1.clicked.connect(self.switch_to_statistique_page)
        self.statistiques_2.clicked.connect(self.switch_to_statistique_page)
        
        self.parametre_1.clicked.connect(self.switch_to_parametre_page)
        self.parametre_2.clicked.connect(self.switch_to_parametre_page)
        
        
      
      
    def switch_to_acceuil_page(self):
        self.stackedWidget.setCurrentIndex(0)
        
    def switch_to_agenda_page(self):
        self.stackedWidget.setCurrentIndex(1)
        
    def switch_to_visites_page(self):
        self.stackedWidget.setCurrentIndex(2)
        
    def switch_to_biens_page(self):
        self.stackedWidget.setCurrentIndex(3)
        
    def switch_to_clients_page(self):
        self.stackedWidget.setCurrentIndex(4)
        
    def switch_to_agents_page(self):
        self.stackedWidget.setCurrentIndex(5)
        
    def switch_to_statistique_page(self):
        self.stackedWidget.setCurrentIndex(6)
        
    def switch_to_parametre_page(self):
        self.stackedWidget.setCurrentIndex(7)