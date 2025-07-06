

/* SHOW DATABASES; */-- 
-- CREATE DATABASE FirstDatabase;

-- CREATE TABLE IF NOT EXISTS
--   FirstDatabase.Cars(brand VARCHAR(255));

USE FirstDatabase;
-- DROP TABLE IF EXISTS Cars;

-- INSERT INTO Cars VALUES ("Dacia");

SELECT * FROM Cars;
INSERT INTO Cars VALUES ("Ford");

SELECT * FROM Cars;

SELECT  COUNT(*) FROM Cars WHERE brand = "dacia";

SELECT DISTINCT * FROM Cars;

SELECT DISTINCT * FROM Cars WHERE brand = "dacia";

SET sql_safe_updates = 0;
UPDATE Cars SET brand = "logan" WHERE brand = "dacia";

SELECT * FROM Cars;

SHOW DATABASES;
USE FirstDatabase;

CREATE TABLE people
	(id INT AUTO_INCREMENT,
    nume VARCHAR(255),
	prenume VARCHAR(255),
    PRIMARY KEY(id)
    );

INSERT INTO people VALUES (1, "Ion", "Ionescu");

INSERT INTO people VALUES (3, "Don", "Donescu");
SELECT * FROM people;

INSERT INTO people (prenume, nume) VALUES ("Non", "Nonescu");


INSERT INTO people VALUES (2, "Ton", "Tonescu");
SELECT * FROM people;

INSERT INTO people (prenume, nume) VALUES ("Gon", "Gonescu");
SELECT * FROM people;

SELECT * FROM people ORDER BY nume ASC;
SELECT * FROM people ORDER BY nume DESC;

INSERT INTO people (prenume, nume, id)  
	VALUES ( "Ron", "Ronescu", 4);
SELECT * FROM people;

INSERT INTO people (prenume, id)  
	VALUES ( "Eon", 5);
SELECT * FROM people;

UPDATE people SET prenume="Eon", nume="Eonescu" WHERE id = 5;
SELECT * FROM people;

INSERT INTO people (prenume, nume)  
	VALUES ( "Ron", "Ronescu");
SELECT * FROM people;



INSERT INTO people SET
 prenume = "Pon", 
 id = 6 , 
 nume="Ponescu";   
SELECT * FROM people;
 
DROP TABLE people;

CREATE TABLE constrained_people(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nume VARCHAR(255) NOT NULL,
    prenume VARCHAR(255) CHECK (length(prenume) >= 2),
    cnp CHAR(13) UNIQUE,
    gen VARCHAR(255) DEFAULT "Secret"
);

SET SQL_SAFE_UPDATES = 1;
DELETE FROM constrained_people WHERE id >= 1;  #length(cnp) < 12;
SELECT * FROM constrained_people;

SELECT * FROM constrained_people WHERE length(cnp) < 12;

ALTER TABLE constrained_people ADD CONSTRAINT cnp CHECK (length(cnp) = 13);

INSERT INTO constrained_people SET
nume = "To-nescu",
prenume = "To",
cnp = "12345678901",
gen = "Barbat";
SELECT * FROM constrained_people;

INSERT INTO constrained_people
SET
nume = "Ionescu",
prenume = "Ion",
cnp = "1234567890124";
SELECT * FROM constrained_people;
SELECT COUNT(*) FROM constrained_people;
SELECT MAX(id) FROM constrained_people;


CREATE TABLE constrained_people_updated(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nume VARCHAR(255) NOT NULL,
    prenume VARCHAR(255) CHECK (length(prenume) >= 2),
    cnp CHAR(13) UNIQUE,
    gen VARCHAR(255) DEFAULT "Secret"
);


INSERT INTO constrained_people_updated ( nume, prenume,  gen) 
	SELECT  nume, prenume,  gen FROM constrained_people WHERE id = 5;
    
SELECT * FROM constrained_people_updated;
SELECT * FROM constrained_people;

