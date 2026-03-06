CREATE TABLE base_brigade (
    Code_brigade INTEGER PRIMARY KEY AUTOINCREMENT,
    Nom_brigade TEXT NOT NULL UNIQUE,
    Code_perimetre INTEGER,
    Code_dept TEXT,
    id_service INTEGER,
    FOREIGN KEY (Code_perimetre) REFERENCES perimetre(Code_perimetre),
    FOREIGN KEY (Code_dept) REFERENCES département(Code_dept),
    FOREIGN KEY (id_service) REFERENCES type_service(code_service)
);


CREATE TABLE Département (
    Code_dept TEXT NOT NULL UNIQUE PRIMARY KEY);


CREATE TABLE "Enregistrement" (
	"annee"	INTEGER,
	"Nom_service"	TEXT,
	"Code_dept"	TEXT,
	"Nom_perimetre"	TEXT,
	"Nom_brigade"	TEXT,
	"Code_infrac"	INTEGER,
	"nom_infrac"	TEXT,
	"nombre_fait"	INTEGER
);


CREATE TABLE Infraction (
    Code_infrac INTEGER UNIQUE PRIMARY KEY,
    Nom_Infrac TEXT NOT NULL UNIQUE);


CREATE TABLE perimetre (
    Code_perimetre INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
    Nom_perimetre TEXT NOT NULL UNIQUE);


CREATE TABLE "Population_dept" (
	"Code département"	INTEGER,
	"Année"	INTEGER,
	"Population totale"	INTEGER,
	"Total hommes"	INTEGER,
	"Total femmes"	INTEGER
);


CREATE TABLE Type_service (
    code_service INTEGER PRIMARY KEY AUTOINCREMENT,
    nom_service TEXT NOT NULL UNIQUE);