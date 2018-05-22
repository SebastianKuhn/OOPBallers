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
-- Table structure for table `instruction_ingredient`
--

DROP TABLE IF EXISTS `instruction_ingredient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `instruction_ingredient` (
  `instruction_ingredient_id` int(11) NOT NULL AUTO_INCREMENT,
  `recipe_instruction_id` int(11) DEFAULT NULL,
  `ingredient_id` int(11) DEFAULT NULL,
  `amount` float DEFAULT NULL,
  `unit` varchar(45) CHARACTER SET latin1 DEFAULT NULL,
  PRIMARY KEY (`instruction_ingredient_id`),
  KEY `_idx` (`recipe_instruction_id`),
  KEY `ingredient_id_idx` (`ingredient_id`),
  CONSTRAINT `ingredient_id` FOREIGN KEY (`ingredient_id`) REFERENCES `ingredients` (`ingredient_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `recipe_instruction_id` FOREIGN KEY (`recipe_instruction_id`) REFERENCES `recipe_instructions` (`recipe_instruction_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=168 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `instruction_ingredient`
--

LOCK TABLES `instruction_ingredient` WRITE;
/*!40000 ALTER TABLE `instruction_ingredient` DISABLE KEYS */;
INSERT INTO `instruction_ingredient` VALUES (1,149,14412,1.5,'cups'),(2,149,16069,0.5,'cup'),(3,151,2024,0.5,'teaspoon'),(4,151,2014,0.5,'teaspoon'),(5,151,4582,1,'tablespoon'),(6,152,31015,2,''),(7,152,93754,0.5,'teaspoon'),(8,153,93604,5,''),(9,154,11282,0.5,'cup'),(10,155,2047,2,'servings'),(11,157,2012,0.5,'teaspoon'),(12,157,2009,1,'teaspoon'),(13,157,2043,0.5,'teaspoon'),(14,159,14412,1.5,'cups'),(15,159,16069,0.5,'cup'),(16,161,16069,0.5,'cup'),(17,162,9021,16,'ounces'),(18,164,9273,4,'cups'),(19,164,9206,1,'cup'),(20,165,1002010,1,'sticks'),(21,165,1002010,6,''),(22,168,1002010,1,'sticks'),(23,168,1002010,6,''),(24,169,42135,1,'packet'),(25,172,18337,1,'sheet'),(26,173,1001,1,'tbsp'),(27,174,1040,0.5,'cup'),(28,174,11260,1,'cup'),(29,174,7059,1,'cup'),(30,174,1123,1,''),(31,174,1123,6,''),(32,175,1123,1,''),(33,175,1123,6,''),(34,176,1102047,8,'servings'),(35,176,11297,0.25,'cup'),(36,177,1123,1,''),(37,177,1123,6,''),(38,178,1123,1,''),(39,178,1123,6,''),(40,179,1123,1,''),(41,179,1123,6,''),(42,180,11590,8,'ounces'),(43,180,11124,1,'cup'),(44,180,10011457,10,'ounces'),(45,182,14412,2.5,'cups'),(46,183,14412,2.5,'cups'),(47,186,2053,5,'Tbsp'),(48,187,12023,9,'servings'),(49,187,11446,9,'servings'),(50,188,11446,9,'servings'),(51,189,12023,9,'servings'),(52,192,14400,1.5,'cups'),(53,192,14400,1.5,'cups'),(54,193,19335,1,'teaspoon'),(55,193,19335,0.25,'cup'),(56,193,1053,1,'cup'),(57,193,14400,1.5,'cups'),(58,194,2010,0.5,'teaspoon'),(59,194,19335,1,'teaspoon'),(60,194,19335,0.25,'cup'),(61,196,4582,2,'quarts'),(62,198,14400,1.5,'cups'),(63,198,18010,1,'cup'),(64,198,2050,1,'teaspoon'),(65,198,20081,0.25,'cup'),(66,201,4582,2,'quarts'),(67,204,14400,1.5,'cups'),(68,207,11916,2,'jars'),(69,207,11955,6,''),(70,207,93828,2,'jars'),(71,208,11215,6,'cloves'),(72,208,6008,28,'ounces'),(73,209,11955,6,''),(74,209,11215,6,'cloves'),(75,211,20409,12,'ounces'),(76,214,20081,2,'Tablespoons'),(77,215,93828,2,'jars'),(78,215,11297,12,'servings'),(79,215,11215,6,'cloves'),(80,215,20081,2,'Tablespoons'),(81,217,9003,3,''),(82,217,19335,0.75,'cup'),(83,217,19335,1,'tablespoon'),(84,218,9003,3,''),(85,219,19334,1,'tablespoon'),(86,219,9152,1,'tablespoon'),(87,219,2010,1,'teaspoon'),(88,219,1012047,0.25,'teaspoon'),(89,219,9003,3,''),(90,219,2025,0.125,'teaspoon'),(91,219,20081,2,'tablespoons'),(92,219,19335,0.75,'cup'),(93,219,19335,1,'tablespoon'),(94,220,18334,1,''),(95,221,18334,1,''),(96,221,9003,3,''),(97,222,18334,1,''),(98,223,1124,1,''),(99,230,11233,4,'cups'),(100,231,10118375,1,'tbsp'),(101,231,19335,1,'tsp'),(102,231,2047,1,'tsp'),(103,232,4053,3,'tbsp'),(104,232,14412,1,'cup'),(105,233,4053,3,'tbsp'),(106,234,10023572,250,'g'),(107,234,11282,1,''),(108,234,14412,1,'cup'),(109,236,11297,1,'handful'),(110,238,4053,3,'tbsp'),(111,240,20081,1,'tablespoon'),(112,246,11677,0.5,'cup'),(113,248,1056,3,'tablespoons'),(114,248,1002030,0.25,'teaspoon'),(115,248,2045,2,'tablespoons'),(116,248,2047,0.5,'teaspoon'),(117,250,12087,0.75,'cup'),(118,251,6615,6,'cups'),(119,251,12087,0.75,'cup'),(120,252,1012047,1.5,'teaspoons'),(121,252,1012047,6,'servings'),(122,252,11215,3,'cloves'),(123,253,11124,1,'cup'),(124,253,11143,1,'cup'),(125,254,12087,0.75,'cup'),(126,254,11233,2,'cups'),(127,259,11362,2,'pounds'),(128,259,14412,1,'cup'),(129,260,11124,4,'cups'),(130,260,2027,1,'teaspoon'),(131,260,11143,2,'cups'),(132,260,11215,3,'cloves'),(133,260,11282,2,'cups'),(134,262,14412,1,'cup'),(135,263,6971,1,'teaspoon'),(136,263,11887,1,''),(137,263,6168,1,'Dash'),(138,263,20081,0.25,'cup'),(139,265,11362,2,'pounds'),(140,265,1077,0.666667,'cup'),(141,266,11362,2,'pounds'),(142,271,1001,0.25,'cup'),(143,271,10018166,24,''),(144,275,11124,4,'ounces'),(145,276,11124,4,'ounces'),(146,277,9152,0.25,'cup'),(147,277,11124,4,'ounces'),(148,277,1006972,1,'tablespoon'),(149,277,12698,0.333333,'cup'),(150,277,1002014,0.25,'teaspoon'),(151,278,1006972,1,'tablespoon'),(152,279,12036,9,'servings'),(153,281,10123,4,'slices'),(154,282,11979,4,''),(155,282,11282,1,''),(156,282,4582,1,'tablespoon'),(157,283,11215,2,'cloves'),(158,284,1102047,4,'servings'),(159,284,10123,4,'slices'),(160,285,1009,1,'cup'),(161,285,1017,4,'ounces'),(162,285,11168,1,'cup'),(163,286,93610,6,'servings'),(164,287,2044,0.333333,'cup'),(165,288,4053,1,'tsp'),(166,288,19296,10,'g'),(167,289,11233,67,'g');
/*!40000 ALTER TABLE `instruction_ingredient` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-05-22  6:33:41
