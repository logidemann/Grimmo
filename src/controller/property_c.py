import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from back_end.classes.models.config_db import DatabaseConnector

class PropertyController:
    def __init__(self):
        # Initialisation de la connexion à la base de données
        self.db = DatabaseConnector("Grimmo", "postgres", "Admin2025!", "192.168.30.46")

    def connect_db(self):
        """
        Connexion à la base de données.
        """
        return self.db.connect()

    def add_property(self, name, location, price):
        """
        Ajoute un bien immobilier à la base de données.
        """
        query = "INSERT INTO properties (name, location, price) VALUES (%s, %s, %s)"
        return self.db.query(query, (name, location, price))

    def get_properties(self):
        """
        Récupère tous les biens immobiliers de la base de données.
        """
        query = "SELECT * FROM properties"
        return self.db.query(query)

    def close_db(self):
        """
        Ferme la connexion à la base de données.
        """
        self.db.close()
