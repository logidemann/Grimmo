CREATE DOMAIN check_mail AS varchar(30) CHECK (VALUE ~ '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$');
CREATE DOMAIN check_tel AS varchar(10) CHECK (VALUE ~ '^[0-9]{10}$');
CREATE DOMAIN check_Cpost AS varchar(5) CHECK (VALUE ~ '^[0-9]{5}$');

CREATE TABLE Clients(
   id_client INT not null,
   mail_client check_mail,
   pren_client VARCHAR(50),
   nom_client VARCHAR(50),
   num_tel check_tel, 
   rue_client VARCHAR(50),
   ville_client VARCHAR(40),
   cdp_client check_Cpost, 
   
   PRIMARY KEY(id_client)

);

CREATE TABLE Propriétaires(
   id_prop INT not null,
   mail_prop  check_mail, 
   prenom_prop VARCHAR(20),
   nom_prop VARCHAR(20),
   num_tel_prop  check_tel, 
   rue_prop VARCHAR(40),
   Ville_prop VARCHAR(30),
   cdp_prop  check_Cpost, 

   PRIMARY KEY(id_prop)
);

CREATE TABLE Type(
   identifiant_typ INT not null,
   Lib_type VARCHAR(15),

   PRIMARY KEY(identifiant_typ)
);

CREATE TABLE Biens(
   id_biens INT not null,
   Ville_biens VARCHAR(30),
   rue_biens VARCHAR(30),
   cdp_biens  check_Cpost, 
   Surf_biens DECIMAL(4,2), 
   ann_constr_biens INT,
   num_porte_biens INT,
   etag_biens INT,
   stat_biens VARCHAR(50), 
   identifiant_typ INT NOT NULL,
   id_prop INT NOT NULL,
   PRIMARY KEY(id_biens),

   FOREIGN KEY(identifiant_typ) REFERENCES Type(identifiant_typ),
   FOREIGN KEY(id_prop) REFERENCES Propriétaires(id_prop),
   CONSTRAINT check_surf CHECK (Surf_biens > 0),
   CONSTRAINT check_ann CHECK (ann_constr_biens > 0)

);

CREATE TABLE Visites(
   id_visi INT not null,
   dat_dema_visite DATE,
   sta_visi VARCHAR(50),
   id_biens INT NOT NULL,
   id_client INT NOT NULL,

   PRIMARY KEY(id_visi),
   FOREIGN KEY(id_biens) REFERENCES Biens(id_biens),
   FOREIGN KEY(id_client) REFERENCES Clients(id_client)
);

CREATE TABLE Loué(
   id_client INT not null,
   id_biens INT not null,

   PRIMARY KEY(id_client, id_biens),
   FOREIGN KEY(id_client) REFERENCES Clients(id_client),
   FOREIGN KEY(id_biens) REFERENCES Biens(id_biens)
);
