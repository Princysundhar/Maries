/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.12-log : Database - maries
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`maries` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `maries`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=latin1;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add login',7,'add_login'),(26,'Can change login',7,'change_login'),(27,'Can delete login',7,'delete_login'),(28,'Can view login',7,'view_login'),(29,'Can add request_service',8,'add_request_service'),(30,'Can change request_service',8,'change_request_service'),(31,'Can delete request_service',8,'delete_request_service'),(32,'Can view request_service',8,'view_request_service'),(33,'Can add service',9,'add_service'),(34,'Can change service',9,'change_service'),(35,'Can delete service',9,'delete_service'),(36,'Can view service',9,'view_service'),(37,'Can add service_provider',10,'add_service_provider'),(38,'Can change service_provider',10,'change_service_provider'),(39,'Can delete service_provider',10,'delete_service_provider'),(40,'Can view service_provider',10,'view_service_provider'),(41,'Can add service_type',11,'add_service_type'),(42,'Can change service_type',11,'change_service_type'),(43,'Can delete service_type',11,'delete_service_type'),(44,'Can view service_type',11,'view_service_type'),(45,'Can add user',12,'add_user'),(46,'Can change user',12,'change_user'),(47,'Can delete user',12,'delete_user'),(48,'Can view user',12,'view_user'),(49,'Can add subcatogary',13,'add_subcatogary'),(50,'Can change subcatogary',13,'change_subcatogary'),(51,'Can delete subcatogary',13,'delete_subcatogary'),(52,'Can view subcatogary',13,'view_subcatogary'),(53,'Can add service_cart',14,'add_service_cart'),(54,'Can change service_cart',14,'change_service_cart'),(55,'Can delete service_cart',14,'delete_service_cart'),(56,'Can view service_cart',14,'view_service_cart'),(57,'Can add request_sub',15,'add_request_sub'),(58,'Can change request_sub',15,'change_request_sub'),(59,'Can delete request_sub',15,'delete_request_sub'),(60,'Can view request_sub',15,'view_request_sub'),(61,'Can add rating',16,'add_rating'),(62,'Can change rating',16,'change_rating'),(63,'Can delete rating',16,'delete_rating'),(64,'Can view rating',16,'view_rating'),(65,'Can add complaint',17,'add_complaint'),(66,'Can change complaint',17,'change_complaint'),(67,'Can delete complaint',17,'delete_complaint'),(68,'Can view complaint',17,'view_complaint'),(69,'Can add chat',18,'add_chat'),(70,'Can change chat',18,'change_chat'),(71,'Can delete chat',18,'delete_chat'),(72,'Can view chat',18,'view_chat'),(73,'Can add bank',19,'add_bank'),(74,'Can change bank',19,'change_bank'),(75,'Can delete bank',19,'delete_bank'),(76,'Can view bank',19,'view_bank');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(19,'maries_app','bank'),(18,'maries_app','chat'),(17,'maries_app','complaint'),(7,'maries_app','login'),(16,'maries_app','rating'),(8,'maries_app','request_service'),(15,'maries_app','request_sub'),(9,'maries_app','service'),(14,'maries_app','service_cart'),(10,'maries_app','service_provider'),(11,'maries_app','service_type'),(13,'maries_app','subcatogary'),(12,'maries_app','user'),(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (1,'contenttypes','0001_initial','2023-11-09 18:32:02.148832'),(2,'auth','0001_initial','2023-11-09 18:32:03.272008'),(3,'admin','0001_initial','2023-11-09 18:32:03.505362'),(4,'admin','0002_logentry_remove_auto_add','2023-11-09 18:32:03.511580'),(5,'admin','0003_logentry_add_action_flag_choices','2023-11-09 18:32:03.519808'),(6,'contenttypes','0002_remove_content_type_name','2023-11-09 18:32:03.682849'),(7,'auth','0002_alter_permission_name_max_length','2023-11-09 18:32:03.768224'),(8,'auth','0003_alter_user_email_max_length','2023-11-09 18:32:03.859967'),(9,'auth','0004_alter_user_username_opts','2023-11-09 18:32:03.867962'),(10,'auth','0005_alter_user_last_login_null','2023-11-09 18:32:03.942866'),(11,'auth','0006_require_contenttypes_0002','2023-11-09 18:32:03.942866'),(12,'auth','0007_alter_validators_add_error_messages','2023-11-09 18:32:03.951164'),(13,'auth','0008_alter_user_username_max_length','2023-11-09 18:32:04.045447'),(14,'auth','0009_alter_user_last_name_max_length','2023-11-09 18:32:04.133418'),(15,'auth','0010_alter_group_name_max_length','2023-11-09 18:32:04.223920'),(16,'auth','0011_update_proxy_permissions','2023-11-09 18:32:04.231635'),(17,'auth','0012_alter_user_first_name_max_length','2023-11-09 18:32:04.317648'),(18,'maries_app','0001_initial','2023-11-09 18:32:06.746909'),(19,'sessions','0001_initial','2023-11-09 18:32:06.843703'),(20,'maries_app','0002_alter_subcatogary_service_type','2023-11-10 17:22:03.858951'),(21,'maries_app','0003_alter_rating_service_provider','2023-12-09 06:46:22.362163');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('v1ds56arnyzg9dsre5upsmo0wxsmc70s','eyJsaWQiOjV9:1rN5PK:5KOI6E3sp78WxNs2mmQkXQuyHGLcWDO8QyE3SI_syn4','2024-01-23 06:16:14.990147');

/*Table structure for table `maries_app_bank` */

DROP TABLE IF EXISTS `maries_app_bank`;

CREATE TABLE `maries_app_bank` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `bank_name` varchar(100) NOT NULL,
  `IFSC_code` varchar(100) NOT NULL,
  `account_no` varchar(100) NOT NULL,
  `amount` varchar(100) NOT NULL,
  `LOGIN_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `maries_app_bank_LOGIN_id_3301656e_fk_maries_app_login_id` (`LOGIN_id`),
  CONSTRAINT `maries_app_bank_LOGIN_id_3301656e_fk_maries_app_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `maries_app_login` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `maries_app_bank` */

/*Table structure for table `maries_app_chat` */

DROP TABLE IF EXISTS `maries_app_chat`;

CREATE TABLE `maries_app_chat` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `chat` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `SERVICE_PROVIDER_id` bigint(20) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `maries_app_chat_SERVICE_PROVIDER_id_6c39fd54_fk_maries_ap` (`SERVICE_PROVIDER_id`),
  KEY `maries_app_chat_USER_id_c295afde_fk_maries_app_user_id` (`USER_id`),
  CONSTRAINT `maries_app_chat_SERVICE_PROVIDER_id_6c39fd54_fk_maries_ap` FOREIGN KEY (`SERVICE_PROVIDER_id`) REFERENCES `maries_app_service_provider` (`id`),
  CONSTRAINT `maries_app_chat_USER_id_c295afde_fk_maries_app_user_id` FOREIGN KEY (`USER_id`) REFERENCES `maries_app_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `maries_app_chat` */

/*Table structure for table `maries_app_complaint` */

DROP TABLE IF EXISTS `maries_app_complaint`;

CREATE TABLE `maries_app_complaint` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `complaint` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `reply` varchar(100) NOT NULL,
  `reply_date` varchar(100) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `maries_app_complaint_USER_id_efa356ef_fk_maries_app_user_id` (`USER_id`),
  CONSTRAINT `maries_app_complaint_USER_id_efa356ef_fk_maries_app_user_id` FOREIGN KEY (`USER_id`) REFERENCES `maries_app_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `maries_app_complaint` */

insert  into `maries_app_complaint`(`id`,`complaint`,`date`,`reply`,`reply_date`,`USER_id`) values (1,'jdcb','vhb','jkjkl','20231209-114709',1);

/*Table structure for table `maries_app_login` */

DROP TABLE IF EXISTS `maries_app_login`;

CREATE TABLE `maries_app_login` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `usertype` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `maries_app_login` */

insert  into `maries_app_login`(`id`,`username`,`password`,`usertype`) values (1,'admin','12','admin'),(2,'admin','123','user'),(3,'yu','456','user'),(4,'a','1','servpro'),(5,'bnm','n','servpro');

/*Table structure for table `maries_app_rating` */

DROP TABLE IF EXISTS `maries_app_rating`;

CREATE TABLE `maries_app_rating` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `rate` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `SERVICE_PROVIDER_id` bigint(20) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `maries_app_rating_USER_id_64de5f7d_fk_maries_app_user_id` (`USER_id`),
  KEY `maries_app_rating_SERVICE_PROVIDER_id_522b098f_fk_maries_ap` (`SERVICE_PROVIDER_id`),
  CONSTRAINT `maries_app_rating_SERVICE_PROVIDER_id_522b098f_fk_maries_ap` FOREIGN KEY (`SERVICE_PROVIDER_id`) REFERENCES `maries_app_service_provider` (`id`),
  CONSTRAINT `maries_app_rating_USER_id_64de5f7d_fk_maries_app_user_id` FOREIGN KEY (`USER_id`) REFERENCES `maries_app_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `maries_app_rating` */

insert  into `maries_app_rating`(`id`,`rate`,`date`,`SERVICE_PROVIDER_id`,`USER_id`) values (1,'bgj','fthj',1,1);

/*Table structure for table `maries_app_request_service` */

DROP TABLE IF EXISTS `maries_app_request_service`;

CREATE TABLE `maries_app_request_service` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `payment_status` varchar(100) NOT NULL,
  `payment_date` varchar(100) NOT NULL,
  `amount` varchar(100) NOT NULL,
  `SERVICE_PROVIDER_id` bigint(20) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `maries_app_request_s_SERVICE_PROVIDER_id_3051065b_fk_maries_ap` (`SERVICE_PROVIDER_id`),
  KEY `maries_app_request_s_USER_id_60c3d233_fk_maries_ap` (`USER_id`),
  CONSTRAINT `maries_app_request_s_SERVICE_PROVIDER_id_3051065b_fk_maries_ap` FOREIGN KEY (`SERVICE_PROVIDER_id`) REFERENCES `maries_app_service_provider` (`id`),
  CONSTRAINT `maries_app_request_s_USER_id_60c3d233_fk_maries_ap` FOREIGN KEY (`USER_id`) REFERENCES `maries_app_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `maries_app_request_service` */

insert  into `maries_app_request_service`(`id`,`date`,`status`,`payment_status`,`payment_date`,`amount`,`SERVICE_PROVIDER_id`,`USER_id`) values (1,'890','approve','fghj','789','789)',1,1);

/*Table structure for table `maries_app_request_sub` */

DROP TABLE IF EXISTS `maries_app_request_sub`;

CREATE TABLE `maries_app_request_sub` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `request_date` varchar(100) NOT NULL,
  `REQUEST_id` bigint(20) NOT NULL,
  `SERVICE_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `maries_app_request_s_REQUEST_id_91998293_fk_maries_ap` (`REQUEST_id`),
  KEY `maries_app_request_s_SERVICE_id_5b910245_fk_maries_ap` (`SERVICE_id`),
  CONSTRAINT `maries_app_request_s_REQUEST_id_91998293_fk_maries_ap` FOREIGN KEY (`REQUEST_id`) REFERENCES `maries_app_request_service` (`id`),
  CONSTRAINT `maries_app_request_s_SERVICE_id_5b910245_fk_maries_ap` FOREIGN KEY (`SERVICE_id`) REFERENCES `maries_app_service` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `maries_app_request_sub` */

/*Table structure for table `maries_app_service` */

DROP TABLE IF EXISTS `maries_app_service`;

CREATE TABLE `maries_app_service` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `descrption` varchar(100) NOT NULL,
  `price` varchar(100) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `SERVICE_PROVIDER_id` bigint(20) NOT NULL,
  `SUBCATEGORY_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `maries_app_service_SERVICE_PROVIDER_id_fbcb11bf_fk_maries_ap` (`SERVICE_PROVIDER_id`),
  KEY `maries_app_service_SUBCATEGORY_id_19d3a9c9_fk_maries_ap` (`SUBCATEGORY_id`),
  CONSTRAINT `maries_app_service_SERVICE_PROVIDER_id_fbcb11bf_fk_maries_ap` FOREIGN KEY (`SERVICE_PROVIDER_id`) REFERENCES `maries_app_service_provider` (`id`),
  CONSTRAINT `maries_app_service_SUBCATEGORY_id_19d3a9c9_fk_maries_ap` FOREIGN KEY (`SUBCATEGORY_id`) REFERENCES `maries_app_subcatogary` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `maries_app_service` */

insert  into `maries_app_service`(`id`,`descrption`,`price`,`photo`,`SERVICE_PROVIDER_id`,`SUBCATEGORY_id`) values (13,'ghjtju76y','2344454','/static/images/231223-130353.jpg',1,6),(15,'ghjtju76y','2344454','/static/images/231223-131252.jpg',1,5);

/*Table structure for table `maries_app_service_cart` */

DROP TABLE IF EXISTS `maries_app_service_cart`;

CREATE TABLE `maries_app_service_cart` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `request_date` varchar(100) NOT NULL,
  `SERVICE_id` bigint(20) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `maries_app_service_c_SERVICE_id_520df0e5_fk_maries_ap` (`SERVICE_id`),
  KEY `maries_app_service_cart_USER_id_bc322131_fk_maries_app_user_id` (`USER_id`),
  CONSTRAINT `maries_app_service_cart_USER_id_bc322131_fk_maries_app_user_id` FOREIGN KEY (`USER_id`) REFERENCES `maries_app_user` (`id`),
  CONSTRAINT `maries_app_service_c_SERVICE_id_520df0e5_fk_maries_ap` FOREIGN KEY (`SERVICE_id`) REFERENCES `maries_app_service` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `maries_app_service_cart` */

/*Table structure for table `maries_app_service_provider` */

DROP TABLE IF EXISTS `maries_app_service_provider`;

CREATE TABLE `maries_app_service_provider` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `contact` varchar(100) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `latitude` varchar(100) NOT NULL,
  `longitude` varchar(100) NOT NULL,
  `LOGIN_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `maries_app_service_p_LOGIN_id_cc58adf1_fk_maries_ap` (`LOGIN_id`),
  CONSTRAINT `maries_app_service_p_LOGIN_id_cc58adf1_fk_maries_ap` FOREIGN KEY (`LOGIN_id`) REFERENCES `maries_app_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `maries_app_service_provider` */

insert  into `maries_app_service_provider`(`id`,`name`,`place`,`post`,`email`,`contact`,`photo`,`latitude`,`longitude`,`LOGIN_id`) values (1,'gygygy','gygg','yyy','yyy','y7yy','/static/images/231223-122057.jpg','11.868506','75.3632065',5),(2,'sree','ghj','ghj','','nm','/static/images/231219-120917.jpg','bnm','nm',1);

/*Table structure for table `maries_app_service_type` */

DROP TABLE IF EXISTS `maries_app_service_type`;

CREATE TABLE `maries_app_service_type` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `maries_app_service_type` */

insert  into `maries_app_service_type`(`id`,`type`) values (6,'service_type object (None)'),(7,'outfit'),(8,'outfit'),(11,'1'),(12,'1'),(13,'2'),(14,'1');

/*Table structure for table `maries_app_subcatogary` */

DROP TABLE IF EXISTS `maries_app_subcatogary`;

CREATE TABLE `maries_app_subcatogary` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `subcatogary_name` varchar(100) NOT NULL,
  `SERVICE_TYPE_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `maries_app_subcatoga_SERVICE_TYPE_id_61ebfc82_fk_maries_ap` (`SERVICE_TYPE_id`),
  CONSTRAINT `maries_app_subcatoga_SERVICE_TYPE_id_61ebfc82_fk_maries_ap` FOREIGN KEY (`SERVICE_TYPE_id`) REFERENCES `maries_app_service_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `maries_app_subcatogary` */

insert  into `maries_app_subcatogary`(`id`,`subcatogary_name`,`SERVICE_TYPE_id`) values (5,'saree',8),(6,'saree',8),(11,'pant',7),(14,'top',8),(15,'',6);

/*Table structure for table `maries_app_user` */

DROP TABLE IF EXISTS `maries_app_user`;

CREATE TABLE `maries_app_user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `pin` varchar(100) NOT NULL,
  `contact` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `LOGIN_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `maries_app_user_LOGIN_id_4bad8507_fk_maries_app_login_id` (`LOGIN_id`),
  CONSTRAINT `maries_app_user_LOGIN_id_4bad8507_fk_maries_app_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `maries_app_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `maries_app_user` */

insert  into `maries_app_user`(`id`,`name`,`gender`,`place`,`post`,`pin`,`contact`,`email`,`photo`,`LOGIN_id`) values (1,'hc ','ijni','vvgb','kjb','tt','hhd','ddd','ggg',3);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
