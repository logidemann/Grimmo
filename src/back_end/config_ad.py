from ldap3 import Server, Connection, ALL, SUBTREE

class ADConnector:
    def __init__(self, server_ip, domain, username, password, port=389):
        """
        Initialise la connexion LDAP avec les paramètres du serveur AD.
        """
        self.server_ip = server_ip
        self.domain = domain
        self.username = username
        self.password = password
        self.port = port
        self.base_dn = f"dc={domain.split('.')[0]},dc={domain.split('.')[1]}"
        self.server = None
        self.connection = None

    def connect(self):
        """
        Se connecte au serveur LDAP (Active Directory) avec une authentification simple.
        """
        try:
            # Créer un serveur LDAP
            self.server = Server(self.server_ip, port=self.port, get_info=ALL)

            # Créer une connexion avec une authentification simple
            self.connection = Connection(
                self.server,
                user=f"{self.username}@{self.domain}",
                password=self.password,
                auto_bind=True
            )

            # Vérifier si la connexion est établie
            if self.connection.bound:
                print("Connexion réussie au serveur LDAP.")
                return True
            else:
                print("Échec de la connexion au serveur LDAP.")
                return False
        except Exception as e:
            print(f"Erreur lors de la connexion à LDAP : {e}")
            return False

    def search_users(self, max_results=10):
        """
        Effectue une recherche pour récupérer les utilisateurs du domaine AD.
        Retourne une liste des utilisateurs trouvés.
        """
        try:
            # Définir le filtre de recherche pour les utilisateurs
            search_filter = '(objectClass=user)'

            # Effectuer la recherche LDAP
            self.connection.search(
                search_base=self.base_dn,
                search_filter=search_filter,
                search_scope=SUBTREE,
                attributes=['cn', 'sAMAccountName', 'mail'],
                size_limit=max_results
            )

            # Récupérer les résultats
            users = []
            for entry in self.connection.entries:
                users.append({
                    'cn': entry.cn.value,
                    'sAMAccountName': entry.sAMAccountName.value,
                    'mail': entry.mail.value if entry.mail else 'Aucun email'
                })

            return users

        except Exception as e:
            print(f"Erreur lors de la recherche des utilisateurs : {e}")
            return []

    def disconnect(self):
        """
        Déconnecte la connexion LDAP.
        """
        if self.connection:
            self.connection.unbind()
            print("Déconnexion du serveur LDAP réussie.")


# Fichier de configuration principal
if __name__ == '__main__':
    # Paramètres du serveur AD
    AD_SERVER_IP = '192.168.30.46'
    AD_DOMAIN = 'grimmo2025.local'
    AD_USERNAME = 'Administrateur'
    AD_PASSWORD = 'Ad123'  # Remplace par le mot de passe correct

    # Créer une instance du connecteur AD
    ad_connector = ADConnector(AD_SERVER_IP, AD_DOMAIN, AD_USERNAME, AD_PASSWORD)

    # Se connecter à AD
    if ad_connector.connect():
        # Effectuer une recherche d'utilisateurs
        users = ad_connector.search_users(max_results=10)
        print("Utilisateurs trouvés dans AD :")
        for user in users:
            print(user)

        # Déconnexion
        ad_connector.disconnect()
