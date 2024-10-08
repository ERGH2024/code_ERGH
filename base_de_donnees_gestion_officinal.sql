
CREATE TABLE Patient (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255),
    prenom VARCHAR(255),
    date_naissance DATE,
    adresse VARCHAR(255),
    telephone VARCHAR(20),
    email VARCHAR(255),
    amo VARCHAR(50),
    code_securite_sociale VARCHAR(255),
    code_ame VARCHAR(255),
    amc VARCHAR(50)
);

CREATE TABLE Mutuelle (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255),
    code_teletransmission VARCHAR(255)
);

CREATE TABLE PatientMutuelle (
    id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT,
    mutuelle_id INT,
    numero_securite_sociale VARCHAR(255),
    taux_remboursement_65 FLOAT,
    taux_remboursement_30 FLOAT,
    taux_remboursement_15 FLOAT,
    FOREIGN KEY (patient_id) REFERENCES Patient(id),
    FOREIGN KEY (mutuelle_id) REFERENCES Mutuelle(id)
);

CREATE TABLE Ordonnance (
    id INT PRIMARY KEY AUTO_INCREMENT,
    date_emission_medecin DATE,
    date_prise_en_charge DATE,
    duree_validite INT,
    nombre_utilisations INT,
    patient_id INT,
    medecin VARCHAR(255),
    type_ordonnance VARCHAR(50),
    medicaments JSON,
    statut VARCHAR(50),
    statut_facturation VARCHAR(50),
    FOREIGN KEY (patient_id) REFERENCES Patient(id)
);

CREATE TABLE Facturation (
    id INT PRIMARY KEY AUTO_INCREMENT,
    ordonnance_id INT,
    date_facturation DATE,
    montant FLOAT,
    statut_facturation VARCHAR(50),
    medicaments_delivres JSON,
    unites_delivrees JSON,
    FOREIGN KEY (ordonnance_id) REFERENCES Ordonnance(id)
);

CREATE TABLE Medicament (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom_commercial VARCHAR(255),
    DCI VARCHAR(255),
    dosage VARCHAR(50),
    forme VARCHAR(50),
    code_cis VARCHAR(50),
    prix FLOAT,
    unites_volume VARCHAR(50),
    quantite_stock INT,
    titulaire_amm VARCHAR(255),
    taux_tva_id INT,
    date_expiration DATE,
    description TEXT,
    FOREIGN KEY (taux_tva_id) REFERENCES TVA_Marges(id)
);

CREATE TABLE TVA_Marges (
    id INT PRIMARY KEY AUTO_INCREMENT,
    taux_tva FLOAT,
    categorie VARCHAR(50),
    coef_marge FLOAT
);

CREATE TABLE Stock (
    id INT PRIMARY KEY AUTO_INCREMENT,
    medicament_id INT,
    quantite INT,
    date_mouvement DATE,
    raison VARCHAR(255),
    FOREIGN KEY (medicament_id) REFERENCES Medicament(id)
);

CREATE TABLE Utilisateur (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255),
    prenom VARCHAR(255),
    role VARCHAR(50),
    email VARCHAR(255),
    mot_de_passe VARCHAR(255),
    code_simple VARCHAR(50),
    mode_authentification VARCHAR(50)
);

CREATE TABLE JournalActivites (
    id INT PRIMARY KEY AUTO_INCREMENT,
    utilisateur_id INT,
    date_activite DATETIME,
    type_activite VARCHAR(255),
    description TEXT,
    FOREIGN KEY (utilisateur_id) REFERENCES Utilisateur(id)
);

CREATE TABLE SessionsUtilisateur (
    id INT PRIMARY KEY AUTO_INCREMENT,
    utilisateur_id INT,
    date_debut DATETIME,
    date_fin DATETIME,
    FOREIGN KEY (utilisateur_id) REFERENCES Utilisateur(id)
);
