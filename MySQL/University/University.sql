SHOW DATABASES;

SELECT * FROM student;

INSERT INTO `student` (
	`idstudent`, `nume`, `prenume`, `gen`,
    `an`, `grupa`, `bursa`, `statut`)
    VALUES(3, "George", "Georgescu","m",
1, 1, 0, "admis");

SELECT * FROM student;

INSERT INTO student VALUES(2, "George", "Georgescu","m",
1, 1, 0, "admis");

INSERT INTO `student` (
	`idstudent`, `nume`, `prenume`, `gen`,
    `an`, `grupa`, `bursa`)
    VALUES(3, "Marius", "Manole","m",
1, 1, 0, "admis");

INSERT INTO student SET nume = "Radu", prenume = "Radulescu";
SELECT * FROM student;

INSERT INTO profesor SET prenume = 'Florin', nume = 'Piersic',
data_nasterii = '1936-01-01', grad = 'III';

SELECT * FROM profesor;

UPDATE profesor SET adresa = 'Teatru National I.L.Caragiale'
WHERE idprofesor = 1;

SELECT * FROM profesor;

SELECT * FROM student;

SELECT * FROM student WHERE idstudent = 4;

SELECT * FROM student WHERE prenume = 'Radulescu' AND nume = 'Radu';

INSERT INTO profesor (prenume, nume) select nume, prenume from student WHERE idstudent = 4;
SELECT * FROM profesor;


INSERT INTO curs SET idcurs = 3, titlu = 'MySQL3', an = 3, semestru = 2, credite = 15
ON DUPLICATE KEY UPDATE titlu = 'MySQL2';
SELECT * FROM curs;

SELECT * FROM student;

UPDATE student SET gen = "other" WHERE idstudent = 1;

INSERT INTO student SET gen = "other", idstudent = 5
ON DUPLICATE KEY UPDATE gen = 'other';

INSERT INTO student SET idstudent = 6, nume = "Stanica", prenume = "Jon",
gen = "m", an = 3, grupa = 2, bursa = 0, statut = "admis";

SELECT * FROM curs;

INSERT INTO curs SET titlu = "OOP", an = 2, semestru = 1, credite = 6;

SELECT * FROM profesor;

INSERT INTO predare SET idprofesor = 1, idcurs = 1, profesor_idprofesor = 1, curs_idcurs = 1;
SELECT * FROM predare;

SELECT * FROM note;

INSERT INTO note SET idnote = 1, valoare = 10, date_notare = '2024-03-07',
student_idstudent = 1, curs_idcurs = 1;

UPDATE student SET bursa = 400, statut = 'bursier' WHERE idstudent >=4;
SELECT * FROM student;

UPDATE student SET bursa = 300, statut = 'bursier' WHERE idstudent >=4;








