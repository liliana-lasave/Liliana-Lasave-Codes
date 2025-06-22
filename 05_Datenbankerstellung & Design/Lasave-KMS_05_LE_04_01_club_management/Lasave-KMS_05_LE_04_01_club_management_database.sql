-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: club_management
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
-- Table structure for table `education`
--

DROP TABLE IF EXISTS `education`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `education` (
  `education_id` int NOT NULL AUTO_INCREMENT,
  `education_name` varchar(100) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `duration_hours` decimal(5,2) DEFAULT NULL,
  `education_level` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`education_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `education`
--

LOCK TABLES `education` WRITE;
/*!40000 ALTER TABLE `education` DISABLE KEYS */;
INSERT INTO `education` VALUES (1,'Volleyball Coaching Basics','Introductory course on volleyball techniques and team management.',20.00,'Beginner'),(2,'Basketball Advanced Tactics','Advanced strategies for coaching competitive basketball teams.',35.00,'Advanced'),(3,'Futsal Coaching Certification','Comprehensive course on futsal rules, drills, and team dynamics.',30.00,'Intermediate'),(4,'Curling Team Leadership','Training focused on curling strategy and team coordination.',25.00,'Intermediate');
/*!40000 ALTER TABLE `education` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `places`
--

DROP TABLE IF EXISTS `places`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `places` (
  `place_id` int NOT NULL AUTO_INCREMENT,
  `place_name` varchar(100) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `place_description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`place_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `places`
--

LOCK TABLES `places` WRITE;
/*!40000 ALTER TABLE `places` DISABLE KEYS */;
INSERT INTO `places` VALUES (1,'Arena Norte','Calle Belgrano 1201','Indoor stadium for basketball games and training.'),(2,'Club Olímpico','Avenida Libertad 555','Multipurpose court used mainly for volleyball training.'),(3,'Polideportivo Sur','Calle San Martín 2300','Indoor futsal facility with locker rooms and stands.'),(4,'Centro de Curling Ártico','Ruta Provincial 9, Km 18','Ice rink facility for curling practice and events.');
/*!40000 ALTER TABLE `places` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `player_team`
--

DROP TABLE IF EXISTS `player_team`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `player_team` (
  `player_id` int NOT NULL,
  `team_id` int NOT NULL,
  `start_date` date DEFAULT NULL,
  PRIMARY KEY (`player_id`,`team_id`),
  KEY `fk_team_id_player_team_from_teams` (`team_id`),
  CONSTRAINT `fk_player_id_player_team_from_players` FOREIGN KEY (`player_id`) REFERENCES `players` (`player_id`),
  CONSTRAINT `fk_team_id_player_team_from_teams` FOREIGN KEY (`team_id`) REFERENCES `teams` (`team_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `player_team`
--

LOCK TABLES `player_team` WRITE;
/*!40000 ALTER TABLE `player_team` DISABLE KEYS */;
INSERT INTO `player_team` VALUES (1,1,'2023-09-10'),(1,12,'2024-03-01'),(2,1,'2023-10-12'),(2,11,'2024-03-12'),(3,2,'2023-11-01'),(3,13,'2024-03-15'),(4,2,'2023-11-15'),(4,12,'2024-03-18'),(5,3,'2024-01-05'),(5,13,'2024-04-01'),(6,3,'2024-01-06'),(6,14,'2024-04-10'),(7,4,'2024-02-01'),(7,14,'2024-04-05'),(8,4,'2024-02-02'),(9,5,'2023-12-10'),(9,11,'2024-02-05'),(10,6,'2024-01-20'),(11,7,'2023-10-30'),(12,8,'2023-09-25'),(13,9,'2023-08-14'),(14,10,'2024-03-03');
/*!40000 ALTER TABLE `player_team` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `players`
--

DROP TABLE IF EXISTS `players`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `players` (
  `player_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  PRIMARY KEY (`player_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `players`
--

LOCK TABLES `players` WRITE;
/*!40000 ALTER TABLE `players` DISABLE KEYS */;
INSERT INTO `players` VALUES (1,'Diego','Pérez'),(2,'Andrés','Jiménez'),(3,'Luis','Ortega'),(4,'Paula','Ruiz'),(5,'Valentina','Ramírez'),(6,'Lucía','Gómez'),(7,'Fernando','Castro'),(8,'Martina','García'),(9,'Pedro','Martínez'),(10,'Camila','Romero'),(11,'Laura','Delgado'),(12,'Jorge','Torres'),(13,'Miguel','Rodríguez'),(14,'Ricardo','Moreno');
/*!40000 ALTER TABLE `players` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teams`
--

DROP TABLE IF EXISTS `teams`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teams` (
  `team_id` int NOT NULL AUTO_INCREMENT,
  `team_name` varchar(100) DEFAULT NULL,
  `team_description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`team_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teams`
--

LOCK TABLES `teams` WRITE;
/*!40000 ALTER TABLE `teams` DISABLE KEYS */;
INSERT INTO `teams` VALUES (1,'Southside Juniors','Junior volleyball team for ages 12-14'),(2,'Northside Panthers','Basketball team for senior players'),(3,'Eastfield Eagles','Youth futsal team for ages 10-12'),(4,'Westwood Curlers','Beginner curling team for adults'),(5,'Riverdale Rockets','Advanced volleyball team for adults'),(6,'Downtown Dribblers','Intermediate basketball team'),(7,'Uptown Strikers','Teen futsal team for ages 15-17'),(8,'Lakeside Sweepers','Curling team for seniors'),(9,'Greenhill Spikers','Mixed volleyball team for college students'),(10,'Metro Hoopers','Competitive adult basketball team'),(11,'Sunset Shooters','Recreational futsal team'),(12,'Hilltop Hammers','Professional curling team'),(13,'City Slam','Urban youth basketball team'),(14,'Forest Flyers','Young beginners volleyball team');
/*!40000 ALTER TABLE `teams` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trainer_education`
--

DROP TABLE IF EXISTS `trainer_education`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trainer_education` (
  `trainer_id` int NOT NULL,
  `education_id` int NOT NULL,
  `completion_date` date DEFAULT NULL,
  `certificate_url` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`trainer_id`,`education_id`),
  KEY `fk_education_id_trainer_education_from_education` (`education_id`),
  CONSTRAINT `fk_education_id_trainer_education_from_education` FOREIGN KEY (`education_id`) REFERENCES `education` (`education_id`),
  CONSTRAINT `fk_trainer_id_trainer_education_from_trainers` FOREIGN KEY (`trainer_id`) REFERENCES `trainers` (`trainer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trainer_education`
--

LOCK TABLES `trainer_education` WRITE;
/*!40000 ALTER TABLE `trainer_education` DISABLE KEYS */;
INSERT INTO `trainer_education` VALUES (1,1,'2023-11-10','https://certificates.example.com/trainer1_volleyball.pdf'),(2,2,'2024-01-05','https://certificates.example.com/trainer2_basketball.pdf'),(3,3,'2023-12-15','https://certificates.example.com/trainer3_futsal.pdf'),(4,4,'2024-02-01','https://certificates.example.com/trainer4_curling.pdf'),(5,1,'2023-10-20','https://certificates.example.com/trainer5_volleyball.pdf'),(6,2,'2023-12-28','https://certificates.example.com/trainer6_basketball.pdf'),(7,1,'2024-01-18','https://certificates.example.com/trainer9_volleyball.pdf'),(7,3,'2024-01-14','https://certificates.example.com/trainer7_futsal.pdf'),(8,2,'2024-03-03','https://certificates.example.com/trainer10_basketball.pdf'),(8,4,'2024-02-20','https://certificates.example.com/trainer8_curling.pdf');
/*!40000 ALTER TABLE `trainer_education` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trainer_team`
--

DROP TABLE IF EXISTS `trainer_team`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trainer_team` (
  `trainer_id` int NOT NULL,
  `team_id` int NOT NULL,
  `start_date` date DEFAULT NULL,
  PRIMARY KEY (`trainer_id`,`team_id`),
  KEY `fk_team_id_trainer_team_from_teams` (`team_id`),
  CONSTRAINT `fk_team_id_trainer_team_from_teams` FOREIGN KEY (`team_id`) REFERENCES `teams` (`team_id`),
  CONSTRAINT `fk_trainer_id_trainer_team_from_trainers` FOREIGN KEY (`trainer_id`) REFERENCES `trainers` (`trainer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trainer_team`
--

LOCK TABLES `trainer_team` WRITE;
/*!40000 ALTER TABLE `trainer_team` DISABLE KEYS */;
INSERT INTO `trainer_team` VALUES (1,1,'2024-01-15'),(1,11,'2024-02-18'),(2,2,'2024-02-10'),(2,12,'2024-03-01'),(3,3,'2023-11-20'),(3,13,'2023-12-15'),(4,4,'2023-12-01'),(4,14,'2024-02-25'),(5,2,'2024-02-22'),(5,5,'2024-01-05'),(6,3,'2024-03-05'),(6,6,'2024-03-12'),(7,7,'2023-10-05'),(7,9,'2024-02-14'),(8,8,'2024-01-22'),(8,10,'2024-01-30');
/*!40000 ALTER TABLE `trainer_team` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trainers`
--

DROP TABLE IF EXISTS `trainers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trainers` (
  `trainer_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `trainer_description` varchar(255) DEFAULT NULL,
  `worked_hours` decimal(5,2) DEFAULT '0.00',
  `salary` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`trainer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trainers`
--

LOCK TABLES `trainers` WRITE;
/*!40000 ALTER TABLE `trainers` DISABLE KEYS */;
INSERT INTO `trainers` VALUES (1,'Laura','Martínez','Experienced volleyball coach',1.75,3500.00),(2,'Luis','García','Experienced basketball coach',2.50,3437.50),(3,'Valentina','Flores','Novice volleyball assistant',2.50,2250.00),(4,'Ricardo','Jiménez','Experienced futsal coach',2.25,3625.00),(5,'Martina','López','Experienced curling coach',1.25,3375.00),(6,'Andrés','Ramírez','Novice basketball assistant',1.50,2375.00),(7,'Pedro','Castro','Novice curling coach',0.00,2500.00),(8,'Elena','Sánchez','Experienced futsal coach',0.00,3500.00);
/*!40000 ALTER TABLE `trainers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `training_sessions`
--

DROP TABLE IF EXISTS `training_sessions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `training_sessions` (
  `session_id` int NOT NULL AUTO_INCREMENT,
  `session_date` date NOT NULL,
  `start_time` time NOT NULL,
  `duration_minutes` int unsigned DEFAULT NULL,
  `trainer_id` int DEFAULT NULL,
  `team_id` int DEFAULT NULL,
  `place_id` int NOT NULL,
  PRIMARY KEY (`session_id`),
  UNIQUE KEY `unique_trainer_team_date` (`trainer_id`,`team_id`,`session_date`,`start_time`),
  KEY `fk_team_id_training_sessions_from_teams` (`team_id`),
  KEY `fk_place_id_training_sessions_from_places` (`place_id`),
  CONSTRAINT `fk_place_id_training_sessions_from_places` FOREIGN KEY (`place_id`) REFERENCES `places` (`place_id`),
  CONSTRAINT `fk_team_id_training_sessions_from_teams` FOREIGN KEY (`team_id`) REFERENCES `teams` (`team_id`),
  CONSTRAINT `fk_trainer_id_training_sessions_from_trainers` FOREIGN KEY (`trainer_id`) REFERENCES `trainers` (`trainer_id`),
  CONSTRAINT `training_sessions_chk_1` CHECK ((`duration_minutes` >= 30))
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `training_sessions`
--

LOCK TABLES `training_sessions` WRITE;
/*!40000 ALTER TABLE `training_sessions` DISABLE KEYS */;
INSERT INTO `training_sessions` VALUES (1,'2024-03-01','17:00:00',60,1,1,1),(2,'2024-03-02','10:00:00',90,2,2,2),(3,'2024-03-03','09:00:00',60,3,3,3),(4,'2024-03-04','14:00:00',75,4,4,4),(5,'2024-03-05','16:30:00',45,1,11,1),(6,'2024-03-06','18:00:00',60,2,12,2),(7,'2024-03-07','19:00:00',90,3,13,3),(8,'2024-03-08','15:30:00',60,4,14,4),(9,'2024-03-09','17:15:00',75,5,2,1),(10,'2024-03-10','10:00:00',90,6,3,2);
/*!40000 ALTER TABLE `training_sessions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-06-22  5:10:48
