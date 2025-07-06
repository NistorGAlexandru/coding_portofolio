
DROP DATABASE IF EXISTS `curs5`;
CREATE DATABASE IF NOT EXISTS `curs5`;
USE `curs5`;

-- -----------------------------------------------------
-- Table `curs5`.`Profesor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `curs5`.`Profesor` (
  `idProfesor` INT NOT NULL AUTO_INCREMENT,
  `nume` VARCHAR(45) NULL,
  `prenume` VARCHAR(45) NULL,
  `adresa` VARCHAR(255) NULL,
  `data_nasterii` DATE NULL,
  `grad` ENUM('I', 'II', 'III') NULL,
  PRIMARY KEY (`idProfesor`));

-- -----------------------------------------------------
-- Table `curs5`.`Student`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `curs5`.`Student` (
  `idStudent` INT NOT NULL AUTO_INCREMENT,
  `nume` VARCHAR(45) NULL,
  `prenume` VARCHAR(45) NULL,
  `data_nasterii` DATETIME,
  `gen` CHAR(1) NULL,
  `an` INT NULL,
  `grupa` VARCHAR(45) NULL,
  `bursa` INT NULL,
  `status` ENUM('admis', 'restantier', 'bursier') NULL,
  PRIMARY KEY (`idStudent`));


-- -----------------------------------------------------
-- Table `curs5`.`Curs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `curs5`.`Curs` (
  `idCurs` INT NOT NULL AUTO_INCREMENT,
  `titlu` VARCHAR(45) NULL,
  `an` INT NULL,
  `semestru` INT NULL,
  `credit` INT NULL,
  PRIMARY KEY (`idCurs`));


-- -----------------------------------------------------
-- Table `curs5`.`Predare`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `curs5`.`Predare` (
  `idProfesor` INT NULL,
  `idCurs` INT NULL,
  INDEX `fk_id_profesor_idx` (`idProfesor` ASC) VISIBLE,
  INDEX `fk_id_curs_idx` (`idCurs` ASC) VISIBLE,
  CONSTRAINT `fk_id_profesor`
    FOREIGN KEY (`idProfesor`)
    REFERENCES `curs5`.`Profesor` (`idProfesor`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_id_curs`
    FOREIGN KEY (`idCurs`)
    REFERENCES `curs5`.`Curs` (`idCurs`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);


-- -----------------------------------------------------
-- Table `curs5`.`Note`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `curs5`.`Note` (
  `idNote` INT NOT NULL AUTO_INCREMENT,
  `idstudent` INT NULL,
  `idcurs` INT NULL,
  `valoare` INT NULL,
  `data_notare` DATETIME NULL DEFAULT current_timestamp,
  PRIMARY KEY (`idNote`),
  INDEX `fk_student_idx` (`idstudent` ASC) VISIBLE,
  INDEX `fk_curs_idx` (`idcurs` ASC) VISIBLE,
  CONSTRAINT `fk_student`
    FOREIGN KEY (`idstudent`)
    REFERENCES `curs5`.`Student` (`idStudent`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_curs`
    FOREIGN KEY (`idcurs`)
    REFERENCES `curs5`.`Curs` (`idCurs`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

SELECT * FROM curs;

USE curs5;



INSERT INTO `curs` VALUES (11,'HTML',2,1,5),(12,'Informatica',1,2,4),(13,'PHP',2,2,5),(14,'MySQL',2,1,8),(15,'JavaScript',2,2,5),(16,'Tehnologii Web2',3,2,10),(17,'Design',1,1,5),(18,'Android',3,1,6),(19,'PHP OOP',3,2,10),(21,'Logica',1,1,5),(22,'Matematica',1,1,4),(23,'OOP',1,2,7),(24,'BD',2,1,8),(25,'Java',2,2,10),(26,'Tehnologii Web',2,2,5),(27,'Sec. Info.',3,1,5),(28,'Python',3,1,6),(29,'Limbaje formale',2,1,5);


--
-- Dumping data for table `note`
--





--
-- Dumping data for table `profesor`
--




INSERT INTO `profesor` VALUES (1,'Dida','Nelson',NULL,'1965-05-05','I'),(2,'Massimo','Oddo',NULL,'1979-05-22','II'),(3,'Maldini','Paolo',NULL,'1973-08-25','III'),(4,'Nesta','Alessandro',NULL,'1969-10-02','III'),(5,'Jankulovski','Marek',NULL,'1967-06-28','I'),(6,'Ambrosini','Massimo',NULL,'1967-11-11','II'),(7,'Kaka','Ricardo',NULL,'1976-07-07','III'),(8,'Gatusso','Genaro',NULL,'1978-08-28','I'),(9,'Inzaghi','Filippo',NULL,'1963-05-31','III'),(10,'Seedorf','Clarence',NULL,'1960-10-07','III'),(11,'Pirlo','Andrea',NULL,'1973-04-08','II'),(12,'Dida','Nelson',NULL,'1973-10-07','II'),(13,'Schevchenko','Andriy',NULL,'1980-08-08','III'),(14,'Gilardino','Alberto',NULL,'1971-01-10','II'),(16,'Costacurta','Rui',NULL,'1980-08-08','III');

SELECT * FROM profesor;

--
-- Dumping data for table `student`
--


INSERT INTO `student` VALUES (100,'Maignan','Mike','1994-08-03','m',3,1,250,'admis'),(101,'Hernandez','Theo','1994-05-09','f',3,2,NULL,'admis'),(102,'Pobega','Tommaso','1994-03-15','m',3,3,350,'admis'),(103,'Kjaer','Simon','1993-09-11','f',3,1,NULL,'admis'),(104,'Terracciano','Filippo','1992-03-15','f',3,2,NULL,'admis'),(105,'Chukwueze','Samuel','1992-12-18','f',3,3,NULL,'admis'),(106,'Tamas','George','1993-07-15','m',3,1,350,'admis'),(107,'Loftus Cheek','Ruben','1994-09-21','f',3,2,NULL,'admis'),(108,'Camarda','Francesco','1993-12-18','f',3,3,NULL,'admis'),(109,'Jovic','Luka','1993-07-25','m',3,1,350,'admis'),(110,'Gabbia','Matteo','1995-08-03','m',2,1,250,'admis'),(111,'Jimenez','Alejandro','1995-05-09','m',2,2,NULL,'admis'),(112,'Corbu','Ion','1995-03-15','m',2,3,350,'admis'),(113,'Tataru','Andreea','1994-09-21','f',2,1,NULL,'admis'),(114,'Simic','Andreea','1996-03-15','f',2,2,NULL,'admis'),(115,'Florenzi','Alessandro','1993-12-28','f',2,3,NULL,'admis'),(116,'Tanase','George','1994-07-15','m',2,1,350,'admis'),(117,'Thiaw','Malik','1995-09-11','f',2,2,NULL,'admis'),(118,'Kalulu','Pierre','1995-12-28','f',2,3,NULL,'admis'),(119,'Bennacer','Ismael','1996-07-15','m',2,1,350,'admis'),(120,'Giroud','Olivier','1997-08-03','m',1,1,250,'admis'),(121,'Okafor','Noah','1996-05-09','f',1,2,NULL,'admis'),(122,'Pioli','Stefano','1997-03-15','m',1,3,350,'admis'),(123,'Pulisic','Christian','1996-09-21','f',1,1,NULL,'admis'),(124,'Leao','Rafael','2000-03-15','f',1,2,NULL,'admis'),(125,'Adli','Yacine','1997-12-28','f',1,3,NULL,'admis'),(126,'Reijnders','Tiijani','1997-07-15','m',1,1,350,'admis'),(127,'Musah','Yunus','1997-09-11','f',1,2,NULL,'admis');
SELECT * FROM student;


INSERT INTO `note` VALUES (1,111,21,8,'2023-10-10'),(2,111,22,9,'2023-03-07'),(3,111,23,10,'2023-12-20'),(4,111,24,9,'2023-12-31'),(5,111,25,7,'2023-11-13'),(6,111,26,8,'2023-01-14'),(7,112,21,7,'2023-11-24'),(8,112,22,6,'2023-01-28'),(9,112,23,5,'2023-12-30'),(10,112,24,6,'2023-12-26'),(11,112,25,7,'2023-03-04'),(12,112,26,4,'2023-03-22'),(13,113,21,9,'2023-11-28'),(14,113,22,9,'2023-01-13'),(15,113,23,7,'2023-03-23'),(16,113,24,10,'2023-11-13'),(17,113,25,4,'2023-10-26'),(18,113,26,7,'2023-03-09'),(19,114,21,6,'2023-11-11'),(20,114,22,9,'2023-11-29'),(21,114,23,10,'2023-03-18'),(22,114,24,4,'2023-03-01'),(23,114,25,5,'2023-12-21'),(24,114,26,4,'2023-01-21'),(25,115,21,10,'2023-02-21'),(26,115,22,7,'2023-11-06'),(27,115,23,10,'2023-12-24'),(28,115,24,10,'2023-02-18'),(29,115,25,8,'2023-01-13'),(30,115,26,9,'2023-01-02'),(31,116,21,10,'2023-02-28'),(32,116,22,10,'2023-02-06'),(33,116,23,9,'2023-10-16'),(34,117,21,7,'2023-10-24'),(35,117,22,6,'2023-12-03'),(36,117,23,4,'2023-12-14'),(37,118,21,7,'2023-10-09'),(38,118,22,7,'2023-02-26'),(39,118,23,7,'2023-11-07'),(40,119,21,7,'2023-12-12'),(41,119,22,8,'2023-12-17'),(42,119,23,9,'2023-03-12'),(43,101,21,8,'2023-10-10'),(44,105,21,10,'2023-02-21'),(45,108,21,7,'2023-10-09'),(46,107,21,7,'2023-10-24'),(47,124,21,6,'2023-11-11'),(48,126,21,10,'2023-02-28'),(49,103,21,9,'2023-11-28'),(50,109,21,7,'2023-12-12'),(51,102,21,7,'2023-11-24'),(52,103,22,9,'2023-01-13'),(53,105,22,7,'2023-11-06'),(54,101,22,9,'2023-03-07'),(55,124,22,9,'2023-11-29'),(56,109,22,8,'2023-12-17'),(57,107,22,6,'2023-12-03'),(58,102,22,6,'2023-01-28'),(59,126,22,10,'2023-02-06'),(60,108,22,7,'2023-02-26'),(61,107,23,4,'2023-12-14'),(62,108,23,7,'2023-11-07'),(63,101,23,10,'2023-12-20'),(64,126,23,9,'2023-10-16'),(65,109,23,9,'2023-03-12'),(66,124,23,10,'2023-03-18'),(67,103,23,7,'2023-03-23'),(68,105,23,10,'2023-12-24'),(69,102,23,5,'2023-12-30'),(70,105,24,10,'2023-02-18'),(71,101,24,9,'2023-12-31'),(72,102,24,6,'2023-12-26'),(73,103,24,10,'2023-11-13'),(74,124,24,4,'2023-03-01'),(75,124,25,5,'2023-12-21'),(76,101,25,7,'2023-11-13'),(77,105,25,8,'2023-01-13'),(78,102,25,7,'2023-03-04'),(79,103,25,4,'2023-10-26'),(80,103,26,7,'2023-03-09'),(81,101,26,8,'2023-01-14'),(82,105,26,9,'2023-01-02'),(83,124,26,4,'2023-01-21'),(84,102,26,4,'2023-03-22');

SELECT * FROM note;


INSERT INTO `predare` VALUES (10,11),(9,12),(11,13),(6,14),(11,19),(1,21),(9,21),(5,22),(3,23),(6,24),(7,24),(8,25),(2,26),(4,27),(7,28),(8,29);

SELECT * FROM predare;
