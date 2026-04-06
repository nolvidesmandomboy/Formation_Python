-- Création des tables
CREATE TABLE artiste (
    nom VARCHAR, 
    artiste_id INTEGER NOT NULL PRIMARY KEY, 
    album_id INTEGER);

CREATE TABLE album (
    album_id INTEGER NOT NULL PRIMARY KEY, 
    artiste_id INTEGER REFERENCES artiste, 
    titre VARCHAR,
    annee_sortie INTEGER);

-- Modification des clés primaires des tables pour qu'elles s'implémentent automatiquement sans qu'on ait besoin d'écrire manuellement
ALTER TABLE artiste
    ALTER COLUMN artiste_id
    ADD GENERATED ALWAYS AS IDENTITY;

ALTER TABLE album
    ALTER COLUMN album_id
    ADD GENERATED ALWAYS AS IDENTITY;

-- insertion de nouvelles valeurs dans les tables
INSERT INTO artiste (nom) VALUES ('Michael Jackson');
INSERT INTO artiste (nom) VALUES ('PNL');
INSERT INTO artiste (nom) VALUES ('Youssoupha');
INSERT INTO album (titre, annee_sortie) VALUES ('Thriller', 1982);
INSERT INTO album (titre, annee_sortie) VALUES ('Deux frères', 2019);
INSERT INTO album (titre, annee_sortie, artiste_id) VALUES ('Polaroid Experience', 2018, 3);
INSERT INTO album (titre, annee_sortie, artiste_id) VALUES ('Dans la légende', 2016, 2)

-- Mise à jour des tables
UPDATE album SET artiste_id = 1 WHERE titre = 'Thriller';
UPDATE album SET artiste_id = 2 WHERE titre = 'Deux frères';
UPDATE artiste SET album_id = 1 WHERE artiste_id = 1;
UPDATE artiste SET album_id = 2 WHERE artiste_id = 2;
UPDATE artiste SET album_id = 3 WHERE artiste_id = 3;

ALTER TABLE artiste
DROP COLUMN album_id;

-- Visualisation
SELECT * FROM artiste
SELECT * FROM album

SELECT nom, titre FROM artiste as ar JOIN album as al ON ar.artiste_id = al.artiste_id
SELECT nom, titre FROM artiste as ar JOIN album as al ON ar.artiste_id = 2 AND al.artiste_id = 2



