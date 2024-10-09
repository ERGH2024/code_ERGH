
CREATE TABLE Patient (
    id SERIAL PRIMARY KEY,
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
    id SERIAL PRIMARY KEY,
    nom VARCHAR(255),
    code_teletransmission VARCHAR(255)
);

CREATE TABLE PatientMutuelle (
    id SERIAL PRIMARY KEY,
    patient_id INT,
    mutuelle_id INT,
    numero_securite_sociale VARCHAR(255),
    taux_remboursement_65 FLOAT,
    taux_remboursement_30 FLOAT,
    taux_remboursement_15 FLOAT,
    FOREIGN KEY (patient_id) REFERENCES Patient(id),
    FOREIGN KEY (mutuelle_id) REFERENCES Mutuelle(id)
);

CREATE TABLE TVA_Marges (
    id SERIAL PRIMARY KEY,
    taux_tva FLOAT,
    categorie VARCHAR(50),
    coef_marge FLOAT
);

CREATE TABLE Medicament (
    id SERIAL PRIMARY KEY,
    produit_id INT NOT NULL,
    DCI VARCHAR(255), 
    dosage VARCHAR(50),
    forme VARCHAR(50),
    code_cis VARCHAR(50),
    unites_volume VARCHAR(50),
    titulaire_amm VARCHAR(255),
    date_expiration DATE,
    FOREIGN KEY (produit_id) REFERENCES Produit(id)
);


CREATE TABLE Ordonnance (
    id SERIAL PRIMARY KEY,
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
    id SERIAL PRIMARY KEY,
    ordonnance_id INT NULL, -- Ordonnance optionnelle
    patient_id INT,  -- Ajout du lien avec Patient
    date_facturation DATE,
    montant FLOAT,
    statut_facturation VARCHAR(50),
    medicaments_delivres JSON,
    unites_delivrees JSON,
    FOREIGN KEY (ordonnance_id) REFERENCES Ordonnance(id),
    FOREIGN KEY (patient_id) REFERENCES Patient(id)  -- Lien vers Patient
);

CREATE TABLE Stock (
    id SERIAL PRIMARY KEY,
    medicament_id INT,
    quantite INT,
    date_mouvement DATE,
    raison VARCHAR(255),
    FOREIGN KEY (medicament_id) REFERENCES Medicament(id)
);

CREATE TABLE Utilisateur (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(255),
    prenom VARCHAR(255),
    role VARCHAR(50),
    email VARCHAR(255),
    mot_de_passe VARCHAR(255),
    code_simple VARCHAR(50),
    mode_authentification VARCHAR(50)
);

CREATE TABLE JournalActivites (
    id SERIAL PRIMARY KEY,
    utilisateur_id INT,
    date_activite TIMESTAMP,
    type_activite VARCHAR(255),
    description TEXT,
    FOREIGN KEY (utilisateur_id) REFERENCES Utilisateur(id)
);

CREATE TABLE SessionsUtilisateur (
    id SERIAL PRIMARY KEY,
    utilisateur_id INT,
    date_debut TIMESTAMP,
    date_fin TIMESTAMP,
    FOREIGN KEY (utilisateur_id) REFERENCES Utilisateur(id)
);

CREATE TABLE Produit (
    id SERIAL PRIMARY KEY,
    nom_produit VARCHAR(255) NOT NULL,
    prix FLOAT NOT NULL,
    description TEXT,
    est_medicament BOOLEAN NOT NULL DEFAULT FALSE, -- Indique si c'est un médicament
    quantite_stock INT NOT NULL,
    taux_tva_id INT, -- Lien vers la table TVA_Marges
    FOREIGN KEY (taux_tva_id) REFERENCES TVA_Marges(id)
);
