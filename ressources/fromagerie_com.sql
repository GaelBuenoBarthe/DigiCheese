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
  `fidelite` int DEFAULT NULL,
  PRIMARY KEY (`codcli`),
  KEY `fk_client_commune` (`ville_id`),
  KEY `fk_client_programme_fidelite` (`fidelite`),
  CONSTRAINT `fk_client_commune` FOREIGN KEY (`ville_id`) REFERENCES `commune` (`id`),
  CONSTRAINT `fk_client_programme_fidelite` FOREIGN KEY (`fidelite`) REFERENCES `programme_fidelite` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client`
--

LOCK TABLES `client` WRITE;
/*!40000 ALTER TABLE `client` DISABLE KEYS */;
INSERT INTO `client` VALUES (1,'M','Client 1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(2,'F','Client 2',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `commande`
--

DROP TABLE IF EXISTS `commande`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `commande` (
  `codcde` int NOT NULL AUTO_INCREMENT,
  `datcde` date DEFAULT NULL,
  `codcli` int DEFAULT NULL,
  `timbrecli` float DEFAULT NULL,
  `timbre_cde` float DEFAULT NULL,
  `nbcolis` int DEFAULT NULL,
  `cheqcli` float DEFAULT NULL,
  `idcondit` int DEFAULT NULL,
  `cdeComt` varchar(255) DEFAULT NULL,
  `barchive` int DEFAULT NULL,
  `bstock` int DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`codcde`),
  KEY `codcli` (`codcli`),
  KEY `commande_index` (`cdeComt`,`codcli`),
  CONSTRAINT `commande_ibfk_1` FOREIGN KEY (`codcli`) REFERENCES `client` (`codcli`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `commande`
--

LOCK TABLES `commande` WRITE;
/*!40000 ALTER TABLE `commande` DISABLE KEYS */;
INSERT INTO `commande` VALUES (1,'2023-01-01',1,1,1,1,1,1,'Commentaire 1',0,0,'Commande 1'),(2,'2023-01-02',2,2,2,2,2,2,'Commentaire 2',0,0,'Commande 2');
/*!40000 ALTER TABLE `commune` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `conditionnement`
--

DROP TABLE IF EXISTS `conditionnement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `conditionnement` (
  `idcondit` int NOT NULL AUTO_INCREMENT,
  `libcondit` varchar(50) DEFAULT NULL,
  `poidscondit` int DEFAULT NULL,
  `prixcond` decimal(10,0) DEFAULT NULL,
  `ordreimp` int DEFAULT NULL,
  PRIMARY KEY (`idcondit`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `conditionnement`
--

LOCK TABLES `conditionnement` WRITE;
/*!40000 ALTER TABLE `conditionnement` DISABLE KEYS */;
INSERT INTO `conditionnement` VALUES (1,'Conditionnement 1',1,10,1),(2,'Conditionnement 2',2,20,2);
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
  `codcde` int DEFAULT NULL,
  `qte` int DEFAULT NULL,
  `colis` int DEFAULT NULL,
  `commentaire` varchar(100) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_detailcde_codcde` (`codcde`),
  CONSTRAINT `detailcde_ibfk_1` FOREIGN KEY (`codcde`) REFERENCES `commande` (`codcde`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detailcde`
--

LOCK TABLES `detailcde` WRITE;
/*!40000 ALTER TABLE `detailcde` DISABLE KEYS */;
INSERT INTO `detailcde` VALUES (1,1,1,1,'Commentaire 1','Detail 1'),(2,2,2,2,'Commentaire 2','Detail 2');
/*!40000 ALTER TABLE `detailcde` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detailob`
--

DROP TABLE IF EXISTS `detailob`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `detailob` (
  `id` int NOT NULL AUTO_INCREMENT,
  `detail_id` int DEFAULT NULL,
  `objet_id` int DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `detail_id` (`detail_id`),
  KEY `objet_id` (`objet_id`),
  CONSTRAINT `detailob_ibfk_1` FOREIGN KEY (`detail_id`) REFERENCES `detailcde` (`id`),
  CONSTRAINT `detailob_ibfk_2` FOREIGN KEY (`objet_id`) REFERENCES `objet` (`codobj`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detailob`
--

LOCK TABLES `detailob` WRITE;
/*!40000 ALTER TABLE `detailob` DISABLE KEYS */;
INSERT INTO `detailob` VALUES (1,1,1,'DetailObjet 1'),(2,2,2,'DetailObjet 2');
/*!40000 ALTER TABLE `enseigne` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `objet`
--

DROP TABLE IF EXISTS `objet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `objet` (
  `codobj` int NOT NULL AUTO_INCREMENT,
  `libobj` varchar(50) DEFAULT NULL,
  `tailleobj` varchar(50) DEFAULT NULL,
  `puobj` decimal(10,4) DEFAULT NULL,
  `poidsobj` decimal(10,4) DEFAULT NULL,
  `indispobj` int DEFAULT NULL,
  `o_imp` int DEFAULT NULL,
  `o_aff` int DEFAULT NULL,
  `o_cartp` int DEFAULT NULL,
  `points` int DEFAULT NULL,
  `o_ordre_aff` int DEFAULT NULL,
  `conditionnement_id` int DEFAULT NULL,
  PRIMARY KEY (`codobj`),
  KEY `conditionnement_id` (`conditionnement_id`),
  KEY `ix_objet_codobj` (`codobj`),
  CONSTRAINT `objet_ibfk_1` FOREIGN KEY (`conditionnement_id`) REFERENCES `conditionnement` (`idcondit`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `objet`
--

LOCK TABLES `objet` WRITE;
/*!40000 ALTER TABLE `objet` DISABLE KEYS */;
INSERT INTO `objet` VALUES (1,'Objet 1',NULL,0.0000,0.0000,0,0,0,0,0,0,1),(2,'Objet 2',NULL,0.0000,0.0000,0,0,0,0,0,0,2);
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
/*!40000 ALTER TABLE `programme_fidelite` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `promo`
--

DROP TABLE IF EXISTS `promo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `promo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `discount_percentage` decimal(5,2) DEFAULT NULL,
  `points_required` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_promo_id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `promo`
--

LOCK TABLES `promo` WRITE;
/*!40000 ALTER TABLE `promo` DISABLE KEYS */;
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_rel_cond`
--

DROP TABLE IF EXISTS `t_rel_cond`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_rel_cond` (
  `idrelcond` int NOT NULL AUTO_INCREMENT,
  `qteobjdeb` int DEFAULT NULL,
  `qteobjfin` int DEFAULT NULL,
  `codobj` int DEFAULT NULL,
  `codcond` int DEFAULT NULL,
  PRIMARY KEY (`idrelcond`),
  KEY `codobj` (`codobj`),
  KEY `codcond` (`codcond`),
  KEY `ix_t_rel_cond_idrelcond` (`idrelcond`),
  CONSTRAINT `t_rel_cond_ibfk_1` FOREIGN KEY (`codobj`) REFERENCES `objet` (`codobj`),
  CONSTRAINT `t_rel_cond_ibfk_2` FOREIGN KEY (`codcond`) REFERENCES `conditionnement` (`idcondit`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_rel_cond`
--

LOCK TABLES `t_rel_cond` WRITE;
/*!40000 ALTER TABLE `t_rel_cond` DISABLE KEYS */;
INSERT INTO `t_rel_cond` VALUES (1,10,20,1,1),(2,15,25,2,2);
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
INSERT INTO `utilisateur` VALUES (1,'Utilisateur 1',NULL,NULL,0,NULL),(2,'Utilisateur 2',NULL,NULL,0,NULL);
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
/*!40000 ALTER TABLE `vignette` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'fromagerie_com'
--
