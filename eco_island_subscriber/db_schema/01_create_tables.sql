CREATE TABLE `threekeco`.`island` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` TINYTEXT NOT NULL,
  `created_on` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `NAME_UNIQUE` (`name` ASC));

CREATE TABLE `threekeco`.`bin` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `island_id` INT NOT NULL,
  `type` INT NOT NULL,
  `created_on` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`));

CREATE TABLE `threekeco`.`volume_sensor` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `bin_id` INT NOT NULL,
  `island_id` INT NOT NULL,
  `value` FLOAT NOT NULL,
  `measured_on` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`));

CREATE TABLE `threekeco`.`load_sensor` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `bin_id` INT NOT NULL,
  `island_id` INT NOT NULL,
  `value` FLOAT NOT NULL,
  `measured_on` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`));

CREATE TABLE `threekeco`.`infrared_sensor` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `bin_id` INT NOT NULL,
  `island_id` INT NOT NULL,
  `value` FLOAT NOT NULL,
  `measured_on` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`));