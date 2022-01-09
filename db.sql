-- MySQL dump 10.13  Distrib 5.7.17, for macos10.12 (x86_64)
--
-- Host: localhost    Database: library
-- ------------------------------------------------------
-- Server version	5.7.20

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
-- Table structure for table `branch`
--
DROP TABLE IF EXISTS `branch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `branch`
(
    `id`          int(11) NOT NULL AUTO_INCREMENT,
    `name`        varchar(45) NOT NULL,
    `create_date` DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    UNIQUE KEY (name)

) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK
TABLES `branch` WRITE;
/*!40000 ALTER TABLE `branch` DISABLE KEYS */;
INSERT INTO `branch` (id, name)
VALUES (1, 'main branch');
/*!40000 ALTER TABLE `branch` ENABLE KEYS */;
UNLOCK
TABLES;


DROP TABLE IF EXISTS `authors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `authors`
(
    `id`          int(11) NOT NULL AUTO_INCREMENT,
    `name`        varchar(45) NOT NULL,
    `create_date` DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    UNIQUE KEY (name)

) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authors`
--
--
-- LOCK
-- TABLES `authors` WRITE;
-- /*!40000 ALTER TABLE `authors` DISABLE KEYS */;
-- INSERT INTO `authors` (id,name) VALUES (1, 'Mahmoud Ahmed'),
--        (2, 'sayed'),
--        (3, 'ali');
-- /*!40000 ALTER TABLE `authors` ENABLE KEYS */;
-- UNLOCK
-- TABLES;


--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `category`
(
    `id`          int(11) NOT NULL AUTO_INCREMENT,
    `name`        varchar(45) NOT NULL,
    `create_date` DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    UNIQUE KEY (name)

) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

-- LOCK
-- TABLES `category` WRITE;
-- /*!40000 ALTER TABLE `category` DISABLE KEYS */;
-- INSERT INTO `category`
-- VALUES (1, 'Gaming'),
--        (2, 'Drama'),
--        (3, 'Sport'),
--        (4, 'Cooking');
-- /*!40000 ALTER TABLE `category` ENABLE KEYS */;
-- UNLOCK
-- TABLES;

--
-- Table structure for table `clients`
--

DROP TABLE IF EXISTS `clients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `clients`
(
    `id`          int(11) NOT NULL AUTO_INCREMENT,
    `name`        varchar(45) NOT NULL,
    `email`       varchar(45) NOT NULL,
    `phone`       varchar(45) NOT NULL,
    `national_id` varchar(45) NOT NULL,
    `join_date`   DATE     DEFAULT NULL,
    `create_date` DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    UNIQUE KEY (name),
    UNIQUE KEY (email),
    UNIQUE KEY (phone),
    UNIQUE KEY (national_id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clients`
--

-- LOCK
-- TABLES `clients` WRITE;
-- /*!40000 ALTER TABLE `clients` DISABLE KEYS */;
-- INSERT INTO `clients`
-- VALUES (2, 'mahmoud', 'mahmoud@gmail.com', '2123213124'),
--        (3, 'ahmed', 'ahmed@gmail.com', '21232674676'),
--        (4, 'jack', 'jack22@gmail.com', '123142423'),
--        (5, 'john33', 'john33@gmail.com', '4534636346');
-- /*!40000 ALTER TABLE `clients` ENABLE KEYS */;
-- UNLOCK
-- TABLES;


--
-- Table structure for table `publisher`
--

DROP TABLE IF EXISTS `publisher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `publisher`
(
    `id`          int(11) NOT NULL AUTO_INCREMENT,
    `name`        varchar(45) NOT NULL,
    `create_date` DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    UNIQUE KEY (name)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `publisher`
--
--
-- LOCK
-- TABLES `publisher` WRITE;
-- /*!40000 ALTER TABLE `publisher` DISABLE KEYS */;
-- INSERT INTO `publisher`
-- VALUES (1, 'Ahmed Ali'),
--        (2, 'amal'),
--        (3, 'maati'),
--        (4, 'ahmed'),
--        (5, 'sayed');
-- /*!40000 ALTER TABLE `publisher` ENABLE KEYS */;
-- UNLOCK
-- TABLES;


--
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `book`
(
    `id`                int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name`              varchar(45) NOT NULL,
    `description`       varchar(100) DEFAULT NULL,
    `code`              varchar(45) NOT NULL,
    `type`              varchar(45) NOT NULL,
    `status`            varchar(45) NOT NULL,
    `check_out`         varchar(45) NOT NULL,
    `rented`            BOOL         DEFAULT false,
    `physical_position` varchar(45) NOT NULL,
    `publication_year`  varchar(45) NOT NULL,
    `added_date`        DATE        NOT NULL,
    `part_order`        int(11) DEFAULT 1,
    `category_id`       int(11) NOT NULL,
    `author_id`         int(11) NOT NULL,
    `publisher_id`      int(11) NOT NULL,
    `price`             int(11) DEFAULT 0,
    `branch_id`         int(11) NOT NULL,
    `create_date`       DATETIME     DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY (code,branch_id),
    CONSTRAINT fk_branch FOREIGN KEY (branch_id)
        REFERENCES branch (id)
        ON DELETE RESTRICT,
    CONSTRAINT fk_category FOREIGN KEY (category_id)
        REFERENCES category (id)
        ON DELETE RESTRICT,
    CONSTRAINT fk_author FOREIGN KEY (author_id)
        REFERENCES authors (id)
        ON DELETE RESTRICT,
    CONSTRAINT fk_publisher FOREIGN KEY (publisher_id)
        REFERENCES publisher (id)
        ON DELETE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book`
--

-- LOCK
-- TABLES `book` WRITE;
-- /*!40000 ALTER TABLE `book` DISABLE KEYS */;
-- INSERT INTO `book`
-- VALUES (2, 'space travel', 'space travel 3', '002', 1, 1, 1, 120, 1);
-- /*!40000 ALTER TABLE `book` ENABLE KEYS */;
-- UNLOCK
-- TABLES;

--
-- Table structure for table `dayoperations`
--

DROP TABLE IF EXISTS `dayoperations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dayoperations`
(
    `id`            int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `book_id`       int(11) NOT NULL,
    `type`          varchar(30) NOT NULL,
    `days`          int(11) DEFAULT NULL,
    `date_from`     DATE        NOT NULL,
    `client_id`     int(11) NOT NULL,
    `branch_id`     int(11) NOT NULL,
    `delay`         int(11) DEFAULT 0,
    `fees`          FLOAT(11) DEFAULT 0,
    `date_to`       DATE      DEFAULT NULL,
    `retrieve_date` DATE      DEFAULT NULL,
    `create_date`   DATETIME  DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_book FOREIGN KEY (book_id)
        REFERENCES book (id)
        ON DELETE CASCADE,
    CONSTRAINT fk_client FOREIGN KEY (client_id)
        REFERENCES clients (id)
        ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dayoperations`
--

-- LOCK
-- TABLES `dayoperations` WRITE;
-- /*!40000 ALTER TABLE `dayoperations` DISABLE KEYS */;
-- INSERT INTO `dayoperations`
-- VALUES (1, 1, 'Retrieve', 4, '2019-01-08', 1, NULL),
--        (2, 1, 'Retrieve', 4, '2019-01-09', 1, NULL);
-- /*!40000 ALTER TABLE `dayoperations` ENABLE KEYS */;
-- UNLOCK
-- TABLES;


--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users`
(
    `id`          int(11) NOT NULL AUTO_INCREMENT,
    `name`        varchar(45) NOT NULL,
    `email`       varchar(45) NOT NULL,
    `password`    varchar(45) NOT NULL,
    `client_id`   int(11) DEFAULT NULL,
    `add_user`    BOOL     DEFAULT false,
    `add_book`    BOOL     DEFAULT false,
    `remove_user` BOOL     DEFAULT false,
    `remove_book` BOOL     DEFAULT false,
    `edit_user`   BOOL     DEFAULT false,
    `edit_book`   BOOL     DEFAULT false,
    `items`       BOOL     DEFAULT false,
    `clients`     BOOL     DEFAULT false,
    `dashboard`   BOOL     DEFAULT false,
    `history`     BOOL     DEFAULT false,
    `reports`     BOOL     DEFAULT false,
    `settings`    BOOL     DEFAULT false,
    `create_date` DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    CONSTRAINT fk_client_user FOREIGN KEY (client_id)
        REFERENCES clients (id)
        ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK
TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO users (name, email, password)
VALUES ('admin', 'admin', 'admin');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK
TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-01-09  1:00:55
