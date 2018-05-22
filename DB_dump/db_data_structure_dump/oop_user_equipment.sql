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
-- Table structure for table `user_equipment`
--

DROP TABLE IF EXISTS `user_equipment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_equipment` (
  `user_equipment_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `equipment_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`user_equipment_id`),
  KEY `fk_user_equipment_equipment1_idx` (`equipment_id`),
  KEY `fk_user_equipment_users1_idx` (`user_id`),
  CONSTRAINT `fk_user_equipment_equipment1` FOREIGN KEY (`equipment_id`) REFERENCES `equipment` (`equipment_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_equipment_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=234 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_equipment`
--

LOCK TABLES `user_equipment` WRITE;
/*!40000 ALTER TABLE `user_equipment` DISABLE KEYS */;
INSERT INTO `user_equipment` VALUES (40,51,404783),(41,51,404645),(42,51,404783),(43,51,404762),(44,51,404726),(45,51,404665),(46,51,404730),(47,51,404783),(48,51,404757),(49,50,404706),(50,50,404706),(51,50,404706),(52,50,404783),(53,50,404645),(54,50,404636),(55,50,404783),(56,50,404645),(57,50,404778),(58,50,221439),(59,50,404783),(60,50,404645),(61,50,404645),(62,50,404642),(63,50,404784),(64,50,404645),(65,50,404779),(66,50,404779),(67,50,405895),(68,50,404779),(69,50,404779),(70,50,404783),(71,50,404706),(72,50,404765),(73,50,404789),(74,50,404706),(75,50,404706),(76,50,404716),(77,50,404645),(78,50,405895),(79,50,404669),(80,50,404726),(81,50,404641),(82,50,404645),(83,50,404636),(84,50,404794),(85,50,404783),(86,50,404645),(87,51,404783),(88,51,404770),(89,51,404727),(90,51,404784),(91,51,404645),(92,51,404783),(93,51,404661),(94,51,404783),(95,51,404727),(96,51,404784),(97,51,404771),(98,51,404726),(99,51,404669),(100,51,404647),(101,51,404669),(102,51,405907),(103,51,404661),(104,50,404784),(105,50,404645),(106,50,404661),(107,50,404645),(108,50,404784),(109,58,404771),(110,58,404726),(111,58,404783),(112,58,404645),(113,58,404783),(114,58,404730),(115,58,405895),(116,58,404745),(117,50,404669),(118,50,404665),(119,50,404783),(120,50,404667),(121,50,404661),(122,50,404783),(123,50,405600),(124,50,404641),(125,50,405900),(126,50,405895),(127,59,404784),(128,59,404752),(129,59,404784),(130,59,404752),(131,59,404636),(132,59,404784),(133,59,404752),(134,59,404783),(135,59,404752),(136,59,404752),(137,50,404727),(138,50,404639),(139,50,404783),(140,50,404784),(141,50,404783),(142,50,404784),(143,50,405915),(144,50,404727),(145,50,404784),(146,50,404727),(147,50,404784),(148,59,404784),(149,59,404629),(150,59,404784),(151,59,404770),(152,59,404628),(153,59,404650),(154,59,404794),(155,59,404783),(156,59,404765),(157,59,404783),(158,59,404629),(159,59,404784),(160,59,404645),(161,59,404765),(162,59,404645),(163,59,404629),(164,59,405900),(165,59,404645),(166,59,404770),(167,59,404628),(168,59,404783),(169,59,404784),(170,59,404645),(171,59,404783),(172,59,404783),(173,59,404783),(174,59,404644),(175,59,404745),(176,59,404628),(177,59,404783),(178,59,404783),(179,59,404661),(180,59,404783),(181,59,404646),(182,59,405924),(183,59,404784),(184,59,404645),(185,59,404784),(186,59,404770),(187,59,404784),(188,50,404669),(189,50,404661),(190,50,404661),(191,50,404645),(192,50,404636),(193,50,404645),(194,50,404645),(195,50,404661),(196,59,404783),(197,59,404726),(198,59,404752),(199,59,404630),(200,59,404784),(201,59,404745),(202,59,404752),(203,59,404752),(204,59,404646),(205,59,404642),(206,59,404765),(207,59,404646),(208,59,404784),(209,59,404784),(210,59,404745),(211,59,404752),(212,59,404752),(213,59,404646),(214,59,404642),(215,59,404765),(216,59,404646),(217,59,404784),(218,59,404784),(219,59,404746),(220,59,405915),(221,59,404661),(222,59,404784),(223,59,404784),(224,59,404765),(225,59,404727),(226,59,404771),(227,59,404783),(228,59,405895),(229,59,404669),(230,59,404645),(231,60,404783),(232,60,404641),(233,60,404783);
/*!40000 ALTER TABLE `user_equipment` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-05-22  6:33:53
