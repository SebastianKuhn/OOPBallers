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
-- Table structure for table `recipes`
--

DROP TABLE IF EXISTS `recipes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recipes` (
  `recipe_id` int(11) NOT NULL,
  `title` text COLLATE utf8_unicode_ci,
  `ready_in_minutes` int(11) DEFAULT NULL,
  `servings` int(11) DEFAULT NULL,
  `vegetarian` tinyint(4) DEFAULT NULL,
  `source_url` text COLLATE utf8_unicode_ci,
  `aggregate_likes` int(11) DEFAULT NULL,
  `health_score` int(11) DEFAULT NULL,
  `date_time_added` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`recipe_id`),
  UNIQUE KEY `recipe_id_UNIQUE` (`recipe_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipes`
--

LOCK TABLES `recipes` WRITE;
/*!40000 ALTER TABLE `recipes` DISABLE KEYS */;
INSERT INTO `recipes` VALUES (21704,'Scrambled Eggs With Bacon And Avocado',15,1,0,'http://www.marthastewart.com/316417/scrambled-eggs-with-bacon-and-avocado',5,7,'2018-05-21 19:24:18'),(24625,'Savory Pumpkin Rosemary Bread',45,16,1,'http://www.food52.com/recipes/4003_savory_pumpkin_rosemary_bread',5,24,'2018-05-21 19:24:18'),(28940,'Italian Pot Roast',241,12,0,'http://thepioneerwoman.com/cooking/2012/10/italian-pot-roast/',0,23,'2018-05-22 03:18:42'),(50549,'Blackberry Pineapple Mojito',45,1,1,'http://www.myrecipes.com/recipe/blackberry-pineapple-mojito-10000001816267/',0,14,'2018-05-21 19:24:18'),(86413,'Fijian Fish Lolo',25,4,0,'http://www.food.com/recipe/fijian-fish-lolo-334952',0,11,'2018-05-21 19:24:18'),(94654,'Shredded Beef Barbecue',375,6,0,'http://www.food.com/recipe/shredded-beef-barbecue-239694',0,20,'2018-05-22 03:55:52'),(103321,'Sweet Barbecue Kim-cheese Burgers',60,4,0,'http://www.seriouseats.com/recipes/2012/07/sweet-barbecue-kim-cheese-burgers-recipe.html',0,21,'2018-05-21 19:24:18'),(113524,'Peanut Butter Squares',20,48,0,'http://www.tasteofhome.com/recipes/peanut-butter-squares-2',0,0,'2018-05-21 19:24:18'),(148705,'Ode to Brad Pitt',35,6,0,'http://www.food.com/recipe/ode-to-brad-pitt-141766',0,5,'2018-05-21 19:24:18'),(191852,'Beef Stroganov',45,6,0,'http://www.epicurious.com/recipes/food/views/105587',0,13,'2018-05-22 03:56:09'),(201753,'Roesti with Shallots and Pancetta',40,2,0,'http://www.seriouseats.com/recipes/2012/12/roesti-with-shallots-and-pancetta-recipe.html',265,22,'2018-05-21 19:24:18'),(202880,'Giant Barbecue Bacon Burger',36,6,0,'http://www.myrecipes.com/recipe/giant-barbecue-bacon-burger-10000001830681/',0,13,'2018-05-21 19:24:18'),(203677,'Smoked Gouda and Bacon Burgers with Barbecue Sauce',40,40,0,'http://www.myrecipes.com/recipe/smoked-gouda-bacon-burgers-barbecue-sauce-53420000020445/',0,1,'2018-05-21 19:24:18'),(205186,'Fried Coke',60,4,1,'http://www.seriouseats.com/recipes/2012/09/fried-coke-recipe.html',273,3,'2018-05-22 02:56:56'),(228132,'5:2 Diet - Savoury Cauliflower Rice = 137 calories',50,4,1,'http://www.tinnedtomatoes.com/2013/03/52-diet-savoury-cauliflower-rice-137.html',1665,49,'2018-05-21 19:24:18'),(235325,'Sausage Pizza',45,6,0,'http://www.myrecipes.com/m/recipe/sausage-pizza-50400000125791/',0,3,'2018-05-22 04:20:17'),(245360,'Eggs Benedict',45,4,0,'http://www.simplyrecipes.com/recipes/eggs_benedict/',5115,5,'2018-05-21 19:24:18'),(249107,'Jalapeno Popper Chicken Soup',45,4,0,'http://www.closetcooking.com/2013/12/jalapeno-popper-chicken-soup.html',8874,14,'2018-05-22 04:15:58'),(300106,'Arugula Pesto: Pesto Di Rucola',10,8,0,'http://www.foodnetwork.com/recipes/arugula-pesto-pesto-di-rucola-recipe.html',0,6,'2018-05-21 19:24:18'),(366101,'Apricot Wassail',30,8,1,'http://www.tasteofhome.com/Recipes/apricot-wassail',0,17,'2018-05-21 19:24:18'),(444601,'Chocolaty Peanut Clusters',130,84,0,'http://www.tasteofhome.com/recipes/chocolaty-peanut-clusters',176,1,'2018-05-21 19:24:18'),(445187,'Spinach Broccoli Salad',15,8,1,'http://www.tasteofhome.com/recipes/spinach-broccoli-salad',3,89,'2018-05-22 00:42:10'),(480733,'Clean Eating Raspberry Chocolate Frosting',10,4,1,'http://realfoodrealdeals.com/2014/02/06/clean-eating-raspberry-chocolate-frosting/',453,6,'2018-05-21 19:24:18'),(487010,'Asian Barbecue Burger Patties',30,4,0,'http://allrecipes.com/Recipe/Asian-Barbecue-Burgers/Detail.aspx?src=rss',131,6,'2018-05-21 19:24:18'),(487665,'Light Fluffy Frosting',45,3,0,'http://www.thelawstudentswife.com/2012/09/light-fluffy-frosting/',60,5,'2018-05-21 19:24:18'),(491574,'Spiked Peach Tea',45,3,1,'http://theblondcook.com/2012/04/spiked-peach-tea/',2128,1,'2018-05-21 19:24:18'),(494968,'One-Pot Pasta Primavera',20,6,0,'http://ohmyveggies.com/one-pot-pasta-primavera/',9755,54,'2018-05-21 19:24:18'),(499855,'Pina Colada Cake',45,15,1,'http://cantstayoutofthekitchen.com/2014/05/10/pina-colada-cake/',7051,1,'2018-05-22 03:44:54'),(506312,'Kale and Purple Cabbage Salad',45,1,1,'http://greenlitebites.com/2013/01/08/kale-and-purple-cabbage-salad/',659,100,'2018-05-22 04:26:16'),(517275,'Green Velvet Cheesecake Cake',135,14,0,'http://www.recipegirl.com/2012/03/05/green-velvet-cheesecake-cake/',95265,1,'2018-05-22 03:40:19'),(559187,'Scrambled Eggs in Puff Pastry',45,8,0,'http://www.jocooks.com/bakery/pastries/scrambled-eggs-in-puff-pastry/',2817,5,'2018-05-21 23:40:41'),(577801,'Bourbon, Lemon, and Honey',45,1,1,'http://naturallyella.com/2013/06/14/bourbon-lemon-and-honey/',228,0,'2018-05-21 19:24:18'),(582031,'Turkish Pide with Ground Beef',110,4,0,'http://www.giverecipe.com/turkish-pide-with-ground-beef.html',42,46,'2018-05-22 03:48:31'),(582938,'Sushi Rice and California Rolls',80,9,0,'http://natashaskitchen.com/2013/10/23/sushi-rice-and-california-rolls-recipe/',8348,14,'2018-05-22 00:48:10'),(594589,'Lightened Up Kale Caesar Salad',5,2,0,'http://www.tablefortwoblog.com/lightened-up-kale-caesar-salad/',2676,79,'2018-05-22 03:44:36'),(595093,'Cheddar Topped Shepherd’s Pie',75,12,0,'http://www.afamilyfeast.com/cheddar-topped-shepherds-pie/',6442,20,'2018-05-22 04:08:28'),(598130,'New York Times Pumpkin Pie with an Oreo Crust',45,8,1,'http://www.somethingswanky.com/new-york-times-pumpkin-cheesecake-with-an-oreo-crust/',12033,6,'2018-05-22 04:15:15'),(600763,'Moong Dal Fry',30,2,1,'http://www.spiceupthecurry.com/moong-dal-fry/',53,38,'2018-05-21 19:24:18'),(615454,'10-Spice Vegetable Soup (Freezer Friendly, Vegan, Gluten-Free)',60,6,0,'http://ohsheglows.com/2014/10/02/10-spice-vegetable-soup-freezer-friendly-vegan-gluten-free/',3511,79,'2018-05-22 04:00:00'),(630607,'Cilantro Lime Tilapia Tacos Skinnytaste',30,4,0,'http://www.skinnytaste.com/2012/02/cilantro-lime-tilapia-tacos.html',7814,71,'2018-05-21 19:24:18'),(631759,'Simit (Turkish Circular Bread)',45,8,1,'http://www.foodista.com/recipe/C4JM5WTQ/simit-turkish-circular-bread',2,41,'2018-05-21 19:24:18'),(715328,'The Best Apple Pie',75,10,1,'http://www.midgetmomma.com/2014/10/31/best-apple-pie/',27139,1,'2018-05-22 03:35:24'),(723984,'Cabbage Salad with Peanuts',15,2,1,'http://naturallyella.com/cabbage-salad-with-peanuts/',406,93,'2018-05-21 19:24:18'),(779313,'Pineapple Crisp',60,4,1,'http://www.thereciperebel.com/pineapple-crisp/',355,9,'2018-05-21 19:24:18'),(812124,'Cherry Coconut Chocolate Smoothie',5,1,0,'http://ahealthylifeforme.com/cherry-coconut-chocolate-smoothie/',1375,76,'2018-05-21 19:24:18'),(871974,'Spicy Carrot Hummus',45,9,1,'http://www.bonappetit.com/recipe/spicy-harissa-carrot-hummus',0,58,'2018-05-22 04:15:36'),(953869,'No Knead Rosemary Bread',1495,8,1,'https://damndelicious.net/2017/12/05/no-knead-rosemary-bread/',1690,16,'2018-05-21 19:24:18'),(1006419,'Unicorn Cupcakes',30,24,0,'https://www.crazyforcrust.com/unicorn-cupcakes/',115,0,'2018-05-21 19:24:18');
/*!40000 ALTER TABLE `recipes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-05-22  6:33:47