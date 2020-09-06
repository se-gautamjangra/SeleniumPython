
CREATE DATABASE `pythondbtest` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `pythondbtest`;
CREATE TABLE `departments` (
  `id` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*
-- Query: SELECT * FROM companydb.departments
LIMIT 0, 1000

-- Date: 2020-08-22 18:57
*/
INSERT INTO `departments` (`id`,`name`) VALUES (101,'Human Resources');
INSERT INTO `departments` (`id`,`name`) VALUES (102,'Inventory');
INSERT INTO `departments` (`id`,`name`) VALUES (103,'Accounts and Finance');
INSERT INTO `departments` (`id`,`name`) VALUES (104,'Sales and marketing');
INSERT INTO `departments` (`id`,`name`) VALUES (105,'Research and development');
INSERT INTO `departments` (`id`,`name`) VALUES (106,'Learning and development');
INSERT INTO `departments` (`id`,`name`) VALUES (107,'IT service');
INSERT INTO `departments` (`id`,`name`) VALUES (108,'Product development');
INSERT INTO `departments` (`id`,`name`) VALUES (109,'Admin department');
INSERT INTO `departments` (`id`,`name`) VALUES (110,'Security and transport');

CREATE TABLE `employees` (
  `emp_no` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `date_of_birth` date NOT NULL,
  `gender` enum('M','F') NOT NULL,
  `hire_date` date NOT NULL,
  PRIMARY KEY (`emp_no`)
) ENGINE=InnoDB AUTO_INCREMENT=1114 DEFAULT CHARSET=latin1;

/*
-- Query: select * from companydb.employees
LIMIT 0, 1000

-- Date: 2020-08-22 18:49
*/
INSERT INTO `employees` (`first_name`,`last_name`,`date_of_birth`,`gender`,`hire_date`) VALUES ('John','Smith','1985-07-15','M','2010-01-10');
INSERT INTO `employees` (`first_name`,`last_name`,`date_of_birth`,`gender`,`hire_date`) VALUES ('Steve','Clark','1987-01-10','M','2013-11-05');
INSERT INTO `employees` (`first_name`,`last_name`,`date_of_birth`,`gender`,`hire_date`) VALUES ('Paris','Kate','1990-09-20','F','2015-01-26');
INSERT INTO `employees` (`first_name`,`last_name`,`date_of_birth`,`gender`,`hire_date`) VALUES ('Betty','Jennifer','1991-02-25','F','2015-04-16');
INSERT INTO `employees` (`first_name`,`last_name`,`date_of_birth`,`gender`,`hire_date`) VALUES ('Brad','Jordan','1990-05-25','M','2016-02-01');
INSERT INTO `employees` (`first_name`,`last_name`,`date_of_birth`,`gender`,`hire_date`) VALUES ('Michael','Smith','1989-09-25','M','2013-10-01');
INSERT INTO `employees` (`first_name`,`last_name`,`date_of_birth`,`gender`,`hire_date`) VALUES ('Susane','Perry','1991-08-21','F','2013-11-21');
INSERT INTO `employees` (`first_name`,`last_name`,`date_of_birth`,`gender`,`hire_date`) VALUES ('Sam','Rogers','1988-10-15','M','2012-10-11');
INSERT INTO `employees` (`first_name`,`last_name`,`date_of_birth`,`gender`,`hire_date`) VALUES ('Shelly','White','1987-09-11','F','2010-10-10');
INSERT INTO `employees` (`first_name`,`last_name`,`date_of_birth`,`gender`,`hire_date`) VALUES ('Shelly','White','1987-09-11','F','2010-10-10');
INSERT INTO `employees` (`first_name`,`last_name`,`date_of_birth`,`gender`,`hire_date`) VALUES ('Shelly','White','1987-09-11','F','2010-10-10');
INSERT INTO `employees` (`first_name`,`last_name`,`date_of_birth`,`gender`,`hire_date`) VALUES ('Shelly','White','1987-09-11','F','2010-10-10');
INSERT INTO `employees` (`first_name`,`last_name`,`date_of_birth`,`gender`,`hire_date`) VALUES ('Shelly','White','1987-09-11','F','2010-10-10');
INSERT INTO `employees` (`first_name`,`last_name`,`date_of_birth`,`gender`,`hire_date`) VALUES ('Shelly','White','1987-09-11','F','2010-10-10');
