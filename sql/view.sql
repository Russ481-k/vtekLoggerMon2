-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: 192.168.1.45    Database: logger
-- ------------------------------------------------------
-- Server version	5.5.5-10.6.12-MariaDB-0ubuntu0.22.04.1

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
-- Temporary view structure for view `areafrom`
--

DROP TABLE IF EXISTS `areafrom`;
/*!50001 DROP VIEW IF EXISTS `areafrom`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `areafrom` AS SELECT
 1 AS `d043`,
 1 AS `count(*)`,
 1 AS `percent`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `dayservice`
--

DROP TABLE IF EXISTS `dayservice`;
/*!50001 DROP VIEW IF EXISTS `dayservice`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `dayservice` AS SELECT
 1 AS `d015`,
 1 AS `count(*)`,
 1 AS `percent`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `hiin`
--

DROP TABLE IF EXISTS `hiin`;
/*!50001 DROP VIEW IF EXISTS `hiin`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `hiin` AS SELECT
 1 AS `d009`,
 1 AS `count(*)`,
 1 AS `percent`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `hiout`
--

DROP TABLE IF EXISTS `hiout`;
/*!50001 DROP VIEW IF EXISTS `hiout`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `hiout` AS SELECT
 1 AS `d008`,
 1 AS `count(*)`,
 1 AS `percent`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `hourcount`
--

DROP TABLE IF EXISTS `hourcount`;
/*!50001 DROP VIEW IF EXISTS `hourcount`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `hourcount` AS SELECT
 1 AS `d002`,
 1 AS `count(*)`,
 1 AS `percent`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `inoutT`
--

DROP TABLE IF EXISTS `inoutT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inoutT` (
  `d001` varchar(100) DEFAULT NULL,
  `d002` datetime DEFAULT NULL,
  `d003` varchar(100) DEFAULT NULL,
  `d004` varchar(100) DEFAULT NULL,
  `d005` varchar(100) DEFAULT NULL,
  `d006` varchar(100) DEFAULT NULL,
  `d007` varchar(100) DEFAULT NULL,
  `d008` varchar(100) DEFAULT NULL,
  `d009` varchar(100) DEFAULT NULL,
  `d010` varchar(100) DEFAULT NULL,
  `d011` varchar(100) DEFAULT NULL,
  `d012` varchar(100) DEFAULT NULL,
  `d013` varchar(100) DEFAULT NULL,
  `d014` varchar(100) DEFAULT NULL,
  `d015` varchar(1000) DEFAULT NULL,
  `d016` varchar(100) DEFAULT NULL,
  `d017` varchar(100) DEFAULT NULL,
  `d018` varchar(100) DEFAULT NULL,
  `d019` varchar(100) DEFAULT NULL,
  `d020` varchar(100) DEFAULT NULL,
  `d021` varchar(100) DEFAULT NULL,
  `d022` varchar(100) DEFAULT NULL,
  `d023` varchar(100) DEFAULT NULL,
  `d024` varchar(100) DEFAULT NULL,
  `d025` varchar(100) DEFAULT NULL,
  `d026` varchar(100) DEFAULT NULL,
  `d027` varchar(100) DEFAULT NULL,
  `d028` varchar(100) DEFAULT NULL,
  `d029` varchar(100) DEFAULT NULL,
  `d030` varchar(100) DEFAULT NULL,
  `d031` varchar(100) DEFAULT NULL,
  `d032` varchar(100) DEFAULT NULL,
  `d033` varchar(100) DEFAULT NULL,
  `d034` varchar(100) DEFAULT NULL,
  `d035` varchar(100) DEFAULT NULL,
  `d036` varchar(100) DEFAULT NULL,
  `d037` varchar(100) DEFAULT NULL,
  `d038` varchar(100) DEFAULT NULL,
  `d039` varchar(100) DEFAULT NULL,
  `d040` varchar(100) DEFAULT NULL,
  `d041` varchar(100) DEFAULT NULL,
  `d042` varchar(100) DEFAULT NULL,
  `d043` varchar(100) DEFAULT NULL,
  `d044` varchar(100) DEFAULT NULL,
  `d045` varchar(100) DEFAULT NULL,
  `d046` varchar(100) DEFAULT NULL,
  `d047` varchar(100) DEFAULT NULL,
  `d048` varchar(100) DEFAULT NULL,
  `d049` varchar(100) DEFAULT NULL,
  `d050` varchar(100) DEFAULT NULL,
  `d051` varchar(100) DEFAULT NULL,
  `d052` varchar(500) DEFAULT NULL,
  `d053` varchar(100) DEFAULT NULL,
  `d054` varchar(100) DEFAULT NULL,
  `d055` varchar(100) DEFAULT NULL,
  `d056` varchar(100) DEFAULT NULL,
  `d057` varchar(100) DEFAULT NULL,
  `d058` varchar(100) DEFAULT NULL,
  `d059` varchar(100) DEFAULT NULL,
  `d060` varchar(100) DEFAULT NULL,
  `d061` varchar(100) DEFAULT NULL,
  `d062` varchar(100) DEFAULT NULL,
  `d063` varchar(100) DEFAULT NULL,
  `d064` varchar(100) DEFAULT NULL,
  `d065` varchar(100) DEFAULT NULL,
  `d066` varchar(100) DEFAULT NULL,
  `d067` varchar(100) DEFAULT NULL,
  `d068` varchar(100) DEFAULT NULL,
  `d069` varchar(100) DEFAULT NULL,
  `d070` varchar(100) DEFAULT NULL,
  `d071` varchar(100) DEFAULT NULL,
  `d072` varchar(100) DEFAULT NULL,
  `d073` varchar(100) DEFAULT NULL,
  `d074` varchar(100) DEFAULT NULL,
  `d075` varchar(100) DEFAULT NULL,
  `d076` varchar(100) DEFAULT NULL,
  `d077` varchar(100) DEFAULT NULL,
  `d078` varchar(100) DEFAULT NULL,
  `d079` varchar(100) DEFAULT NULL,
  `d080` varchar(100) DEFAULT NULL,
  `d081` varchar(100) DEFAULT NULL,
  `d082` varchar(100) DEFAULT NULL,
  `d083` varchar(100) DEFAULT NULL,
  `d084` varchar(100) DEFAULT NULL,
  `d085` varchar(100) DEFAULT NULL,
  `d086` varchar(100) DEFAULT NULL,
  `d087` varchar(100) DEFAULT NULL,
  `d088` varchar(100) DEFAULT NULL,
  `d089` varchar(100) DEFAULT NULL,
  `d090` varchar(100) DEFAULT NULL,
  `d091` varchar(100) DEFAULT NULL,
  `d092` varchar(100) DEFAULT NULL,
  `d093` varchar(100) DEFAULT NULL,
  `d094` varchar(100) DEFAULT NULL,
  `d095` varchar(100) DEFAULT NULL,
  `d096` varchar(100) DEFAULT NULL,
  `d097` varchar(100) DEFAULT NULL,
  `d098` varchar(100) DEFAULT NULL,
  `d099` varchar(100) DEFAULT NULL,
  `d100` varchar(100) DEFAULT NULL,
  `d101` varchar(100) DEFAULT NULL,
  `d102` varchar(100) DEFAULT NULL,
  `d103` varchar(100) DEFAULT NULL,
  `d104` varchar(100) DEFAULT NULL,
  `d105` varchar(100) DEFAULT NULL,
  `d106` varchar(100) DEFAULT NULL,
  `d107` varchar(100) DEFAULT NULL,
  `d108` varchar(100) DEFAULT NULL,
  `d109` varchar(100) DEFAULT NULL,
  `d110` varchar(100) DEFAULT NULL,
  `d111` varchar(100) DEFAULT NULL,
  `d112` varchar(100) DEFAULT NULL,
  `d113` varchar(100) DEFAULT NULL,
  `d114` varchar(100) DEFAULT NULL,
  `d115` varchar(100) DEFAULT NULL,
  `d116` varchar(100) DEFAULT NULL,
  `d117` varchar(100) DEFAULT NULL,
  `d118` varchar(100) DEFAULT NULL,
  `d119` varchar(100) DEFAULT NULL,
  `d120` varchar(100) DEFAULT NULL,
  `d121` varchar(100) DEFAULT NULL,
  `d122` varchar(100) DEFAULT NULL,
  `d123` varchar(100) DEFAULT NULL,
  `d124` varchar(100) DEFAULT NULL,
  `d125` varchar(100) DEFAULT NULL,
  `d126` varchar(100) DEFAULT NULL,
  `d127` varchar(100) DEFAULT NULL,
  `d128` varchar(100) DEFAULT NULL,
  `d129` varchar(100) DEFAULT NULL,
  `d130` varchar(100) DEFAULT NULL,
  KEY `inoutT_d002_IDX` (`d002`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `menuCustom`
--

DROP TABLE IF EXISTS `menuCustom`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `menuCustom` (
  `customNo` int(11) NOT NULL AUTO_INCREMENT COMMENT '설정번호',
  `userNo` int(11) DEFAULT NULL COMMENT '사용자',
  `menuNo` varchar(10) DEFAULT NULL COMMENT '메뉴번호',
  `activeMenu` varchar(10) DEFAULT NULL COMMENT '컬럼명',
  `menuTitle` varchar(100) DEFAULT NULL COMMENT '컬럼타이틀',
  `useYN` varchar(5) DEFAULT NULL COMMENT '사용유무',
  `sortNo` int(11) DEFAULT 100 COMMENT '배치순번',
  `sortCust` int(11) DEFAULT NULL COMMENT '순번설정',
  `attrib` varchar(15) DEFAULT '10000' COMMENT '추가설정',
  PRIMARY KEY (`customNo`)
) ENGINE=InnoDB AUTO_INCREMENT=2200 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary view structure for view `monthcount`
--

DROP TABLE IF EXISTS `monthcount`;
/*!50001 DROP VIEW IF EXISTS `monthcount`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `monthcount` AS SELECT
 1 AS `d002`,
 1 AS `count(*)`,
 1 AS `percent`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `service`
--

DROP TABLE IF EXISTS `service`;
/*!50001 DROP VIEW IF EXISTS `service`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `service` AS SELECT
 1 AS `d015`,
 1 AS `count(*)`,
 1 AS `percent`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `userAccount`
--

DROP TABLE IF EXISTS `userAccount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `userAccount` (
  `userNo` int(11) NOT NULL AUTO_INCREMENT,
  `userId` varchar(100) DEFAULT NULL,
  `userName` varchar(100) DEFAULT NULL,
  `userPasswd` varchar(100) DEFAULT NULL,
  `userEmail` varchar(100) DEFAULT NULL,
  `userKey` varchar(100) DEFAULT NULL,
  `userRole` varchar(10) DEFAULT NULL,
  `attrib` varchar(15) NOT NULL DEFAULT '10000',
  PRIMARY KEY (`userNo`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping routines for database 'logger'
--

--
-- Final view structure for view `areafrom`
--

/*!50001 DROP VIEW IF EXISTS `areafrom`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb3 */;
/*!50001 SET character_set_results     = utf8mb3 */;
/*!50001 SET collation_connection      = utf8mb3_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `areafrom` AS select `inoutT`.`d043` AS `d043`,count(0) AS `count(*)`,count(0) * 100.0 / sum(count(0)) over () AS `percent` from `inoutT` where `inoutT`.`d002` between current_timestamp() - interval 1 hour and current_timestamp() group by `inoutT`.`d043` order by count(0) * 100.0 / sum(count(0)) over () desc */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `dayservice`
--

/*!50001 DROP VIEW IF EXISTS `dayservice`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`swcore`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `dayservice` AS select `inoutT`.`d015` AS `d015`,count(0) AS `count(*)`,count(0) * 100.0 / sum(count(0)) over () AS `percent` from `inoutT` where `inoutT`.`d002` between current_timestamp() - interval 1 hour and current_timestamp() group by `inoutT`.`d015` order by count(0) * 100.0 / sum(count(0)) over () desc */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `hiin`
--

/*!50001 DROP VIEW IF EXISTS `hiin`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb3 */;
/*!50001 SET character_set_results     = utf8mb3 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`swcore`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `hiin` AS select 1 AS `d009`,1 AS `count(*)`,1 AS `percent` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `hiout`
--

/*!50001 DROP VIEW IF EXISTS `hiout`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb3 */;
/*!50001 SET character_set_results     = utf8mb3 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`swcore`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `hiout` AS select 1 AS `d008`,1 AS `count(*)`,1 AS `percent` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `hourcount`
--

/*!50001 DROP VIEW IF EXISTS `hourcount`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`swcore`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `hourcount` AS select date_format(`inoutT`.`d002`,'%Y-%m-%d %h:00:00') AS `d002`,count(0) AS `count(*)`,count(0) * 100.0 / sum(count(0)) over () AS `percent` from `inoutT` where `inoutT`.`d002` between current_timestamp() - interval 1 day and current_timestamp() group by date_format(`inoutT`.`d002`,'%Y-%m-%d %h') order by count(0) * 100.0 / sum(count(0)) over () desc */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `monthcount`
--

/*!50001 DROP VIEW IF EXISTS `monthcount`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`swcore`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `monthcount` AS select date_format(`inoutT`.`d002`,'%Y-%m-%d') AS `d002`,count(0) AS `count(*)`,count(0) * 100.0 / sum(count(0)) over () AS `percent` from `inoutT` where `inoutT`.`d002` between current_timestamp() - interval 1 month and current_timestamp() group by date_format(`inoutT`.`d002`,'%Y-%m-%d') order by count(0) * 100.0 / sum(count(0)) over () desc */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `service`
--

/*!50001 DROP VIEW IF EXISTS `service`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`swcore`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `service` AS select `inoutT`.`d015` AS `d015`,count(0) AS `count(*)`,count(0) * 100.0 / sum(count(0)) over () AS `percent` from `inoutT` where `inoutT`.`d002` between current_timestamp() - interval 1 hour and current_timestamp() group by `inoutT`.`d015` order by count(0) * 100.0 / sum(count(0)) over () desc */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-02 14:48:39
