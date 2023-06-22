-- MySQL dump 10.13  Distrib 8.0.31, for Linux (x86_64)
--
-- Host: localhost    Database: vivah
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `education`
--

DROP TABLE IF EXISTS `education`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `education` (
  `highest_education` varchar(44) DEFAULT NULL,
  `work_expierence` varchar(44) DEFAULT NULL,
  `employed_in` varchar(444) DEFAULT NULL,
  `occupation` varchar(444) DEFAULT NULL,
  `income` varchar(44) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `education`
--

LOCK TABLES `education` WRITE;
/*!40000 ALTER TABLE `education` DISABLE KEYS */;
INSERT INTO `education` VALUES ('k','k','k','k','44');
/*!40000 ALTER TABLE `education` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `family_details`
--

DROP TABLE IF EXISTS `family_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `family_details` (
  `family_status` varchar(44) DEFAULT NULL,
  `family_values` varchar(44) DEFAULT NULL,
  `family_type` varchar(44) DEFAULT NULL,
  `family_income` varchar(44) DEFAULT NULL,
  `father_occupation` varchar(44) DEFAULT NULL,
  `mother_occupation` varchar(44) DEFAULT NULL,
  `brothers` varchar(44) DEFAULT NULL,
  `brothers_married` varchar(44) DEFAULT NULL,
  `sisters` varchar(44) DEFAULT NULL,
  `sisters_married` varchar(44) DEFAULT NULL,
  `family_country` varchar(44) DEFAULT NULL,
  `gothra` varchar(44) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `family_details`
--

LOCK TABLES `family_details` WRITE;
/*!40000 ALTER TABLE `family_details` DISABLE KEYS */;
INSERT INTO `family_details` VALUES ('','','','','','','','','','','','');
/*!40000 ALTER TABLE `family_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `introduction`
--

DROP TABLE IF EXISTS `introduction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `introduction` (
  `full_name` varchar(98) DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `date_of_birth` varchar(20) DEFAULT NULL,
  `age` varchar(65) DEFAULT NULL,
  `height` varchar(20) DEFAULT NULL,
  `country` varchar(30) DEFAULT NULL,
  `state` varchar(34) DEFAULT NULL,
  `city` varchar(34) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `introduction`
--

LOCK TABLES `introduction` WRITE;
/*!40000 ALTER TABLE `introduction` DISABLE KEYS */;
INSERT INTO `introduction` VALUES ('k','male','k','44','44','k','k','k');
/*!40000 ALTER TABLE `introduction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `partner_preferences`
--

DROP TABLE IF EXISTS `partner_preferences`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `partner_preferences` (
  `partner_min_age` varchar(445) DEFAULT NULL,
  `partner_max_age` varchar(445) DEFAULT NULL,
  `partner_gender` varchar(445) DEFAULT NULL,
  `partner_minheight` varchar(989) DEFAULT NULL,
  `partner_maxheight` varchar(445) DEFAULT NULL,
  `partner_country` varchar(445) DEFAULT NULL,
  `partner_address` varchar(445) DEFAULT NULL,
  `partner_marital_status` varchar(445) DEFAULT NULL,
  `partner_marital_children` varchar(445) DEFAULT NULL,
  `partner_religion` varchar(445) DEFAULT NULL,
  `partner_caste` varchar(445) DEFAULT NULL,
  `Partner_mother_tongue` varchar(445) DEFAULT NULL,
  `partner_manglik` varchar(445) DEFAULT NULL,
  `partner_education` varchar(445) DEFAULT NULL,
  `partner_occupation` varchar(445) DEFAULT NULL,
  `partner_min_income` varchar(445) DEFAULT NULL,
  `partner_max_income` varchar(445) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `partner_preferences`
--

LOCK TABLES `partner_preferences` WRITE;
/*!40000 ALTER TABLE `partner_preferences` DISABLE KEYS */;
INSERT INTO `partner_preferences` VALUES ('33','43','male','34','34','k','k','k','k','k','k','k','k','k','k','45','56');
/*!40000 ALTER TABLE `partner_preferences` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reccomend_profile`
--

DROP TABLE IF EXISTS `reccomend_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reccomend_profile` (
  `full_name` varchar(98) DEFAULT NULL,
  `age` varchar(65) DEFAULT NULL,
  `height` varchar(20) DEFAULT NULL,
  `gender` varchar(34) DEFAULT NULL,
  `country` varchar(30) DEFAULT NULL,
  `state` varchar(34) DEFAULT NULL,
  `city` varchar(34) DEFAULT NULL,
  `income` varchar(79) DEFAULT NULL,
  `marital_status` varchar(89) DEFAULT NULL,
  `occupation` varchar(76) DEFAULT NULL,
  `highest_education` varchar(889) DEFAULT NULL,
  `mother_tongue` varchar(8989) DEFAULT NULL,
  `religion` varchar(77) DEFAULT NULL,
  `caste` varchar(98) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reccomend_profile`
--

LOCK TABLES `reccomend_profile` WRITE;
/*!40000 ALTER TABLE `reccomend_profile` DISABLE KEYS */;
INSERT INTO `reccomend_profile` VALUES ('k','44','44','male','k','k','k','44','k','k','k','k','k','k');
/*!40000 ALTER TABLE `reccomend_profile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_status`
--

DROP TABLE IF EXISTS `social_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `social_status` (
  `marital_status` varchar(44) DEFAULT NULL,
  `children_having` varchar(44) DEFAULT NULL,
  `mother_tongue` varchar(44) DEFAULT NULL,
  `religion` varchar(44) DEFAULT NULL,
  `caste` varchar(44) DEFAULT NULL,
  `caste_no_bar` varchar(67) DEFAULT NULL,
  `horoscope_marriage` varchar(44) DEFAULT NULL,
  `manglik` varchar(44) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_status`
--

LOCK TABLES `social_status` WRITE;
/*!40000 ALTER TABLE `social_status` DISABLE KEYS */;
INSERT INTO `social_status` VALUES ('k','k','k','k','k','k','','');
/*!40000 ALTER TABLE `social_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `whole_profile_detail`
--

DROP TABLE IF EXISTS `whole_profile_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `whole_profile_detail` (
  `full_name` varchar(98) DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `date_of_birth` varchar(20) DEFAULT NULL,
  `age` varchar(65) DEFAULT NULL,
  `height` varchar(20) DEFAULT NULL,
  `country` varchar(30) DEFAULT NULL,
  `state` varchar(34) DEFAULT NULL,
  `city` varchar(34) DEFAULT NULL,
  `highest_education` varchar(44) DEFAULT NULL,
  `work_expierence` varchar(44) DEFAULT NULL,
  `employed_in` varchar(444) DEFAULT NULL,
  `occupation` varchar(444) DEFAULT NULL,
  `income` varchar(44) DEFAULT NULL,
  `marital_status` varchar(44) DEFAULT NULL,
  `children_having` varchar(44) DEFAULT NULL,
  `mother_tongue` varchar(44) DEFAULT NULL,
  `religion` varchar(44) DEFAULT NULL,
  `caste` varchar(44) DEFAULT NULL,
  `caste_no_bar` varchar(67) DEFAULT NULL,
  `horoscope_marriage` varchar(44) DEFAULT NULL,
  `manglik` varchar(44) DEFAULT NULL,
  `family_status` varchar(44) DEFAULT NULL,
  `family_values` varchar(44) DEFAULT NULL,
  `family_type` varchar(44) DEFAULT NULL,
  `family_income` varchar(44) DEFAULT NULL,
  `father_occupation` varchar(44) DEFAULT NULL,
  `mother_occupation` varchar(44) DEFAULT NULL,
  `brothers` varchar(44) DEFAULT NULL,
  `brothers_married` varchar(44) DEFAULT NULL,
  `sisters` varchar(44) DEFAULT NULL,
  `sisters_married` varchar(44) DEFAULT NULL,
  `family_country` varchar(44) DEFAULT NULL,
  `gothra` varchar(44) DEFAULT NULL,
  `partner_min_age` varchar(445) DEFAULT NULL,
  `partner_max_age` varchar(445) DEFAULT NULL,
  `partner_gender` varchar(445) DEFAULT NULL,
  `partner_minheight` varchar(989) DEFAULT NULL,
  `partner_maxheight` varchar(445) DEFAULT NULL,
  `partner_country` varchar(445) DEFAULT NULL,
  `partner_address` varchar(445) DEFAULT NULL,
  `partner_marital_status` varchar(445) DEFAULT NULL,
  `partner_marital_children` varchar(445) DEFAULT NULL,
  `partner_religion` varchar(445) DEFAULT NULL,
  `partner_caste` varchar(445) DEFAULT NULL,
  `Partner_mother_tongue` varchar(445) DEFAULT NULL,
  `partner_manglik` varchar(445) DEFAULT NULL,
  `partner_education` varchar(445) DEFAULT NULL,
  `partner_occupation` varchar(445) DEFAULT NULL,
  `partner_min_income` varchar(445) DEFAULT NULL,
  `partner_max_income` varchar(445) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `whole_profile_detail`
--

LOCK TABLES `whole_profile_detail` WRITE;
/*!40000 ALTER TABLE `whole_profile_detail` DISABLE KEYS */;
INSERT INTO `whole_profile_detail` VALUES ('k','male','k','44','44','k','k','k','k','k','k','k','44','k','k','k','k','k','k','','','','','','','','','','','','','','','33','43','male','34','34','k','k','k','k','k','k','k','k','k','k','45','56');
/*!40000 ALTER TABLE `whole_profile_detail` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-22 17:36:57
