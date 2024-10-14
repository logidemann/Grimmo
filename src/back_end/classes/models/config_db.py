import psycopg2
from psycopg2 import sql

class DatabaseConnector:
  def __init__(self, db_name, user, password, host, port=5432):
    """
    Initialise la connexion à la base de données PostgreSQL.
    """
    self.db_name = db_name
    self.user = user
    self.password = password
    self.host = host
    self.port = port
    self.connection = None
    self.cursor = None
    
  def connect(self):
    """
    Se connecte à la base de données PostgreSQL.
    """
    try:
      self.connection = psycopg2.connect(
        dbname=self.db_name,
        user=self.user,
        password=self.password,
        host=self.host,
        port=self.port
      )
      self.cursor = self.connection.cursor()
      print("Connexion réussie à la base de données.")
      return True
    except Exception as e:
      print(f"Erreur lors de la connexion à la base de données : {e}")
      return False
    
  def query(self, query_str, params=None):
    """
    Exécute une requête SQL sur la base de données.
    params : tuple ou liste de paramètres pour les requêtes paramétrées
    """
    try:
      if self.cursor:
        self.cursor.execute(query_str, params)
        # Si c'est une requête SELECT, on récupère les résultats
        if query_str.strip().lower().startswith("select"):
          return self.cursor.fetchall()
        # Pour les autres requêtes (INSERT, UPDATE, DELETE), on valide la transaction
        else:
          self.connection.commit()
          print("Requête exécutée avec succès.")
    except Exception as e:
      print(f"Erreur lors de l'exécution de la requête : {e}")
      
  def close(self):
    """
    Ferme la connexion à la base de données.
    """
    if self.connection:
      self.cursor.close()
      self.connection.close()
      print("Connexion à la base de données fermée.")
      
# Exemple d'utilisation
if __name__ == "__main__":
  db = DatabaseConnector("Grimmo", "postgres", "Admin2025!", "192.168.30.46")
  db.connect()
  
  result = db.query()
  if result:
    for row in result:
      print(row)
      
  db.close()