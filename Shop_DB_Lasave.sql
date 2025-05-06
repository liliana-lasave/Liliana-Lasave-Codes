-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: shop_db_lasave
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
-- Table structure for table `artikel`
--

DROP TABLE IF EXISTS `artikel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `artikel` (
  `artikel_id` int NOT NULL AUTO_INCREMENT,
  `bezeichnung` varchar(100) DEFAULT NULL,
  `beschreibung` text,
  `preis` decimal(10,2) DEFAULT NULL,
  `lagerbestand` int DEFAULT NULL,
  `lieferanten_id` int DEFAULT NULL,
  PRIMARY KEY (`artikel_id`),
  KEY `fk_lieferant` (`lieferanten_id`),
  CONSTRAINT `fk_lieferant` FOREIGN KEY (`lieferanten_id`) REFERENCES `lieferanten` (`lieferanten_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artikel`
--

LOCK TABLES `artikel` WRITE;
/*!40000 ALTER TABLE `artikel` DISABLE KEYS */;
INSERT INTO `artikel` VALUES (1,'Mate','Set de mate de acero inoxidable',3500.00,49,1),(2,'Alfajores','Caja de 12 alfajores de dulce de leche',1500.00,100,2),(3,'Fernet','Botella de Fernet 750ml',2500.00,30,1),(4,'Dulce de leche','Pote de 400g',800.00,40,2);
/*!40000 ALTER TABLE `artikel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kunden`
--

DROP TABLE IF EXISTS `kunden`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `kunden` (
  `kunden_id` int NOT NULL AUTO_INCREMENT,
  `vorname` varchar(50) DEFAULT NULL,
  `nachname` varchar(50) DEFAULT NULL,
  `strasse` varchar(50) DEFAULT NULL,
  `hausnummer` varchar(10) DEFAULT NULL,
  `postleitzahl` varchar(10) DEFAULT NULL,
  `stadt` varchar(50) DEFAULT NULL,
  `telefonnummer` varchar(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`kunden_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kunden`
--

LOCK TABLES `kunden` WRITE;
/*!40000 ALTER TABLE `kunden` DISABLE KEYS */;
INSERT INTO `kunden` VALUES (1,'María','González','Avenida Santa Fe','1234','C1425','CABA','011-4321-1234','maria@gmail.com'),(2,'Juan','Pérez','Calle Córdoba','567','5000','Córdoba','0351-123-4567','juan@gmail.com');
/*!40000 ALTER TABLE `kunden` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `kundenverkaeufe`
--

DROP TABLE IF EXISTS `kundenverkaeufe`;
/*!50001 DROP VIEW IF EXISTS `kundenverkaeufe`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `kundenverkaeufe` AS SELECT 
 1 AS `vorname`,
 1 AS `nachname`,
 1 AS `bezeichnung`,
 1 AS `menge`,
 1 AS `datum`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `lieferanten`
--

DROP TABLE IF EXISTS `lieferanten`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lieferanten` (
  `lieferanten_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `strasse` varchar(50) DEFAULT NULL,
  `hausnummer` varchar(10) DEFAULT NULL,
  `postleitzahl` varchar(10) DEFAULT NULL,
  `stadt` varchar(50) DEFAULT NULL,
  `telefonnummer` varchar(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`lieferanten_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lieferanten`
--

LOCK TABLES `lieferanten` WRITE;
/*!40000 ALTER TABLE `lieferanten` DISABLE KEYS */;
INSERT INTO `lieferanten` VALUES (1,'Proveedor Norte','Ruta Nacional 9','km 123','4000','San Miguel de Tucumán','0381-456-7890','norte@proveedores.com'),(2,'Proveedor Sur','Avenida Colón','1500','7600','Mar del Plata','0223-654-3210','sur@proveedores.com');
/*!40000 ALTER TABLE `lieferanten` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `verkauf`
--

DROP TABLE IF EXISTS `verkauf`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `verkauf` (
  `verkauf_id` int NOT NULL AUTO_INCREMENT,
  `kunden_id` int DEFAULT NULL,
  `artikel_id` int DEFAULT NULL,
  `menge` int DEFAULT NULL,
  `datum` date DEFAULT NULL,
  PRIMARY KEY (`verkauf_id`),
  KEY `kunden_id` (`kunden_id`),
  KEY `artikel_id` (`artikel_id`),
  CONSTRAINT `verkauf_ibfk_1` FOREIGN KEY (`kunden_id`) REFERENCES `kunden` (`kunden_id`),
  CONSTRAINT `verkauf_ibfk_2` FOREIGN KEY (`artikel_id`) REFERENCES `artikel` (`artikel_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `verkauf`
--

LOCK TABLES `verkauf` WRITE;
/*!40000 ALTER TABLE `verkauf` DISABLE KEYS */;
INSERT INTO `verkauf` VALUES (1,1,1,2,'2024-05-10'),(2,2,2,1,'2024-05-11'),(3,1,3,1,'2024-05-12'),(4,1,1,1,'2025-05-06');
/*!40000 ALTER TABLE `verkauf` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `kundenverkaeufe`
--

/*!50001 DROP VIEW IF EXISTS `kundenverkaeufe`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `kundenverkaeufe` AS select `kunden`.`vorname` AS `vorname`,`kunden`.`nachname` AS `nachname`,`artikel`.`bezeichnung` AS `bezeichnung`,`verkauf`.`menge` AS `menge`,`verkauf`.`datum` AS `datum` from ((`verkauf` join `kunden` on((`verkauf`.`kunden_id` = `kunden`.`kunden_id`))) join `artikel` on((`verkauf`.`artikel_id` = `artikel`.`artikel_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-06  1:47:14
