-- MySQL dump 10.13  Distrib 9.0.1, for Linux (x86_64)
--
-- Host: localhost    Database: blackmirror
-- ------------------------------------------------------
-- Server version	9.0.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `%REDACTED_TABLE_NAME%`
--

DROP TABLE IF EXISTS `%REDACTED_TABLE_NAME%`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `%REDACTED_TABLE_NAME%` (
  `flag` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `%REDACTED_TABLE_NAME%`
--

LOCK TABLES `%REDACTED_TABLE_NAME%` WRITE;
/*!40000 ALTER TABLE `%REDACTED_TABLE_NAME%` DISABLE KEYS */;
INSERT INTO `%REDACTED_TABLE_NAME%` VALUES ('%FLAG_REDACTED%');
/*!40000 ALTER TABLE `%REDACTED_TABLE_NAME%` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `series`
--

DROP TABLE IF EXISTS `series`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `series` (
  `name` varchar(64) DEFAULT NULL,
  `season` int DEFAULT NULL,
  `episode` int DEFAULT NULL,
  `link`  varchar(128)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `series`
--

LOCK TABLES `series` WRITE;
/*!40000 ALTER TABLE `series` DISABLE KEYS */;
INSERT INTO `series` VALUES
('The National AnthemmehtnA lanoitaN ehT',1,1, 'https://www.imdb.com/title/tt2089051/'),
('Fifteen Million MeritsstireM noilliM neetfiF',1,2, 'https://www.imdb.com/title/tt2089049/'),
('The Entire History of YouuoY fo yrotsiH eritnE ehT',1,3, 'https://www.imdb.com/title/tt2089050/'),
('Be Right BackkcaB thgiR eB',2,1, 'https://www.imdb.com/title/tt2290780/'),
('White BearraeB etihW',2,2, 'https://www.imdb.com/title/tt2542420/'),
('The Waldo MomenttnemoM odlaW ehT',2,3, 'https://www.imdb.com/title/tt13665666/'),
('White ChristmassamtsirhC etihW',2014,NULL, 'https://www.imdb.com/title/tt13665600/'),
('NosediveevidesoN',3,1, 'https://www.imdb.com/title/tt5497778/'),
('PlaytesttsetyalP',3,2, 'https://www.imdb.com/title/tt5709242/'),
('Shut Up and DanceecnaD dna pU tuhS',3,3, 'https://www.imdb.com/title/tt5709230/'),
('San JuniperoorepinuJ naS',3,4, 'https://www.imdb.com/title/tt4538072/'),
('Men Against FireeriF tsniagA neM',3,5, 'https://www.imdb.com/title/tt5709234/'),
('Hated in the NationnoitaN eht ni detaH',3,6, 'https://www.imdb.com/title/tt5709236/'),
('USS CallisterretsillaC SSU',4,1, 'https://www.imdb.com/title/tt5710974/'),
('ArkangellegnakrA',4,2, 'https://www.imdb.com/de/title/tt5709250/'),
('CrocodileelidocorC',4,3, 'https://www.imdb.com/title/tt5710976/'),
('Hang the DJJD eht gnaH',4,4, 'https://www.imdb.com/title/tt5710978/'),
('MetalheaddaehlateM',4,5, 'https://www.imdb.com/title/tt2374902/'),
('Black MuseummuesuM kcalB',4,6, 'https://www.imdb.com/title/tt5058700/'),
('BandersnatchhctansrednaB',2018,NULL, 'https://www.imdb.com/title/tt9495224/'),
('Striking ViperssrepiV gnikirtS',5,1, 'https://www.imdb.com/title/tt8503298/'),
('Rachel Jack and Ashley TooooT yelhsA dna kcaJ lehcaR',5,2, 'https://www.imdb.com/title/tt9053874/'),
('Joan Is AwfullufwA sI naoJ',6,1, 'https://www.imdb.com/title/tt20247352/'),
('Loch HenryyrneH hcoL',6,2, 'https://www.imdb.com/title/tt27731608/'),
('Beyond the SeaaeS eht dnoyeB',6,3, 'https://www.imdb.com/title/tt27731623/'),
('Mazey DayyaD yezaM',6,4, 'https://www.imdb.com/title/tt27731663/'),
('Demon 7997 nomeD',6,5, 'https://www.imdb.com/title/tt27731671/');

/*!40000 ALTER TABLE `series` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-25 16:58:27
