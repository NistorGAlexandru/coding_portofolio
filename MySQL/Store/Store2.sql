CREATE DATABASE curs7_magazin;
USE  curs7_magazin;


#Tabela adrese
CREATE TABLE IF NOT EXISTS adresa
(id int unique auto_increment primary key,
strada char(20),
oras char(20));
 
#Tabela clienti
CREATE TABLE IF NOT EXISTS client
(id int unique auto_increment primary key,
denumire char(50),
adresa_id int,
INDEX (adresa_id),
FOREIGN KEY (adresa_id) REFERENCES adresa(id));
 
#Tabela comenzi
 CREATE TABLE IF NOT EXISTS comanda
(id int unique auto_increment primary key,
data date,
client_id int,
INDEX (client_id),
FOREIGN KEY (client_id) REFERENCES client(id));
 
#Tabela articole
 CREATE TABLE IF NOT EXISTS articol
(id int unique auto_increment primary key,
descriere char(40),
pret  float);
 
# Tabela de legatura dintre comenzi si articole (un articol poate sa apara in mai multe comenzi, o comanda are mai
#multe articole
 CREATE TABLE IF NOT EXISTS comanda_articol
(id int unique auto_increment primary key,
comanda_id int,
articol_id int,
cantitate int,
INDEX (comanda_id),
INDEX (articol_id),
FOREIGN KEY (comanda_id) REFERENCES comanda(id),
FOREIGN KEY (articol_id) REFERENCES articol(id));
-- Popularea tabelelor cu date

INSERT INTO adresa (strada, oras) VALUES
('Magheru', 'Bucuresti'),
('Brasov',  'Bucuresti'),
('Elisabeta', 'Bucuresti'),
('Maniu', 'Brasov'),
('Aviatorilor', 'Bucuresti'),
('Balcescu', 'Buzau'),
('Mihalache', 'Bucuresti'),
('Horea', 'Cluj Napoca'),
('Macaralei', 'Barlad'),
('Minerului', 'Petrosani');
 
##
INSERT INTO client (denumire, adresa_id) VALUES
('SC LEON SRL', 1),
('GEOMIL', 2),
('LIBERTY', 3),
('MINERON', 10),
('AEROFUN', 4),
('MEDITEL', 5);
 
##
INSERT INTO comanda (data, client_id) VALUES
('2023-4-8', 1),
('2023-4-8', 1),
('2023-4-7', 2),
('2022-4-8', 2),
('2022-4-9', 3),
('2022-4-8', 4),
('2021-4-8', 5);
 
##
INSERT INTO articol (descriere, pret) VALUES
('stilou', 5),
('pix bila', 4),
('creion', 0.5),
('marker', 2),
('guma', 0.75),
('rigla', 1),
('echer', 1),
('penar', 2),
('top hartie', 9.5),
('top hartie gloss', 9.5),
('cutie cerneala', 2.25);
 
##
INSERT INTO comanda_articol (comanda_id, articol_id, cantitate) VALUES
 
(1,1,10),
(1,2,10),
(1,3,10),
 
(2,4,2),
(2,5,4),
(2,6,12),
 
(3,8,20),
(3,5,42),
 
(4,1,20),
(4,2,40),
(4,3,20),
(4,4,40),
(4,5,20),
(4,6,20),
 
(5,1,100),
(5,7,200),
 
(6,2,25),
(6,6,25),
(7,3,100);