import random
import string
from ldap3 import Server, Connection, ALL, SUBTREE, MODIFY_ADD

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
        self.base_dn = f"dc={domain.split('.')[0]},dc={domain.split('.')[1]}"  # Base DN correct pour grimmo.local
        self.server = None
        self.connection = None

    def connect(self):
        """
        Se connecte au serveur LDAP (Active Directory) avec une authentification simple.
        """
        try:
            # Créer un serveur LDAP
            self.server = Server(self.server_ip, port=self.port, get_info=ALL)

            # Créer une connexion avec une authentification simple (simple bind)
            self.connection = Connection(
                self.server,
                user=f"{self.username}@{self.domain}",  # Format UPN (User Principal Name)
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

    def login(self, username, password):
        """
        Méthode de login pour vérifier si l'utilisateur peut se connecter avec ses informations.
        """
        try:
            login_dn = f"{username}@{self.domain}"
            # Test de connexion avec les informations fournies par l'utilisateur
            test_conn = Connection(self.server, user=login_dn, password=password, auto_bind=True)
            
            if test_conn.bound:
                print(f"Login réussi pour {username}.")
                test_conn.unbind()
                return True
            else:
                print(f"Login échoué pour {username}.")
                return False
        except Exception as e:
            print(f"Erreur lors de la tentative de login : {e}")
            return False

    def add_user(self, prenom, nom, ou='Users', group='Agent'):
        """
        Ajoute un nouvel utilisateur avec un nom d'utilisateur généré automatiquement
        et l'associe au groupe 'Agent' par défaut.
        """
        try:
            # Générer le nom complet et l'identifiant
            nom_complet = f"{prenom.capitalize()} {nom.capitalize()}"
            identifiant = f"{prenom[0].upper()}{nom.capitalize()}"

            # Générer un mot de passe temporaire
            mot_de_passe = "Azerty123"

            # DN pour la création d'un nouvel utilisateur dans Grimmo > Users
            user_dn = f"cn={nom_complet},ou={ou},ou=Grimmo,{self.base_dn}"

            # Attributs du nouvel utilisateur
            attributes = {
                'cn': nom_complet,
                'sn': nom,
                'givenName': prenom,
                'userPassword': mot_de_passe,
                'objectClass': ['person', 'top', 'organizationalPerson', 'user'],
                'sAMAccountName': identifiant,
                'userPrincipalName': f"{identifiant}@{self.domain}",
                'displayName': nom_complet,
                'userAccountControl': 514,
            }

            # Ajout de l'utilisateur dans l'AD
            self.connection.add(user_dn, attributes=attributes)

            if self.connection.result['description'] == 'success':
                print(f"Utilisateur {nom_complet} ajouté avec succès avec l'identifiant {identifiant}.")

                # Ajouter l'utilisateur au groupe "Agent"
                group_dn = f"cn={group},ou=Groups,ou=Grimmo,{self.base_dn}"  # DN du groupe Agent
                self.connection.modify(group_dn, {'member': [(MODIFY_ADD, [user_dn])]})

                if self.connection.result['description'] == 'success':
                    print(f"Utilisateur {nom_complet} ajouté au groupe {group}.")
                else:
                    print(f"Erreur lors de l'ajout de l'utilisateur au groupe {group}: {self.connection.result['description']}")
                
                # Activer le compte et forcer le changement de mot de passe à la première connexion
                self.connection.modify(user_dn, {
                    'userAccountControl': [(MODIFY_ADD, [512])],  # Activer le compte
                    'pwdLastSet': [(MODIFY_ADD, [0])]  # Forcer le changement de mot de passe à la première connexion
                })

                print(f"Le mot de passe temporaire pour {nom_complet} est : {mot_de_passe}")
                return True
            else:
                print(f"Erreur lors de l'ajout de l'utilisateur : {self.connection.result['description']}")
                return False
        except Exception as e:
            print(f"Erreur lors de l'ajout de l'utilisateur : {e}")
            return False

    def delete_user(self, prenom, nom, ou='Users'):
        """
        Supprime un utilisateur basé sur son prénom, nom et l'OU (Unité d'Organisation).
        """
        try:
            # Générer le nom complet
            nom_complet = f"{prenom.capitalize()} {nom.capitalize()}"

            # DN de l'utilisateur à supprimer
            user_dn = f"cn={nom_complet},ou={ou},ou=Grimmo,{self.base_dn}"

            # Supprimer l'utilisateur
            self.connection.delete(user_dn)

            if self.connection.result['description'] == 'success':
                print(f"Utilisateur {nom_complet} supprimé avec succès.")
                return True
            else:
                print(f"Erreur lors de la suppression de l'utilisateur {nom_complet} : {self.connection.result['description']}")
                return False
        except Exception as e:
            print(f"Erreur lors de la suppression de l'utilisateur : {e}")
            return False

    def get_all_users(self, max_results=100):
        """
        Effectue une recherche pour récupérer tous les utilisateurs du domaine AD.
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


# # Fichier de configuration principal
# if __name__ == '__main__':
#     # Paramètres du serveur AD
#     AD_SERVER_IP = '192.168.30.46'
#     AD_DOMAIN = 'grimmo.local'  # Domaine spécifié dans LDAP Admin
#     AD_USERNAME = 'Administrateur'  # Utilisateur spécifié dans LDAP Admin
#     AD_PASSWORD = 'Ad123'  # Mot de passe correct correspondant

#     # Créer une instance du connecteur AD
#     ad_connector = ADConnector(AD_SERVER_IP, AD_DOMAIN, AD_USERNAME, AD_PASSWORD)

#     # Se connecter à AD
#     if ad_connector.connect():
#         print("Connexion établie avec succès.")

#         # Tester le login
#         if ad_connector.login('JMoreno', 'Azerty123'):
#             print("Login réussi.")

#         # Ajouter un nouvel utilisateur
#         if ad_connector.add_user('titi', 'koko'):
#             print("Utilisateur ajouté avec succès.")

#         # Récupérer tous les utilisateurs
#         users = ad_connector.get_all_users(max_results=10)
#         print("Utilisateurs trouvés dans AD :")
#         for user in users:
#             print(user)
            
#         # Supprimer un utilisateur
#         if ad_connector.delete_user('titi', 'koko'):
#             print("Utilisateur supprimé avec succès.")
        
#         # Récupérer tous les utilisateurs
#         users = ad_connector.get_all_users(max_results=10)
#         print("Utilisateurs trouvés dans AD :")
#         for user in users:
#             print(user)

#         # Déconnexion
#         ad_connector.disconnect()
#     else:
#         print("Échec de la connexion.")
