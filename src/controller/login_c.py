import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from back_end.classes.models.config_ad import ADConnector

class LoginController:
    def __init__(self):
        # Configuration de la connexion à Active Directory
        self.AD_SERVER_IP = '192.168.30.46'
        self.AD_DOMAIN = 'grimmo.local'
        self.AD_USERNAME = 'Administrateur'
        self.AD_PASSWORD = 'Ad123'  
        self.ad_connector = ADConnector(self.AD_SERVER_IP, self.AD_DOMAIN, self.AD_USERNAME, self.AD_PASSWORD)
    
    def connect_ad(self):
        """
        Connecte à l'Active Directory.
        """
        return self.ad_connector.connect()

    def login(self, username, password):
        """
        Vérifie les informations de login via Active Directory.
        """
        return self.ad_connector.login(username, password)

    def disconnect_ad(self):
        """
        Déconnecte de l'AD.
        """
        self.ad_connector.disconnect()
