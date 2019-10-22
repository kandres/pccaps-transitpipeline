--You can ignore this, it is just the initital database creation for MYSQL
CREATE SCHEMA `transit_pipeline_db` ;

--Here we are telling the database 'transit_pipeline_db' to create a table 'app_users', a database can have many tables in it. Each row (ex: id, first_name, etc..) below is a column definition. A table can have many columns
CREATE TABLE `transit_pipeline_db`.`app_users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(150) NULL,
  `last_name` VARCHAR(150) NULL,
  `email` VARCHAR(150) NOT NULL,
  `created_on` DATETIME NOT NULL,
  PRIMARY KEY (`id`));


-- Now that our table is created above, we can insert data into that table by telling it what data to put in each column
INSERT INTO app_users (first_name, last_name, email, created_on) 
VALUES ('Kyle', 'Andres', 'kyle.andres@adelear.com', now())