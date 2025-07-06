
-- Construiți un VIEW care să listeze angajații din departamentul cu ID= 4 
-- si sa contina nume, prenume, salariu_annual
-- Utilizati acest VIEW
-- Adaugati inca 2 angajati, apoi utilizati VIEW-UL creat. 

USE curs7_firma;

SELECT CONCAT(nume,' ',prenume) AS 'Nume', 
	salariu * 12 AS salariu_anual FROM angajat 
    WHERE departament_id = 4;
    
CREATE VIEW salariati_salarii AS SELECT CONCAT(nume,' ',prenume) AS 'Nume', 
	salariu * 12 AS salariu_anual FROM angajat 
    WHERE departament_id = 4; 
    
SELECT * FROM salariati_salarii;

SELECT SUM(salariu_anual) FROM salariati_salarii;


SELECT *  FROM salariati_salarii ORDER BY nume;

INSERT INTO angajat SET nume = 'Mickey', 
	prenume='Mouse', salariu=3000, departament_id = 4;

INSERT INTO angajat SET nume = 'Donald', 
	prenume='Duck', salariu=4000, departament_id = 4;

SELECT *  FROM salariati_salarii ORDER BY nume;

CREATE VIEW angajat_departament AS 
SELECT CONCAT(angajat.nume,' ',angajat.prenume) AS 'Nume', 
	salariu * 12 AS salariu_anual, departament.nume AS 'departament' FROM angajat JOIN departament 
		ON angajat.departament_id = departament.id where departament_id = 4;    

SELECT * FROM angajat_departament;

-- Selectati angajatii ai căror manager NU este Toma Ion și care au salariu mai mare de 4000 lei 

CREATE VIEW not_toma AS
SELECT * FROM angajat WHERE (manager_id <> 1 OR manager_id IS NULL) 
	AND salariu > 4000;

SELECT * FROM not_toma;

CREATE VIEW  not_toma_2 AS
SELECT CONCAT(s.nume,' ', s.prenume) AS 'Nume', s.salariu FROM angajat AS s LEFT JOIN angajat AS m
		ON s.manager_id = m.id
        WHERE ( (m.nume <> "Toma" OR m.prenume <> 'Ion') OR s.manager_id IS NULL) 
	AND s.salariu > 4000;
SELECT * FROM not_toma_2;


