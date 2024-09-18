-- MySQL dump 10.13  Distrib 5.7.24, for Win64 (x86_64)
--
-- Host: localhost    Database: fromagerie_com
-- ------------------------------------------------------
-- Server version	8.0.39

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
/*!40000 ALTER TABLE `bonus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `client`
--

DROP TABLE IF EXISTS `client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `client` (
  `codcli` int NOT NULL AUTO_INCREMENT,
  `genre` varchar(8) DEFAULT NULL,
  `nom` varchar(40) DEFAULT NULL,
  `prenom` varchar(30) DEFAULT NULL,
  `adresse1` varchar(50) DEFAULT NULL,
  `adresse2` varchar(50) DEFAULT NULL,
  `adresse3` varchar(50) DEFAULT NULL,
  `ville_id` int DEFAULT NULL,
  `telephone` varchar(10) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `portable` varchar(10) DEFAULT NULL,
  `newsletter` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`codcli`),
  KEY `fk_client_commune` (`ville_id`),
  CONSTRAINT `fk_client_commune` FOREIGN KEY (`ville_id`) REFERENCES `commune` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client`
--

LOCK TABLES `client` WRITE;
/*!40000 ALTER TABLE `client` DISABLE KEYS */;
INSERT INTO `client` VALUES (1,'M','Client 1','Toto','Adresse 1','Adresse 2','Adresse 3',1,'0102030405','client1@example.com','0607080910',1),(2,'F','Client 2','Prenom 2','Adresse 1','Adresse 2','Adresse 3',2,'0102030406','client2@example.com','0607080911',0),(3,'M','Bueno','Gael','add1','add2','add3',1,'0400000000','gb@example.com','0600000000',1);
/*!40000 ALTER TABLE `client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `client_programme_fidelite`
--

DROP TABLE IF EXISTS `client_programme_fidelite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `client_programme_fidelite` (
  `client_id` int NOT NULL,
  `programme_fidelite_id` int NOT NULL,
  PRIMARY KEY (`client_id`,`programme_fidelite_id`),
  KEY `programme_fidelite_id` (`programme_fidelite_id`),
  CONSTRAINT `client_programme_fidelite_ibfk_1` FOREIGN KEY (`client_id`) REFERENCES `client` (`codcli`),
  CONSTRAINT `client_programme_fidelite_ibfk_2` FOREIGN KEY (`programme_fidelite_id`) REFERENCES `programme_fidelite` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client_programme_fidelite`
--

LOCK TABLES `client_programme_fidelite` WRITE;
/*!40000 ALTER TABLE `client_programme_fidelite` DISABLE KEYS */;
INSERT INTO `client_programme_fidelite` VALUES (1,1),(2,2);
/*!40000 ALTER TABLE `commande` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `commune`
--

DROP TABLE IF EXISTS `commune`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `commune` (
  `id` int NOT NULL AUTO_INCREMENT,
  `code_postal` varchar(50) DEFAULT NULL,
  `nom` varchar(50) DEFAULT NULL,
  `departement_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `departement_id` (`departement_id`),
  KEY `ix_commune_id` (`id`),
  CONSTRAINT `commune_ibfk_1` FOREIGN KEY (`departement_id`) REFERENCES `departement` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `commune`
--

LOCK TABLES `commune` WRITE;
/*!40000 ALTER TABLE `commune` DISABLE KEYS */;
INSERT INTO `commune` VALUES (1,'34000','Montpellier',1),(2,'31000','Toulouse',2);
/*!40000 ALTER TABLE `conditionnement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `departement`
--

DROP TABLE IF EXISTS `departement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `departement` (
  `id` int NOT NULL AUTO_INCREMENT,
  `code` varchar(50) DEFAULT NULL,
  `nom` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_departement_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departement`
--

LOCK TABLES `departement` WRITE;
/*!40000 ALTER TABLE `departement` DISABLE KEYS */;
INSERT INTO `departement` VALUES (1,'34','Hérault'),(2,'31','Haute-Garonne');
/*!40000 ALTER TABLE `departement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detailcde`
--

DROP TABLE IF EXISTS `detailcde`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `detailcde` (
  `id` int NOT NULL AUTO_INCREMENT,
  `detail_id` int DEFAULT NULL,
  `objet_id` int DEFAULT NULL,
  `codcde` int DEFAULT NULL,
  `qte` int DEFAULT NULL,
  `colis` int DEFAULT NULL,
  `commentaire` varchar(100) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_detailcde_objet_id` (`objet_id`),
  KEY `ix_detailcde_codcde` (`codcde`),
  KEY `ix_detailcde_detail_id` (`detail_id`),
  CONSTRAINT `detailcde_ibfk_1` FOREIGN KEY (`codcde`) REFERENCES `commande` (`codcde`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detailcde`
--

LOCK TABLES `detailcde` WRITE;
/*!40000 ALTER TABLE `detailcde` DISABLE KEYS */;
INSERT INTO `detailcde` VALUES (1,1,1,1,1,1,'Commentaire 1','Detail 1'),(2,2,2,2,2,2,'Commentaire 2','Detail 2');
/*!40000 ALTER TABLE `detailob` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `enseigne`
--

DROP TABLE IF EXISTS `enseigne`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `enseigne` (
  `id` int NOT NULL AUTO_INCREMENT,
  `libelle` varchar(50) DEFAULT NULL,
  `ville` varchar(50) DEFAULT NULL,
  `departement_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `departement_id` (`departement_id`),
  KEY `ix_enseigne_id` (`id`),
  CONSTRAINT `enseigne_ibfk_1` FOREIGN KEY (`departement_id`) REFERENCES `departement` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `enseigne`
--

LOCK TABLES `enseigne` WRITE;
/*!40000 ALTER TABLE `enseigne` DISABLE KEYS */;
INSERT INTO `enseigne` VALUES (1,'Enseigne 1','Ville 1',1),(2,'Enseigne 2','Ville 2',2);
/*!40000 ALTER TABLE `objet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `poids`
--

DROP TABLE IF EXISTS `poids`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `poids` (
  `id` int NOT NULL AUTO_INCREMENT,
  `valmin` decimal(10,0) DEFAULT NULL,
  `valtimbre` decimal(10,0) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `poids`
--

LOCK TABLES `poids` WRITE;
/*!40000 ALTER TABLE `poids` DISABLE KEYS */;
INSERT INTO `poids` VALUES (1,10,20),(2,15,25);
/*!40000 ALTER TABLE `poids` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `programme_fidelite`
--

DROP TABLE IF EXISTS `programme_fidelite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `programme_fidelite` (
  `id` int NOT NULL AUTO_INCREMENT,
  `points` decimal(10,2) DEFAULT NULL,
  `level` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_programme_fidelite_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `programme_fidelite`
--

LOCK TABLES `programme_fidelite` WRITE;
/*!40000 ALTER TABLE `programme_fidelite` DISABLE KEYS */;
INSERT INTO `programme_fidelite` VALUES (1,100.00,'Silver'),(2,200.00,'Gold');
/*!40000 ALTER TABLE `promo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `role` (
  `codrole` int NOT NULL AUTO_INCREMENT,
  `librole` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`codrole`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
INSERT INTO `role` VALUES (1,'Role 1'),(2,'Role 2');
/*!40000 ALTER TABLE `t_rel_cond` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transaction`
--

DROP TABLE IF EXISTS `transaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `transaction` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `amount_spent` decimal(10,2) DEFAULT NULL,
  `points_earned` decimal(10,2) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `ix_transaction_id` (`id`),
  CONSTRAINT `transaction_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `client` (`codcli`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaction`
--

LOCK TABLES `transaction` WRITE;
/*!40000 ALTER TABLE `transaction` DISABLE KEYS */;
INSERT INTO `transaction` VALUES (1,1,100.00,10.00,'Transaction 1'),(2,2,200.00,20.00,'Transaction 2');
/*!40000 ALTER TABLE `transaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `utilisateur`
--

DROP TABLE IF EXISTS `utilisateur`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `utilisateur` (
  `code_utilisateur` int NOT NULL AUTO_INCREMENT,
  `nom_utilisateur` varchar(50) DEFAULT NULL,
  `prenom_utilisateur` varchar(50) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `couleur_fond_utilisateur` int DEFAULT NULL,
  `date_insc_utilisateur` date DEFAULT NULL,
  PRIMARY KEY (`code_utilisateur`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `utilisateur`
--

LOCK TABLES `utilisateur` WRITE;
/*!40000 ALTER TABLE `utilisateur` DISABLE KEYS */;
INSERT INTO `utilisateur` VALUES (1,'Utilisateur 1','Toto','Totoweb',1,'2024-01-01'),(2,'Utilisateur 2','Tata','Tataweb',2,'2024-01-02');
/*!40000 ALTER TABLE `utilisateur_role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vignette`
--

DROP TABLE IF EXISTS `vignette`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vignette` (
  `id` int NOT NULL AUTO_INCREMENT,
  `valmin` decimal(10,0) DEFAULT NULL,
  `valtimbre` decimal(10,0) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vignette`
--

LOCK TABLES `vignette` WRITE;
/*!40000 ALTER TABLE `vignette` DISABLE KEYS */;
INSERT INTO `vignette` VALUES (1,10,20),(2,15,25);
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-18 14:18:23
