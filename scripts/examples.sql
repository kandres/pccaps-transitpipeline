CREATE SCHEMA `transit_pipeline_db` ;

CREATE TABLE `transit_pipeline_db`.`app_users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(150) NULL,
  `last_name` VARCHAR(150) NULL,
  `email` VARCHAR(150) NOT NULL,
  `created_on` DATETIME NOT NULL,
  PRIMARY KEY (`id`));


INSERT INTO app_users (first_name, last_name, email, created_on) 
VALUES ('Kyle', 'Andres', 'kyle.andres@adelear.com', now())