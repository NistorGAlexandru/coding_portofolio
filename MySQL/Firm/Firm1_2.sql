USE curs6_firma;
-- 2. Listați numele angajaților
SELECT * FROM angajat;
SELECT nume, prenume FROM angajat;
SELECT CONCAT(nume, prenume) FROM angajat;
SELECT CONCAT(nume,  " " , prenume) AS "Nume Angajat" FROM angajat;

-- 3. Listați numele angajaților, ordonate crescător 
SELECT CONCAT(nume,  " " , prenume) AS "Nume Angajat" FROM angajat ORDER BY nume;
SELECT CONCAT(nume,  " " , prenume) AS "Nume Angajat" 
	FROM angajat ORDER BY nume, prenume;

-- 4. Selectați numele angajaților, ordonate descrescător
SELECT CONCAT(nume,  " " , prenume) AS "Nume Angajat" 
	FROM angajat ORDER BY nume DESC, prenume DESC;
SELECT CONCAT(prenume,  " " , nume) AS "Nume Angajat" 
	FROM angajat ORDER BY prenume DESC, nume DESC;

-- 5.Selectați numele angajaților: DESC după departament_id, ASC după salariu;
 SELECT * FROM angajat ORDER BY departament_id DESC, salariu;
 
 
-- 6. Selectați numele angajatilor care lucreaza la HR 
SELECT id FROM departament WHERE nume = "HR";
SELECT * FROM angajat WHERE departament_id = 5;

SET @dep_id = 5;
SELECT @dep_id;

SET @dep_id = (SELECT id FROM departament WHERE nume LIKE "%end");
SELECT * FROM angajat WHERE departament_id = @dep_id;

SELECT * FROM departament;

SELECT * FROM angajat JOIN departament 
	ON departament.id = angajat.departament_id;
SELECT * FROM angajat;
SELECT * FROM departament;

SELECT * FROM angajat JOIN departament 
	ON departament.id = angajat.departament_id  WHERE departament.nume = "HR";

SELECT * FROM departament JOIN angajat 
	ON departament.id = angajat.departament_id;

SELECT * FROM departament JOIN angajat 
	ON departament.id = angajat.departament_id WHERE departament.nume = "HR";

SELECT angajat.nume, angajat.prenume FROM angajat JOIN departament 
	ON departament.id = angajat.departament_id  WHERE departament.nume = "HR";

-- 7. Listati angajatii care nu lucreaza la HR 
SELECT angajat.nume, angajat.prenume FROM angajat JOIN departament 
	ON departament.id = angajat.departament_id  WHERE departament.nume != "HR";

SELECT COUNT(*) FROM angajat JOIN departament 
	ON departament.id = angajat.departament_id  WHERE departament.nume != "HR";

SELECT angajat.nume, angajat.prenume FROM angajat JOIN departament 
	ON departament.id = angajat.departament_id  WHERE departament.nume <> "HR";


-- 8. Listati angajatii care au salariu mai mare de 3000 lei
SELECT * FROM angajat WHERE salariu > 3000;

-- 8.1 Toate numele de departament care au salarii mai mari de 3000
SELECT DISTINCT departament.nume FROM angajat JOIN departament 
ON angajat.departament_id  = departament.id WHERE angajat.salariu > 3000;

-- 8.2 SERGIU: cati bani per departament
SELECT SUM(salariu) AS 'Suma totala salarii' FROM angajat;
SELECT  SUM(salariu) AS 'Suma totala salarii' FROM angajat GROUP BY departament_id;

SELECT departament_id, SUM(salariu) AS 'Suma totala salarii' FROM angajat GROUP BY departament_id;

SELECT departament.nume, SUM(salariu) AS 'Suma totala salarii' FROM angajat JOIN departament 
ON angajat.departament_id  = departament.id  GROUP BY angajat.departament_id;

-- 8.2 SERGIU: cati bani per departament, cu numele de departament specificat si salariul peste 3000 
SELECT departament.nume, SUM(salariu) AS 'Suma totala salarii' FROM angajat JOIN departament 
ON angajat.departament_id  = departament.id  WHERE angajat.salariu > 3000
GROUP BY angajat.departament_id ;


-- 9. Selectati angajatii care au salariul 3000 lei
SELECT * FROM angajat WHERE salariu = 3000;


-- 10. Selectați angajații care au salariul intre 3000 si 5000 de lei
SELECT * FROM angajat WHERE salariu > 3000 AND salariu < 5000;

-- 11 Selectați angajații care nu au manager 
SELECT * FROM angajat WHERE manager_id IS NOT NULL;

SELECT COUNT(*) FROM angajat WHERE manager_id IS NOT NULL;

-- 12. Listați angajații ai caror manager are ID-ul 1

SELECT * FROM angajat WHERE manager_id = 1;

-- 13. Enumerați angajații ai căror manager este Toma Ion 
SELECT COUNT(*) FROM angajat AS salariat INNER JOIN angajat AS manager  
		  ON manager.id = salariat.manager_id;
          
SELECT * FROM angajat AS salariat LEFT JOIN angajat AS manager  
		  ON manager.id = salariat.manager_id;
          
SELECT * FROM angajat AS manager    RIGHT JOIN angajat AS salariat
		  ON manager.id = salariat.manager_id;          


SELECT * FROM angajat AS salariat RIGHT JOIN angajat AS manager  
		  ON manager.id = salariat.manager_id;
          
SELECT COUNT(*) FROM angajat AS salariat RIGHT JOIN angajat AS manager  
		  ON manager.id = salariat.manager_id;

SELECT * FROM angajat AS salariat JOIN angajat AS manager  
		  ON manager.id = salariat.manager_id;

SELECT * FROM angajat AS manager JOIN angajat AS salariat
		  ON manager.id = salariat.manager_id;
          
-- 14. Listati angajații care au salariu mai mare de 2500 lei 
-- si lucrează pe Backend 
SELECT * FROM angajat JOIN departament 
	ON departament.id = angajat.departament_id
WHERE angajat.salariu > 2500 AND departament.nume = "Backend";

SELECT COUNT(*) FROM angajat;
-- 15. Selectati angajatii ai căror manager NU este Toma Ion
-- și care au salariu mai mare de 4000 lei 
SELECT * FROM angajat;
SELECT COUNT(manager_id) FROM angajat;
SELECT COUNT(DISTINCT departament_id) FROM angajat;
SELECT DISTINCT departament_id FROM angajat;
SELECT DISTINCT COUNT( departament_id) FROM angajat;

SELECT COUNT(*) FROM angajat as salariat 
		 JOIN angajat AS manager
         ON manager.id = salariat.manager_id
         WHERE manager.nume <> "Toma" OR manager.prenume <> "Ion";
        
SELECT COUNT(*) FROM angajat as salariat 
		LEFT JOIN angajat AS manager
         ON manager.id = salariat.manager_id
         WHERE (manager.nume <> "Toma" OR manager.prenume <> "Ion") 
         OR salariat.manager_id IS NULL;
        

SELECT * FROM angajat WHERE manager_id <> 1 OR manager_id IS  NULL;

SELECT * FROM angajat WHERE  (nume <> "Toma" OR prenume <> "Ion") ;

SELECT * FROM angajat as salariat 
		LEFT JOIN angajat AS manager
         ON manager.id = salariat.manager_id
         WHERE ((manager.nume <> "Toma" OR manager.prenume <> "Ion") 
         OR salariat.manager_id IS NULL) AND salariat.salariu > 4000;
         
-- Cati subalterni sunt sub fiecare manager
SELECT * FROM angajat;

SELECT COUNT(*) , manager_id FROM angajat GROUP BY manager_id;

SELECT COUNT(*) , manager.nume FROM angajat as salariat 
		JOIN angajat AS manager
         ON manager.id = salariat.manager_id GROUP BY salariat.manager_id;
         
SELECT COUNT(*), manager.nume FROM angajat as salariat 
		JOIN angajat AS manager
         ON manager.id = salariat.manager_id GROUP BY salariat.manager_id;