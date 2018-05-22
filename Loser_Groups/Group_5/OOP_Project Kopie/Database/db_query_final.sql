-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema oopproject
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema oopproject
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `oopproject` DEFAULT CHARACTER SET latin1 ;
USE `oopproject` ;

-- -----------------------------------------------------
-- Table `oopproject`.`categories`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `oopproject`.`categories` (
  `category_id` INT(11) NOT NULL AUTO_INCREMENT,
  `category_name` VARCHAR(100) NOT NULL,
  `category_plain` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`category_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `oopproject`.`requests`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `oopproject`.`requests` (
  `request_id` INT(11) NOT NULL AUTO_INCREMENT,
  `updatetime` DATETIME NOT NULL,
  `latitude` VARCHAR(100) NOT NULL,
  `longitude` VARCHAR(100) NOT NULL,
  `categories_category_id` INT(11) NOT NULL,
  PRIMARY KEY (`request_id`),
  INDEX `fk_requests_categories1_idx` (`categories_category_id` ASC),
  CONSTRAINT `fk_requests_categories1`
    FOREIGN KEY (`categories_category_id`)
    REFERENCES `oopproject`.`categories` (`category_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `oopproject`.`venue`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `oopproject`.`venue` (
  `venue_id` INT(11) NOT NULL AUTO_INCREMENT,
  `yelp_id` VARCHAR(100) NOT NULL,
  `address` VARCHAR(100) NULL DEFAULT NULL,
  `city` VARCHAR(100) NULL DEFAULT NULL,
  `latitude` VARCHAR(100) NULL DEFAULT NULL,
  `longitude` VARCHAR(100) NULL DEFAULT NULL,
  `name` VARCHAR(100) NULL DEFAULT NULL,
  `rating` FLOAT NULL DEFAULT NULL,
  `url` VARCHAR(300) NULL DEFAULT NULL,
  `phone` VARCHAR(100) NULL DEFAULT NULL,
  `distance` FLOAT NULL DEFAULT NULL,
  `requests_request_id` INT(11) NOT NULL,
  PRIMARY KEY (`venue_id`),
  INDEX `fk_venue_requests_idx` (`requests_request_id` ASC),
  CONSTRAINT `fk_venue_requests`
    FOREIGN KEY (`requests_request_id`)
    REFERENCES `oopproject`.`requests` (`request_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `oopproject`.`weather`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `oopproject`.`weather` (
  `weather_ID` INT(11) NOT NULL AUTO_INCREMENT,
  `curr_summary` VARCHAR(100) NULL DEFAULT NULL,
  `curr_temp` VARCHAR(100) NULL DEFAULT NULL,
  `curr_humidity` VARCHAR(100) NULL DEFAULT NULL,
  `curr_uvindex` VARCHAR(100) NULL DEFAULT NULL,
  `day0_summary` VARCHAR(100) NULL DEFAULT NULL,
  `day0_temp_high` VARCHAR(100) NULL DEFAULT NULL,
  `day0_temp_low` VARCHAR(100) NULL DEFAULT NULL,
  `day0_humidity` VARCHAR(100) NULL DEFAULT NULL,
  `day0_uvindex` VARCHAR(100) NULL DEFAULT NULL,
  `day1_summary` VARCHAR(100) NULL DEFAULT NULL,
  `day1_temp_high` VARCHAR(100) NULL DEFAULT NULL,
  `day1_temp_low` VARCHAR(100) NULL DEFAULT NULL,
  `day1_humidity` VARCHAR(100) NULL DEFAULT NULL,
  `day1_uvindex` VARCHAR(100) NULL DEFAULT NULL,
  `day2_summary` VARCHAR(100) NULL DEFAULT NULL,
  `day2_temp_high` VARCHAR(100) NULL DEFAULT NULL,
  `day2_temp_low` VARCHAR(100) NULL DEFAULT NULL,
  `day2_humidity` VARCHAR(100) NULL DEFAULT NULL,
  `day2_uvindex` VARCHAR(100) NULL DEFAULT NULL,
  `week_summary` VARCHAR(200) NULL DEFAULT NULL,
  `requests_request_id` INT(11) NOT NULL,
  PRIMARY KEY (`weather_ID`),
  INDEX `fk_weather_requests1_idx` (`requests_request_id` ASC),
  CONSTRAINT `fk_weather_requests1`
    FOREIGN KEY (`requests_request_id`)
    REFERENCES `oopproject`.`requests` (`request_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;