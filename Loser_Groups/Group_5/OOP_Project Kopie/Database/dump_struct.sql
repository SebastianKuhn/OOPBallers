-- MySQL dump 10.13  Distrib 5.7.17, for macos10.12 (x86_64)
--
-- Host: 127.0.0.1    Database: oopproject
-- ------------------------------------------------------
-- Server version	5.7.21

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
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `categories` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(100) NOT NULL,
  `category_plain` varchar(100) NOT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `requests`
--

DROP TABLE IF EXISTS `requests`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `requests` (
  `request_id` int(11) NOT NULL AUTO_INCREMENT,
  `updatetime` datetime NOT NULL,
  `latitude` varchar(100) NOT NULL,
  `longitude` varchar(100) NOT NULL,
  `categories_category_id` int(11) NOT NULL,
  PRIMARY KEY (`request_id`),
  KEY `fk_requests_categories1_idx` (`categories_category_id`),
  CONSTRAINT `fk_requests_categories1` FOREIGN KEY (`categories_category_id`) REFERENCES `categories` (`category_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `venue`
--

DROP TABLE IF EXISTS `venue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `venue` (
  `venue_id` int(11) NOT NULL AUTO_INCREMENT,
  `yelp_id` varchar(100) NOT NULL,
  `address` varchar(100) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `latitude` varchar(100) DEFAULT NULL,
  `longitude` varchar(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `rating` float DEFAULT NULL,
  `url` varchar(300) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `distance` float DEFAULT NULL,
  `requests_request_id` int(11) NOT NULL,
  PRIMARY KEY (`venue_id`),
  KEY `fk_venue_requests_idx` (`requests_request_id`),
  CONSTRAINT `fk_venue_requests` FOREIGN KEY (`requests_request_id`) REFERENCES `requests` (`request_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `weather`
--

DROP TABLE IF EXISTS `weather`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `weather` (
  `weather_ID` int(11) NOT NULL AUTO_INCREMENT,
  `curr_summary` varchar(100) DEFAULT NULL,
  `curr_temp` varchar(100) DEFAULT NULL,
  `curr_humidity` varchar(100) DEFAULT NULL,
  `curr_uvindex` varchar(100) DEFAULT NULL,
  `day0_summary` varchar(100) DEFAULT NULL,
  `day0_temp_high` varchar(100) DEFAULT NULL,
  `day0_temp_low` varchar(100) DEFAULT NULL,
  `day0_humidity` varchar(100) DEFAULT NULL,
  `day0_uvindex` varchar(100) DEFAULT NULL,
  `day1_summary` varchar(100) DEFAULT NULL,
  `day1_temp_high` varchar(100) DEFAULT NULL,
  `day1_temp_low` varchar(100) DEFAULT NULL,
  `day1_humidity` varchar(100) DEFAULT NULL,
  `day1_uvindex` varchar(100) DEFAULT NULL,
  `day2_summary` varchar(100) DEFAULT NULL,
  `day2_temp_high` varchar(100) DEFAULT NULL,
  `day2_temp_low` varchar(100) DEFAULT NULL,
  `day2_humidity` varchar(100) DEFAULT NULL,
  `day2_uvindex` varchar(100) DEFAULT NULL,
  `week_summary` varchar(200) DEFAULT NULL,
  `requests_request_id` int(11) NOT NULL,
  PRIMARY KEY (`weather_ID`),
  KEY `fk_weather_requests1_idx` (`requests_request_id`),
  CONSTRAINT `fk_weather_requests1` FOREIGN KEY (`requests_request_id`) REFERENCES `requests` (`request_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-05-22 22:42:42
