--
-- Table structure for table `film`
--

DROP TABLE IF EXISTS `film`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `film` (
  `id_film` smallint(5) unsigned NOT NULL,
  `judul` varchar(128) NOT NULL,
  `tahun_rilis` year(4) DEFAULT NULL,
  `durasi` int(4) unsigned DEFAULT NULL,
  `bahasa` varchar(100) NOT NULL,
  `genre` varchar(100) NOT NULL,
  PRIMARY KEY (`id_film`),
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `film`
--

LOCK TABLES `film` WRITE;
/*!40000 ALTER TABLE `film` DISABLE KEYS */;
INSERT INTO `film` VALUES


/*!40000 ALTER TABLE `film` ENABLE KEYS */;
UNLOCK TABLES;







--
-- Table structure for table `format_film`
--

DROP TABLE IF EXISTS `format_film`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `format_film` (
  `id_film` smallint(5) unsigned NOT NULL,
  'format_film' varchar(10) NOT NULL,
  PRIMARY KEY (`id_film`, 'format_film'),
  KEY `id_film` (`id_film`),
  CONSTRAINT `format_film_ibfk_1` FOREIGN KEY (`id_film`) REFERENCES `film` (`id_film`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `format_film`
--

LOCK TABLES `format_film` WRITE;
/*!40000 ALTER TABLE `format_film` DISABLE KEYS */;
INSERT INTO `format_film` VALUES


/*!40000 ALTER TABLE `format_film` ENABLE KEYS */;
UNLOCK TABLES;











--
-- Table structure for table `studio`
--

DROP TABLE IF EXISTS `studio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `studio` (
  `no_studio` tinyint(2) unsigned NOT NULL,
  `tipe` varchar(10) NOT NULL,
  `kapasitas` tinyint(3) unsigned NOT NULL,
  PRIMARY KEY (`no_studio`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `studio`
--

LOCK TABLES `studio` WRITE;
/*!40000 ALTER TABLE `studio` DISABLE KEYS */;
INSERT INTO `studio` VALUES


/*!40000 ALTER TABLE `studio` ENABLE KEYS */;
UNLOCK TABLES;










--
-- Table structure for table `menayangkan`
--

DROP TABLE IF EXISTS `menayangkan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `menayangkan` (
  `id_film` smallint(5) unsigned NOT NULL,
  `no_studio` tinyint(2) unsigned NOT NULL,
  KEY `id_film` (`id_film`),
  KEY `no_studio` (`no_studio`),
  CONSTRAINT `menayangkan_ibfk_1` FOREIGN KEY (`id_film`) REFERENCES `film` (`id_film`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `menayangkan_ibfk_2` FOREIGN KEY (`no_studio`) REFERENCES `studio` (`no_studio`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menayangkan`
--

LOCK TABLES `menayangkan` WRITE;
/*!40000 ALTER TABLE `menayangkan` DISABLE KEYS */;
INSERT INTO `menayangkan` VALUES


/*!40000 ALTER TABLE `menayangkan` ENABLE KEYS */;
UNLOCK TABLES;









--
-- Table structure for table `pesanan`
--

DROP TABLE IF EXISTS `pesanan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pesanan` (
  `no_pesanan` int(10) unsigned NOT NULL,
  `waktu_transaksi` datetime NOT NULL,
  `id_pelanggan` int(8) unsigned NOT NULL,
  `id_pegawai` int(7) unsigned NOT NULL,
  KEY `id_pelanggan` (`id_pelanggan`),
  KEY `id_pegawai` (`id_pegawai`),
  CONSTRAINT `pesanan_ibfk_1` FOREIGN KEY (`id_pelanggan`) REFERENCES `pelanggan` (`id_pelanggan`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `pesanan_ibfk_2` FOREIGN KEY (`id_pegawai`) REFERENCES `pegawai` (`id_pegawai`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pesanan`
--

LOCK TABLES `pesanan` WRITE;
/*!40000 ALTER TABLE `pesanan` DISABLE KEYS */;
INSERT INTO `pesanan` VALUES


/*!40000 ALTER TABLE `pesanan` ENABLE KEYS */;
UNLOCK TABLES;









--
-- Table structure for table `pembayaran`
--

DROP TABLE IF EXISTS `pembayaran`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pembayaran` (
  `no_pembayaran` int(10) unsigned NOT NULL,
  `waktu_transaksi` datetime NOT NULL,
  `id_pelanggan` int(8) unsigned NOT NULL,
  `id_pegawai` int(7) unsigned NOT NULL,
  KEY `id_pelanggan` (`id_pelanggan`),
  KEY `id_pegawai` (`id_pegawai`),
  CONSTRAINT `pembayaran_ibfk_1` FOREIGN KEY (`id_pelanggan`) REFERENCES `pelanggan` (`id_pelanggan`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `pembayaran_ibfk_2` FOREIGN KEY (`id_pegawai`) REFERENCES `pegawai` (`id_pegawai`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pembayaran`
--

LOCK TABLES `pembayaran` WRITE;
/*!40000 ALTER TABLE `pembayaran` DISABLE KEYS */;
INSERT INTO `pembayaran` VALUES


/*!40000 ALTER TABLE `pembayaran` ENABLE KEYS */;
UNLOCK TABLES;