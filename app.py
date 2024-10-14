import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from src.controller.login_c import LoginController
from src.controller.property_c import PropertyController

# Chemin vers les fichiers .ui
login_ui_path = "GUI/nouvelle_page_de_connexion.ui"
main_ui_path = "GUI/main_application.ui"

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.login_controller = LoginController()
        self.property_controller = PropertyController()

        # Charger la page de connexion
        self.login_window = uic.loadUi(login_ui_path, self)

        # Lier le bouton de connexion
        self.connect_btn = self.findChild(QtWidgets.QPushButton, 'connect_btn')
        self.connect_btn.clicked.connect(self.handle_login)

    def handle_login(self):
      try:
          # Récupérer les informations de connexion
          username = self.findChild(QtWidgets.QLineEdit, 'username').text()
          password = self.findChild(QtWidgets.QLineEdit, 'password').text()

          print(f"Username: {username}, Password: {password}")  # Debug info

          if self.login_controller.connect_ad():
              print("Connexion à AD réussie.")  # Debug info

              if self.login_controller.login(username, password):
                  QMessageBox.information(self, 'Succès', 'Connexion réussie !')
                  self.show_main_application()
              else:
                  QMessageBox.warning(self, 'Erreur', 'Nom d\'utilisateur ou mot de passe incorrect.')
          else:
              print("Échec de la connexion à AD.")  # Debug info

          # Déconnecter de l'AD
          self.login_controller.disconnect_ad()
      except Exception as e:
          print(f"Erreur lors de la connexion : {e}")
          QMessageBox.warning(self, 'Erreur', f'Une erreur est survenue : {str(e)}')


    def show_main_application(self):
        # Charger la page principale
        self.main_window = uic.loadUi(main_ui_path, self)
        self.main_window.show()
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
