USE curs5;

SELECT * FROM student;
SELECT * FROM profesor;

SELECT * FROM student;
SELECT * FROM student WHERE an = 3 AND grupa = 1;

SELECT * FROM student ORDER By nume;
SELECT * FROM student ORDER By data_nasterii;
SELECT bursa, nume, prenume, idStudent, status, gen, an, grupa FROM student 
	WHERE bursa IS NOT NULL 
    ORDER By bursa, nume 
    LIMIT 5;
SELECT COUNT(*) AS 'Numar burse', bursa FROM student GROUP BY bursa;
SELECT COUNT(*) AS 'Persoane per an', an FROM student GROUP BY an;

SELECT COUNT(*), nume AS 'Nume' FROM student GROUP BY nume;

SELECT nume AS 'Nume' FROM student GROUP BY nume;

SELECT nume FROM student WHERE nume LIKE 'C%'; 


SELECT COUNT(gen), gen AS 'Nume' FROM student GROUP BY gen;

SELECT COUNT(gen), gen AS 'Nume' FROM student GROUP BY gen HAVING gen='m';

SELECT COUNT(gen), gen AS 'Nume' FROM student WHERE gen='m';


SELECT COUNT(*) AS 'Numar profesori' FROM profesor;

SELECT COUNT(*) AS Numar_profesori FROM profesor;
SELECT COUNT(*)  Numar_profesori FROM profesor;

SELECT nume AS prenume FROM profesor;
SELECT nume, prenume FROM profesor;

SELECT CONCAT(nume, ' ', prenume) AS 'Full name' FROM profesor;

SELECT * FROM profesor;

SELECT CONCAT(nume, ' ', prenume, ' ', data_nasterii) AS 'Full name' FROM profesor;

SELECT NOW();
SELECT CURDATE();
SELECT VERSION() ;

SELECT NOW(), CURDATE(), VERSION() ;
SELECT NOW() AS 'ACUM', CURDATE() AS 'AZI', VERSION()  AS 'VERSIUNE' ;

SELECT titlu FROM curs;
SELECT titlu FROM curs ORDER BY titlu;

SELECT nume, prenume, status FROM student;

-- restantier Pioli
SELECT idStudent FROM student WHERE nume = 'Pioli';

UPDATE student SET status = 'restantier' WHERE idStudent = 122;
 
SELECT nume, prenume, status FROM student WHERE status = 'admis';

SELECT nume, prenume, an FROM student WHERE an = 1 or an = 2;
SELECT nume, prenume, an FROM student WHERE an IN (1, 2, 3);

SELECT SUM(bursa) FROM student WHERE an = 1;
SELECT SUM(bursa) AS 'Suma burselor din anul 1' FROM student WHERE an = 1;
SELECT SUM(bursa) AS 'Suma burselor din anul', an FROM student GROUP BY an;


SET @suma_burse_an1 = (SELECT SUM(bursa) AS 'Suma burselor din anul 1' FROM student WHERE an = 1);
SET @suma_burse_an2 = (SELECT SUM(bursa) AS 'Suma burselor din anul 2' FROM student WHERE an = 2);
SET @suma_burse_an3 = (SELECT SUM(bursa) AS 'Suma burselor din anul 3' FROM student WHERE an = 3);

SET @suma_1 = 1;
SELECT @suma_burse_an1 AS 'Suma burselor din anul 1',
	   @suma_burse_an2 AS 'Suma burselor din anul 2', 
	 @suma_burse_an3 AS 'Suma burselor din anul 3';

SELECT @o_variabila_care_nu_exista;


SET @@sql_safe_update = 0;


SET @variabila = 1;

SET @variabila := 2;
SELECT @variabila;

SELECT @variabila := 3;
SELECT @variabila;

SELECT @variabila = 3;
SELECT @variabila;

SET @jucator = 'Giroud';
-- jucatorului Pulisic ii punem bursa cu 100 mai mult decat maximul bursei 
SELECT @jucator;

SELECT * FROM student WHERE nume = @jucator;
SELECT idStudent FROM student WHERE nume = @jucator;
SET @id_jucator = (SELECT idStudent FROM student WHERE nume = @jucator);
SELECT @id_jucator;

SET @max_bursa = (SELECT MAX(bursa) FROM student);
SELECT @max_bursa;

UPDATE student SET bursa = (@max_bursa + 100) WHERE idStudent = @id_jucator;
SELECT * FROM student WHERE nume = @jucator;


SELECT nume AS "Nume Profesori" FROM profesor;

-- Studenților care au bursa să li se schimbe statusul în bursieri 

SELECT * FROM student;
SELECT idStudent FROM student WHERE bursa IS NOT NULL;

SET @@sql_safe_updates = 0;
UPDATE student SET status = "bursier" WHERE bursa IS NOT NULL;


SELECT * FROM student;

SET @antrenor = "Pioli";
-- bursa NULL si status restantier
SET @id_antrenor = (SELECT idStudent FROM student WHERE nume = @antrenor);
UPDATE student SET status = "restantier", bursa = NULL 
	WHERE idStudent = @id_antrenor;
SELECT * FROM student WHERE nume = @antrenor;

SELECT COUNT(*) AS 'Nr Total' FROM student;
SELECT an AS 'An',COUNT(*) AS 'Nr Total' FROM student GROUP BY an ORDER By an;


SELECT * FROM student;
SELECT data_nasterii FROM student;
SELECT * FROM student WHERE data_nasterii > '1996-01-01 00:00:00';

SELECT * FROM student WHERE data_nasterii > '1996-01-01';
SELECT * FROM student WHERE YEAR(data_nasterii) > 1995;
SELECT * FROM student WHERE YEAR(data_nasterii) > 1992;

SELECT * FROM profesor WHERE grad = 'I' or grad = 'II';
SELECT * FROM profesor WHERE grad < 3;

SELECT * FROM profesor WHERE grad = 1;

SELECT * FROM profesor WHERE grad != 3;

SELECT * FROM profesor WHERE grad <> 3;

SELECT * FROM profesor WHERE grad = 'I' || grad = 'II';

SELECT * FROM curs WHERE an = 2 AND semestru = 2;
SELECT COUNT(*) AS 'Nr cursuri per an', an FROM curs GROUP BY an;

SELECT * FROM student WHERE DATE_FORMAT(data_nasterii, '%m-%d') = '03-15';

SELECT * FROM student WHERE MONTH(data_nasterii) = 3 AND DAY(data_nasterii) = 15;

SELECT * FROM student WHERE bursa * 12 > 4000;