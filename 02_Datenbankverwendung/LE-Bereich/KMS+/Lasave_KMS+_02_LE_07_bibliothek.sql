-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: bibliothek
-- ------------------------------------------------------
-- Server version	8.0.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ausleihe`
--

DROP TABLE IF EXISTS `ausleihe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ausleihe` (
  `ausleiheID` int NOT NULL,
  `exemplarID` int NOT NULL,
  `von` date DEFAULT NULL,
  `bis` date DEFAULT NULL,
  `isbn` varchar(20) DEFAULT NULL,
  `titel` varchar(200) DEFAULT NULL,
  `fachbuchID` int DEFAULT NULL,
  PRIMARY KEY (`ausleiheID`,`exemplarID`),
  KEY `fachbuchID` (`fachbuchID`),
  CONSTRAINT `ausleihe_ibfk_1` FOREIGN KEY (`fachbuchID`) REFERENCES `fachbuch` (`fachbuchID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ausleihe`
--

LOCK TABLES `ausleihe` WRITE;
/*!40000 ALTER TABLE `ausleihe` DISABLE KEYS */;
INSERT INTO `ausleihe` VALUES (1,1,'2024-03-01','2024-03-10','978-3-540-11111-1','Einführung in die Gentechnik',1),(2,1,'2024-03-05','2024-03-18','978-3-540-33333-3','Mikrobiologische Verfahren',3),(3,1,'2024-03-07','2024-03-20','978-3-540-44444-4','Bioreaktoren und Fermentation',4);
/*!40000 ALTER TABLE `ausleihe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fachbereich`
--

DROP TABLE IF EXISTS `fachbereich`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fachbereich` (
  `fachbereichID` int NOT NULL,
  `fachbereich` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`fachbereichID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fachbereich`
--

LOCK TABLES `fachbereich` WRITE;
/*!40000 ALTER TABLE `fachbereich` DISABLE KEYS */;
INSERT INTO `fachbereich` VALUES (1,'Gentechnik'),(2,'Mikrobiologie'),(3,'Zellbiologie'),(4,'Biochemie');
/*!40000 ALTER TABLE `fachbereich` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fachbereichfachbuch`
--

DROP TABLE IF EXISTS `fachbereichfachbuch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fachbereichfachbuch` (
  `fachbereichID` int DEFAULT NULL,
  `fachbuchID` int DEFAULT NULL,
  KEY `fachbereichID` (`fachbereichID`),
  KEY `fachbuchID` (`fachbuchID`),
  CONSTRAINT `fachbereichfachbuch_ibfk_1` FOREIGN KEY (`fachbereichID`) REFERENCES `fachbereich` (`fachbereichID`),
  CONSTRAINT `fachbereichfachbuch_ibfk_2` FOREIGN KEY (`fachbuchID`) REFERENCES `fachbuch` (`fachbuchID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fachbereichfachbuch`
--

LOCK TABLES `fachbereichfachbuch` WRITE;
/*!40000 ALTER TABLE `fachbereichfachbuch` DISABLE KEYS */;
INSERT INTO `fachbereichfachbuch` VALUES (1,1),(3,2),(2,3),(4,4),(2,4);
/*!40000 ALTER TABLE `fachbereichfachbuch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fachbuch`
--

DROP TABLE IF EXISTS `fachbuch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fachbuch` (
  `fachbuchID` int NOT NULL,
  `isbn` varchar(20) DEFAULT NULL,
  `titel` varchar(200) DEFAULT NULL,
  `verlagID` int DEFAULT NULL,
  PRIMARY KEY (`fachbuchID`),
  KEY `verlagID` (`verlagID`),
  CONSTRAINT `fachbuch_ibfk_1` FOREIGN KEY (`verlagID`) REFERENCES `verlag` (`verlagID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fachbuch`
--

LOCK TABLES `fachbuch` WRITE;
/*!40000 ALTER TABLE `fachbuch` DISABLE KEYS */;
INSERT INTO `fachbuch` VALUES (1,'978-3-540-11111-1','Einführung in die Gentechnik',1),(2,'978-3-540-22222-2','Molekulare Zellbiologie',2),(3,'978-3-540-33333-3','Mikrobiologische Verfahren',3),(4,'978-3-540-44444-4','Bioreaktoren und Fermentation',1);
/*!40000 ALTER TABLE `fachbuch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `verlag`
--

DROP TABLE IF EXISTS `verlag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `verlag` (
  `verlagID` int NOT NULL,
  `verlag` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`verlagID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `verlag`
--

LOCK TABLES `verlag` WRITE;
/*!40000 ALTER TABLE `verlag` DISABLE KEYS */;
INSERT INTO `verlag` VALUES (1,'Wissenschaftsverlag BioTech'),(2,'Genoma Press'),(3,'MolekularMedien GmbH'),(4,'Biotech Future Verlag');
/*!40000 ALTER TABLE `verlag` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-30  0:20:52
