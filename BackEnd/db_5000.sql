-- MariaDB dump 10.19  Distrib 10.5.22-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: storedb
-- ------------------------------------------------------
-- Server version	10.5.22-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `documents`
--
DROP TABLE IF EXISTS `documents`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `documents` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `text` text NOT NULL,
  `date` varchar(255) NOT NULL,
  `category` varchar(255) NOT NULL,
  `url` varchar(255) NOT NULL,
  `state` int(11) NOT NULL,
  `summary` text DEFAULT NULL,
  `location` text DEFAULT NULL,
  `lat` varchar(255) DEFAULT NULL,
  `lng` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=137 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `documents`
--

LOCK TABLES `documents` WRITE;
/*!40000 ALTER TABLE `documents` DISABLE KEYS */;
/*!40000 ALTER TABLE `documents` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `geocache`
--

DROP TABLE IF EXISTS `geocache`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `geocache` (
  `location_id` int(11) NOT NULL AUTO_INCREMENT,
  `location` varchar(255) NOT NULL,
  `lat` varchar(255) DEFAULT NULL,
  `lng` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`location_id`)
) ENGINE=InnoDB AUTO_INCREMENT=134 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `geocache`
--

LOCK TABLES `geocache` WRITE;
/*!40000 ALTER TABLE `geocache` DISABLE KEYS */;
INSERT INTO `geocache` VALUES (1,'Montevideo, Uruguay','-34.9055016','-56.1851147'),(2,'Retén de Carabineros de Curaco de Vélez','-42.43892930000001','-73.5945464'),(3,'Chile','-35.675147','-71.542969'),(4,'La Araucanía, Selva Oscura Villa Cautín, Victoria, Curacautín, Rariruca','-38.3699435','-72.16994799999999'),(5,'Chile, Santiago, Región Metropolitana','-33.4843354','-70.6216794'),(6,'Ñuñoa, Santiago, Chile','-33.4566678','-70.5978415'),(7,'Melipilla, Chile','-33.6858668','-71.2180485'),(8,'La Dehesa, Santiago, Chile','-33.3335344','-70.526396'),(9,'Santiago','-33.4488897','-70.6692655'),(10,'Providencia, Región Metropolitana, Chile','-33.4314474','-70.6093325'),(11,'Iquique, Región de Tarapacá, Chile','-20.2307033','-70.1356692'),(12,'Hamelín','52.1042035','9.3616'),(13,'Comisión de Vigilancia de la Auditoría Superior de la Federación',' ',' '),(14,'Banco Central',' ',' '),(15,'Comité Interministerial de Respuesta Pandémica',' ',' '),(16,'Wuhan, China','30.5927599','114.30525'),(17,'Maipú, Chile','-33.5105866','-70.7572607'),(18,'Quellón, Chile','-43.1169327','-73.6138821'),(19,'Finlandia','61.92410999999999','25.748151'),(20,'Lima','-12.0463731','-77.042754'),(21,'Wall Street, New York, Estados Unidos','40.7077143','-74.00827869999999'),(22,'Canadá','56.130366','-106.346771'),(23,'Viña del Mar, Chile','-33.0153481','-71.55002759999999'),(24,'La Huérfana 2, Orphan: First Kill',' ',' '),(25,'Universidad de Playa Ancha, Valparaíso, Chile','-33.047238','-71.61268849999999'),(26,'Chañarcillo, Copiapó, Atacama, Chile','-27.368358','-70.3350163'),(27,'Teatro Caupolicán, Santiago, Región Metropolitana, Chile','-33.456225','-70.6494471'),(28,'España','40.46366700000001','-3.74922'),(29,'Región de Los Ríos','-40.2310217','-72.331113'),(30,'México','23.634501','-102.552784'),(31,'Hualaihué, Rolecha, Chauchil, Hornopirén, Islas Desertores','-41.9662408','-72.47121899999999'),(32,'Ford Puma Rally1 híbrido',' ',' '),(33,'Capurganá, Chocó, Colombia','8.6341284','-77.3491331'),(34,'La Araucanía','-38.948921','-72.331113'),(35,'Chile Vamos','-35.675147','-71.542969'),(36,'Antofagasta, Chile','-23.6509279','-70.39750219999999'),(37,'Coronel, Región del Biobío','-37.0340769','-73.1404838'),(38,'Phoenix','33.4483771','-112.0740373'),(39,'Microsoft, Redmond, Washington, Estados Unidos','47.6739881','-122.121512'),(40,'Ministerio del Deporte, Los Ríos, Chile','-40.2310217','-72.331113'),(41,'Santiago, Chile','-33.4488897','-70.6692655'),(42,'Ancud, Chiloé, Chile','-41.8675003','-73.8276965'),(43,'China','35.86166','104.195397'),(44,'El Alto, La Paz, Bolivia','-16.4899474','-68.2081896'),(45,'Venezuela','6.42375','-66.58973'),(46,'Bruselas','50.8476424','4.3571696'),(47,'Escuela 88, Izhevsk, Udmurtia, Rusia','56.86186009999999','53.2324285'),(48,'Sala Nicolás Copérnico, observatorio Cerro Mamalluca, Vicuña, Chile','-30.0337096','-70.7135378'),(49,'Pozo Almonte, Tarapacá, Chile','-20.2567092','-69.7860128'),(50,'Merced, esquina Manuel Tocornal, San Pedro',' ',' '),(51,'Ciudad de Panamá','8.9823792','-79.51986959999999'),(52,'Estados Unidos','37.09024','-95.712891'),(53,'EE.UU.','37.09024','-95.712891'),(54,'Provincia El Loa','-22.2799222','-68.52471489999999'),(55,'Colima, Mexico','19.2452342','-103.7240868'),(56,'Poder Legislativo',' ',' '),(57,'Quemchi, Chile','-42.1447134','-73.4780559'),(58,'ciudad de las rosas','20.6751707','-103.3473385'),(59,'Loncotoro, Llanquihue, Chile','-41.2926438','-73.2124515'),(60,'Rosario, Argentina','-32.9587022','-60.69304159999999'),(61,'Aeropuerto Internacional Jorge Chávez, Lima, Perú','-12.0230437','-77.10799759999999'),(62,'Hollywood','34.0928092','-118.3286614'),(63,'Pucón, La Araucanía, Chile','-39.2722541','-71.9776285'),(64,'Reserva Biológica Huilo Huilo, Región de Los Ríos, Chile','-40.0299532','-71.95278309999999'),(65,'Guaratiba, Río de Janeiro, Brasil','-22.9683529','-43.6216275'),(66,'exCongreso de Santiago','-33.4378527','-70.6530451'),(67,'Valdivia, Chile','-39.8176676','-73.2425892'),(68,'Calama, Chile','-22.4543923','-68.9293819'),(69,'Puente Alto, Santiago, Chile','-33.6186082','-70.5906057'),(70,'Wolfsburgo','52.4226503','10.7865461'),(71,'4 de febrero de 2014, Michelle Bachelet, Gabriel Boric, Convención Constitucional, Covid-19, Banco Central, Ministerio de Salud, Partido Republicano',' ',' '),(72,'Colegio Altazor, Concón, Chile','-32.9240634','-71.519328'),(73,'Puerto Varas','-41.3167','-72.9833'),(74,'Barcelona, España','41.3873974','2.168568'),(75,'ninguna',' ',' '),(76,'Hotel Diego de Almagro, Río Calle Calle',' ',' '),(77,'Región de Coquimbo, Chile','-30.540181','-70.81199529999999'),(78,'Peja, Kosovo','42.6592868','20.2887358'),(79,'Sence Los Ríos','-39.8100353','-73.2450114'),(80,'Convención Constitucional',' ',' '),(81,'Universidad Católica, Santiago, Chile','-33.5226641','-70.7842551'),(82,'Isla Quiriquina, región del Bío Bío','-36.625768','-73.060805'),(83,'región de Valparaíso','-32.5040172','-71.0022311'),(84,'Rancagua, Chile','-34.17013240000001','-70.7406259'),(85,'estadio Municipal de San Bernardo','-33.5944526','-70.6903189'),(86,'Avatar: The Way of Water',' ',' '),(87,'Gobierno',' ',' '),(88,'Concepción, Biobío, Chile','-36.8201352','-73.0443904'),(89,'Podemos Hablar, Telefé, Argentina','-38.416097','-63.61667199999999'),(90,'India','20.593684','78.96288'),(91,'Recoleta, Región Metropolitana, Chile','-33.4062104','-70.6336883'),(92,'Población Eleonor Roosevelt de Miraflores Alto',' ',' '),(93,'Premier League',' ',' '),(94,'cerebro',' ',' '),(95,'Valparaíso, Valparaíso, Chile','-33.047238','-71.61268849999999'),(96,'División Ventanas, Codelco, Puchuncaví, Quintero, Chile','-32.7644868','-71.4820605'),(97,'Polo Norte Magnético',' ',' '),(98,'CNN Magazine',' ',' '),(99,'Google, Estados Unidos','37.09024','-95.712891'),(100,'República Dominicana','18.735693','-70.162651'),(101,'Islas Vírgenes Británicas','18.420695','-64.639968'),(102,'Banco de Inglaterra','51.5139287','-0.0883581'),(103,'Oqueldán, Chaiguao, Tutil, Chilcol, Quellón','-43.1130406','-73.6147893'),(104,'Delegación Presidencial Provincial (DPP) de Limarí','-30.7462002','-71.0022311'),(105,'Kazán, Rusia','55.7878944','49.12332929999999'),(106,'O\'Higgins de Castro',' ',' '),(107,'Litueche, O’Higgins, Chile','-34.117272','-71.72517599999999'),(108,'Aysén, Los Lagos, Los Ríos, Ministerio de Ciencia, Tecnología, Conocimiento e Innovación, Universidad Austral de Chile','-39.8624985','-72.8079312'),(109,'provincia de Buenos Aires','-37.2017285','-59.84106969999999'),(110,'Corte de Apelaciones de Valparaíso','-33.039461','-71.630021'),(111,'Cerro Dominador, Chile','-22.7722721','-69.4796142'),(112,'Universidad de Tokio','35.7126775','139.761989'),(113,'Francia','46.227638','2.213749'),(114,'Servicio de Salud Viña del Mar Quillota','-32.7787814','-71.53148999999999'),(115,'Nueva York, Estados Unidos','40.7127753','-74.0059728'),(116,'Parlophone Records',' ',' '),(117,'CN Televisión, Mundo',' ',' '),(118,'María Eugenia Suárez, también conocida como China Suárez',' ',' '),(119,'Magallanes','-53.4428344','-72.1496817'),(120,'Downing Street, Londres, Reino Unido','51.5032437','-0.1275898'),(121,'Banco Central de Chile, Santiago, Chile','-33.4203076','-70.6584077'),(122,'Plymouth, Gran Bretaña','50.3754565','-4.1426565'),(123,'Región de O\'Higgins','-34.5755374','-71.0022311'),(124,'Parque Nacional Alerce Costero, Región de Los Ríos, Chile','-40.194219','-73.4340119'),(125,'Manchester, Reino Unido','53.4807593','-2.2426305'),(126,'Embajada de Argentina en Santiago de Chile','-33.4395206','-70.6352493'),(127,'Plaza Pública de Cadem',' ',' '),(128,'Estadio Nacional, Chile','-33.4646281','-70.6106762'),(129,'zona norte','32.5388762','-117.0455722'),(130,'Valparaíso, Chile','-33.047238','-71.61268849999999'),(131,'Teatro del Lago, Frutillar, Región de los Lagos, Chile','-41.1394411','-73.0254205'),(132,'Región de Los Lagos','-41.9197779','-72.1416132'),(133,'Organización Mundial de la Salud (OMS)',' ',' ');
/*!40000 ALTER TABLE `geocache` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-03 22:32:01