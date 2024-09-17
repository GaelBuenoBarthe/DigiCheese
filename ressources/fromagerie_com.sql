
--
-- Table structure for table `bonus`
--

DROP TABLE IF EXISTS `bonus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bonus` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `bonus_type` varchar(50) DEFAULT NULL,
  `points` decimal(10,2) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `ix_bonus_id` (`id`),
  CONSTRAINT `bonus_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `utilisateur` (`code_utilisateur`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bonus`
--

LOCK TABLES `bonus` WRITE;
/*!40000 ALTER TABLE `bonus` DISABLE KEYS */;
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
INSERT INTO `objet` VALUES (1,'Objet 1','Taille 1',10.0000,1.0000,0,1,1,1,10,1,1),(2,'Objet 2','Taille 2',20.0000,2.0000,0,2,2,2,20,2,2);
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `promo`
--

LOCK TABLES `promo` WRITE;
/*!40000 ALTER TABLE `promo` DISABLE KEYS */;
INSERT INTO `promo` VALUES (1,'Promo 1',10.00,100.00),(2,'Promo 2',20.00,200.00);
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

-- Dump completed on 2024-09-17 13:13:08
