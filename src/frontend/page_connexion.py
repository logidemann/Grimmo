import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from back_end.classes.models.config_ad import ADConnector

# Chemin vers ton fichier .ui (chemin relatif)
ui_file_path = "GUI/page_connexion.ui"

class PageConnexion(QtWidgets.QMainWindow):
    def __init__(self):
        super(PageConnexion, self).__init__()
        # Chargement de la page .ui
        uic.loadUi(ui_file_path, self)

        # Trouver les éléments de la page (bouton et champs de saisie)
        self.connect_btn = self.findChild(QPushButton, 'connect_btn')
        self.username_login = self.findChild(QLineEdit, 'username')
        self.password_login = self.findChild(QLineEdit, 'password')

        # Connecter le bouton à la méthode de login
        self.connect_btn.clicked.connect(self.login_user)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # Création de l'instance de la fenêtre
    window = PageConnexion()

    # Affichage de la fenêtre
    window.show()

    # Boucle d'exécution de l'application
    sys.exit(app.exec_())
