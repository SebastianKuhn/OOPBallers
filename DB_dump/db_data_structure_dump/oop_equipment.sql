-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: oop
-- ------------------------------------------------------
-- Server version	5.7.22-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `equipment`
--

DROP TABLE IF EXISTS `equipment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `equipment` (
  `equipment_id` int(11) NOT NULL,
  `equipment_name` varchar(500) COLLATE utf8_unicode_ci DEFAULT NULL,
  `datetime_added` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`equipment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipment`
--

LOCK TABLES `equipment` WRITE;
/*!40000 ALTER TABLE `equipment` DISABLE KEYS */;
INSERT INTO `equipment` VALUES (221439,'kitchen towels','2018-05-21 19:27:12'),(404628,'hand mixer','2018-05-22 03:40:20'),(404629,'roasting pan','2018-05-22 03:40:20'),(404630,'ladle','2018-05-22 04:00:02'),(404636,'slotted spoon','2018-05-21 19:27:12'),(404639,'colander','2018-05-22 03:35:25'),(404641,'tongs','2018-05-21 19:27:12'),(404642,'spatula','2018-05-21 19:27:12'),(404644,'toothpicks','2018-05-22 03:40:20'),(404645,'frying pan','2018-05-21 19:27:12'),(404646,'baking pan','2018-05-21 19:27:12'),(404647,'cheesecloth','2018-05-21 19:27:12'),(404650,'springform pan','2018-05-22 03:40:20'),(404658,'pressure cooker','2018-05-21 19:27:12'),(404661,'whisk','2018-05-21 19:27:12'),(404665,'stand mixer','2018-05-21 19:27:12'),(404667,'dutch oven','2018-05-22 02:56:56'),(404669,'sauce pan','2018-05-21 19:27:12'),(404695,'kitchen timer','2018-05-21 19:27:12'),(404706,'grill','2018-05-21 19:27:12'),(404716,'cutting board','2018-05-21 19:27:12'),(404718,'slow cooker','2018-05-21 19:27:12'),(404726,'blender','2018-05-21 19:27:12'),(404727,'baking sheet','2018-05-21 19:27:12'),(404730,'plastic wrap','2018-05-21 19:27:12'),(404732,'wooden spoon','2018-05-21 19:27:12'),(404745,'knife','2018-05-22 00:48:10'),(404746,'rolling pin','2018-05-22 04:15:16'),(404752,'pot','2018-05-21 19:27:12'),(404757,'pastry bag','2018-05-21 19:27:12'),(404762,'microwave','2018-05-21 19:27:12'),(404765,'aluminum foil','2018-05-21 19:27:12'),(404770,'baking paper','2018-05-21 19:27:12'),(404771,'food processor','2018-05-21 19:27:12'),(404778,'box grater','2018-05-21 19:27:12'),(404779,'griddle','2018-05-21 19:27:12'),(404783,'bowl','2018-05-21 19:27:12'),(404784,'oven','2018-05-21 19:27:12'),(404789,'kitchen thermometer','2018-05-21 19:27:12'),(404794,'stove','2018-05-21 19:27:12'),(405600,'sieve','2018-05-22 02:56:56'),(405895,'paper towels','2018-05-21 19:27:12'),(405900,'wire rack','2018-05-22 02:56:56'),(405907,'mixing bowl','2018-05-21 19:27:12'),(405915,'pie form','2018-05-22 03:35:25'),(405924,'drinking straws','2018-05-22 03:44:54');
/*!40000 ALTER TABLE `equipment` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-05-22  6:33:51
