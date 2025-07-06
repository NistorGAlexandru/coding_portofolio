USE CURS7_magazin;

-- Care este prețul maxim al articolelor din comanda numărul 3 ? 
SELECT * FROM comanda;
SELECT * FROM comanda_articol;
SELECT * FROM articol WHERE id = 8 OR id = 5;
SELECT MAX(pret) FROM articol WHERE id = 8 OR id = 5;
SELECT MAX(pret) AS 'Pretul maxim al articolelor din comanda 3' FROM articol WHERE id = 8 OR id = 5;

SELECT * FROM comanda_articol JOIN articol
ON comanda_articol.articol_id = articol. id WHERE comanda_articol.comanda_id = 3;

SELECT MAX(pret) FROM comanda_articol JOIN articol
ON comanda_articol.articol_id = articol.id WHERE comanda_articol.comanda_id = 3;

-- Câte articole au cel mai mare preț ? 
SELECT * FROM articol;
SELECT MAX(pret) FROM articol;

SELECT COUNT(pret), pret FROM articol GROUP BY pret ORDER BY pret DESC LIMIT 1;

SELECT COUNT(pret) AS 'Cate articole au pretul cel mai mare'
	FROM articol GROUP BY pret ORDER BY pret DESC LIMIT 1;
    
SELECT MAX(pret) FROM articol;
SELECT COUNT(*) FROM articol WHERE pret = 9.5;
SELECT COUNT(*) FROM articol WHERE pret = (SELECT MAX(pret) FROM articol);
SELECT COUNT(*) AS 'Cate articole au pretul cel mai mare'
	FROM articol WHERE pret = (SELECT MAX(pret) FROM articol);
    
-- Dar cel mai mic pret ? 
SELECT COUNT(pret) AS 'Cate articole au pretul cel mai mic'
	FROM articol GROUP BY pret ORDER BY pret ASC LIMIT 1;

SELECT COUNT(*) AS 'Cate articole au pretul cel mai mic'
	FROM articol WHERE pret = (SELECT MIN(pret) FROM articol);

SELECT MIN(pret) FROM articol;
SELECT * FROM articol;

--  Care este diferența între cel mai mare și mai mic pret (in bani) ? 
SET @minim = (SELECT MIN(pret) FROM articol);
SET @maxim = (SELECT MAX(pret) FROM articol);

SELECT (@maxim - @minim) AS 'diferența între cel mai mare și mai mic pret';

SELECT MAX(pret) - MIN(pret) FROM articol;
SELECT MAX(pret) - MIN(pret) AS 'diferența între cel mai mare și mai mic pret' FROM articol;

--  Care este inițiala clientului cu ultimul nume, în ordine alfabetica ? 
SELECT * FROM client;
SELECT * FROM client ORDER BY denumire;


SELECT * FROM client ORDER BY denumire DESC LIMIT 1;
SELECT MAX(denumire) FROM client;

SELECT SUBSTRING(MAX(denumire), 1, 1) 
	AS 'Initiala clientului cu ultimul nume alfabetic' FROM client;

SELECT @nume := (SELECT denumire FROM client ORDER BY denumire DESC LIMIT 1);
SELECT @nume;

SELECT SUBSTRING(@nume, 1, 1) 
	AS 'Initiala clientului cu ultimul nume alfabetic';

--  Care este suma prețurilor articolelor ? 
SELECT * FROM articol;
SELECT SUM(pret) FROM articol;

--  Care este prețul total al comenzii cu numărul 3 ? 
SELECT * FROM comanda_articol;
SELECT * FROM comanda_articol JOIN articol
		   ON comanda_articol.articol_id = articol.id;
           
SELECT SUM(pret) FROM comanda_articol JOIN articol
		   ON comanda_articol.articol_id = articol.id WHERE comanda_id = 3;

SELECT SUM(pret * cantitate) AS 'Prețul total al comenzii cu numărul 3' FROM comanda_articol JOIN articol
		   ON comanda_articol.articol_id = articol.id WHERE comanda_id = 3;
           
--  Calculați pretul mediu al articolelor.
SELECT AVG(pret) AS 'Pret mediu' FROM articol;
SELECT SUM(pret) / COUNT(pret) AS 'Pret mediu' FROM articol;

--  Calculati pretul mediu al articolelor, neponderat.
SELECT AVG(DISTINCT pret) AS 'Pret mediu' FROM articol;
SELECT DISTINCT AVG( pret) AS 'Pret mediu' FROM articol;

--  Calculați pretul mediu al comenzilor.
SELECT * FROM articol JOIN comanda_articol
		   ON articol.id = comanda_articol.articol_id;
           
SELECT comanda_articol.comanda_id, pret * cantitate AS 'Pret per comanda' FROM articol JOIN comanda_articol
		   ON articol.id = comanda_articol.articol_id;

SELECT SUM(pret * cantitate) AS 'Pret per comanda' FROM articol JOIN comanda_articol
		   ON articol.id = comanda_articol.articol_id
           GROUP BY comanda_articol.comanda_id;

SELECT AVG(pret * cantitate) AS 'Pret per comanda' FROM articol JOIN comanda_articol
		   ON articol.id = comanda_articol.articol_id;


--  Calculati pretul mediu al comenzilor, neponderat. 
SELECT AVG(pret ) AS 'Pret per comanda' FROM articol JOIN comanda_articol
		   ON articol.id = comanda_articol.articol_id;
           
-- View

CREATE VIEW  comanda_articol_view AS
  SELECT articol.id, descriere, pret, comanda_id, articol_id, cantitate FROM articol JOIN comanda_articol
		   ON articol.id = comanda_articol.articol_id;
           
SELECT * FROM comanda_articol_view;

CREATE VIEW  pret_cantitate_view AS
  SELECT  pret,  cantitate FROM articol JOIN comanda_articol
		   ON articol.id = comanda_articol.articol_id;
SELECT * FROM pret_cantitate_view;


SELECT MAX(pret) FROM pret_cantitate_view;

SELECT AVG(pret * cantitate) FROM pret_cantitate_view;

DROP VIEW pret_cantitate_view;


CREATE VIEW articole_comenzi AS 
SELECT articol.id AS 'articol_id', descriere, pret, 
		comanda_articol.id AS 'comanda_articol_id', cantitate, data, client_id FROM articol JOIN comanda_articol 
		   ON articol.id = comanda_articol.articol_id
		 JOIN comanda 
           ON comanda_articol.comanda_id = comanda.id;

SELECT * FROM articole_comenzi;



