-- database: job_portal
CREATE DATABASE job_portal;

-- create user_type table:
CREATE TABLE `job_portal`.`user_type` (`id` INT NOT NULL , `user_type_name` VARCHAR(20) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;

-- create user_account table:
CREATE TABLE `job_portal`.`user_account` (`id` INT NOT NULL , `user_type_id` INT NOT NULL , `email` VARCHAR(255) NOT NULL , `password` VARCHAR(255) NOT NULL , `date_of_birth` DATE NOT NULL , `gender` CHAR(1) NOT NULL , `is_active` CHAR(1) NOT NULL , `contact_number` INT(10) NOT NULL , `sms_notification_active` CHAR(1) NOT NULL , `email_notification_active` CHAR(1) NOT NULL , `user_image` BLOB , `registration_date` DATE NOT NULL , PRIMARY KEY (`id`) , FOREIGN KEY (user_type_id) REFERENCES user_type(id)) ENGINE = InnoDB;

-- create user_log table:
CREATE TABLE `job_portal`.`user_log` (`user_account_id` INT NOT NULL , `last_login_date` DATE NOT NULL , `last_job_apply_date` DATE , PRIMARY KEY (`user_account_id`) , FOREIGN KEY (user_account_id) REFERENCES user_account(id)) ENGINE = InnoDB;

-- create business_stream table:
CREATE TABLE `job_portal`.`business_stream` (`id` INT NOT NULL , `business_stream_name` VARCHAR(100) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;

-- create company table:
CREATE TABLE `job_portal`.`company` (`id` INT NOT NULL , `company_name` VARCHAR(100) NOT NULL , `profile_description` VARCHAR(1000) NOT NULL , `business_stream_id` INT NOT NULL , `establishment_date` DATE NOT NULL , `company_website_url` VARCHAR(200) NOT NULL , PRIMARY KEY (`id`) , FOREIGN KEY (business_stream_id) REFERENCES business_stream(id)) ENGINE = InnoDB;

-- create company_image table:
CREATE TABLE `job_portal`.`company_image` (`id` INT NOT NULL , `company_id` INT NOT NULL , `company_image` BLOB NOT NULL , PRIMARY KEY (`id`) , FOREIGN KEY (company_id) REFERENCES company(id)) ENGINE = InnoDB;

-- create seeker_profile table:
CREATE TABLE `job_portal`.`seeker_profile` (`user_account_id` INT NOT NULL , `first_name` VARCHAR(50) NOT NULL , `last_name` VARCHAR(50) NOT NULL , `current_salary` INT , `is_anually_monthly` CHAR(1) , `currency` VARCHAR(50) , PRIMARY KEY (`user_account_id`) , FOREIGN KEY (user_account_id) REFERENCES user_account(id)) ENGINE = InnoDB;

-- create education_detail table:
CREATE TABLE `job_portal`.`education_detail` (`user_account_id` INT NOT NULL , `certificate_degree_name` VARCHAR(50) NOT NULL , `major` VARCHAR(50) NOT NULL , `institute_university_name` VARCHAR(50) NOT NULL , `starting_date` DATE NOT NULL , `completion_date` DATE , `percentage` INT , `cgpa` INT , PRIMARY KEY (`user_account_id`, `certificate_degree_name`, `major`), FOREIGN KEY (user_account_id) REFERENCES user_account(id)) ENGINE = InnoDB;

-- create experience_detail table:
CREATE TABLE `job_portal`.`experience_details` (`user_account_id` INT NOT NULL , `is_current_job` CHAR(1) NOT NULL , `start_date` DATE NOT NULL , `end_date` DATE NOT NULL , `job_title` VARCHAR(50) NOT NULL , `company_name` VARCHAR(100) NOT NULL , `job_location_city` VARCHAR(50) NOT NULL , `job_location_state` VARCHAR(50) NOT NULL , `job_location_country` VARCHAR(50) NOT NULL , `description` VARCHAR(4000) NOT NULL , PRIMARY KEY (`user_account_id`, `start_date`, `end_date`) , FOREIGN KEY (user_account_id) REFERENCES user_account(id)) ENGINE = InnoDB;

-- create skill_set table:
CREATE TABLE `job_portal`.`skill_set` (`id` INT NOT NULL , `skill_set_name` VARCHAR(50) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;

-- create seeker_skill_set table:
CREATE TABLE `job_portal`.`seeker_skill_set` (`user_account_id` INT NOT NULL , `skill_set_id` INT NOT NULL , `skill_level` INT NOT NULL , PRIMARY KEY (`user_account_id`, `skill_set_id`) , FOREIGN KEY (user_account_id) REFERENCES user_account(id) , FOREIGN KEY (skill_set_id) REFERENCES skill_set(id)) ENGINE = InnoDB;

-- create job_type table:
CREATE TABLE `job_portal`.`job_type` (`id` INT NOT NULL , `job_type` VARCHAR(20) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;

-- create job_location table:
CREATE TABLE `job_portal`.`job_location` (`id` INT NOT NULL , `street_address` VARCHAR(100) NOT NULL , `city` VARCHAR(50) NOT NULL , `state` VARCHAR(50) NOT NULL , `country` VARCHAR(50) NOT NULL , `zip` VARCHAR(50) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;

-- create job_post table:
CREATE TABLE `job_portal`.`job_post` (`id` INT NOT NULL , `posted_by_id` INT NOT NULL , `job_type_id` INT NOT NULL , `company_id` INT NOT NULL , `is_company_name_hidden` CHAR(1) NOT NULL , `created_date` DATE NOT NULL , `job_description` VARCHAR(500) NOT NULL , `job_location_id` INT NOT NULL , `is_active` CHAR(1) NOT NULL , PRIMARY KEY (`id`) , FOREIGN KEY (posted_by_id) REFERENCES user_account(id) , FOREIGN KEY (job_type_id) REFERENCES job_type(id) , FOREIGN KEY (company_id) REFERENCES company(id) , FOREIGN KEY (job_location_id) REFERENCES job_location(id)) ENGINE = InnoDB;

-- create job_post_skill_set table:
CREATE TABLE `job_portal`.`job_post_skill_set` (`skill_set_id` INT NOT NULL , `job_post_id` INT NOT NULL , `skill_level` INT NOT NULL , PRIMARY KEY (`skill_set_id`, `job_post_id`) , FOREIGN KEY (skill_set_id) REFERENCES skill_set(id) , FOREIGN KEY (job_post_id) REFERENCES job_post(id)) ENGINE = InnoDB;

-- create job_post_activity table:
CREATE TABLE `job_portal`.`job_post_activity` (`user_account_id` INT NOT NULL , `job_post_id` INT NOT NULL , `apply_date` DATE NOT NULL , PRIMARY KEY (`user_account_id`, `job_post_id`) , FOREIGN KEY (user_account_id) REFERENCES user_account(id) , FOREIGN KEY (job_post_id) REFERENCES job_post(id)) ENGINE = InnoDB;


-- Modifications


-- add salary_offered & experience_required tables in job_post table:
ALTER TABLE job_post
ADD COLUMN salary_offered INT,
ADD COLUMN experience_required INT;

-- add name column in user_account table:
ALTER TABLE user_account 
ADD COLUMN name VARCHAR(50) NOT NULL AFTER password;

-- change contact_number from INT type to VARCHAR type
ALTER TABLE `user_account` CHANGE `contact_number` `contact_number` VARCHAR(10) NOT NULL;


-- adding AUTO_INCREMENT in tables
-- ALTER TABLE <table name> AUTO_INCREMENT = 1;
ALTER TABLE user_type CHANGE id id INT NOT NULL AUTO_INCREMENT;
ALTER TABLE user_account CHANGE id id INT NOT NULL AUTO_INCREMENT;
ALTER TABLE business_stream CHANGE id id INT NOT NULL AUTO_INCREMENT;
ALTER TABLE company CHANGE id id INT NOT NULL AUTO_INCREMENT;
ALTER TABLE skill_set AUTO_INCREMENT = 1;
ALTER TABLE job_type CHANGE id id INT NOT NULL AUTO_INCREMENT;
ALTER TABLE job_location CHANGE id id INT NOT NULL AUTO_INCREMENT;
ALTER TABLE job_post CHANGE id id INT NOT NULL AUTO_INCREMENT;
ALTER TABLE company_image CHANGE id id INT NOT NULL AUTO_INCREMENT;

-- check table structure
DESCRIBE user_account;


/*
Suggestions:
    1. Consider adding a table for storing resumes, with a foreign key referencing the user_account table.
    2. You may want to add a table for storing job application statuses (e.g., pending, rejected, accepted).
    3. For the education_detail table, consider adding a separate table for storing institutions and universities to avoid data redundancy.
    4. In the experience_details table, you may want to add a column for storing the job's industry or sector.
*/

-- adding business_stream_id in experience_details table which will be foreign key to business_stream table:
-- Add business_stream_id column
ALTER TABLE experience_details
ADD COLUMN business_stream_id INT NOT NULL;

-- Add foreign key constraint
ALTER TABLE experience_details
ADD CONSTRAINT fk_business_stream_id
FOREIGN KEY (business_stream_id)
REFERENCES business_stream (id);

-- renamed experience_details to experience_detail
RENAME TABLE `job_portal`.`experience_details` TO `job_portal`.`experience_detail`;

/*
1. Resume Table: resume
Purpose: Store resumes uploaded by job seekers.
Columns:
    id (primary key)
    user_account_id (foreign key referencing user_account)
    resume_file (blob or varchar to store file path)
    file_name (resume file name)
    upload_date (timestamp)
*/
CREATE TABLE `job_portal`.`resume` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_account_id` INT NOT NULL,
  `resume_file` BLOB,
  `file_name` VARCHAR(255) NOT NULL,
  `upload_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_account_id`) REFERENCES `user_account` (`id`)
) ENGINE = InnoDB;


/*
2. Job Application Status Table: job_application_status
Purpose: Store the status of job applications.
Columns:
    id (primary key)
    job_post_id (foreign key referencing job_post)
    user_account_id (foreign key referencing user_account)
    status (enum: 'pending', 'rejected', 'accepted', etc.)
    application_date (timestamp)
*/
CREATE TABLE `job_portal`.`job_application_status` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `job_post_id` INT NOT NULL,
  `user_account_id` INT NOT NULL,
  `status` ENUM('pending', 'rejected', 'accepted', 'interviewScheduled') NOT NULL,
  `application_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`job_post_id`) REFERENCES `job_post` (`id`),
  FOREIGN KEY (`user_account_id`) REFERENCES `user_account` (`id`)
) ENGINE = InnoDB;


-- insert to user_type
INSERT INTO `user_type`(`id`, `user_type_name`) VALUES ('1','job_seeker');
INSERT INTO `user_type`(`id`, `user_type_name`) VALUES ('2','recruiter');

-- dummy values in user_account table
INSERT INTO `job_portal`.`user_account` 
(`id`, `user_type_id`, `email`, `password`, `name`, `date_of_birth`, `gender`, `is_active`, `contact_number`, `sms_notification_active`, `email_notification_active`, `registration_date`)
VALUES

(1, 1, 'john.doe@example.com', 'password123', 'John Doe', '1990-02-12', 'M', 'Y', 9876543210, 'Y', 'Y', '2022-01-01'),
(2, 2, 'jane.smith@example.com', 'password456', 'Jane Smith', '1992-08-25', 'F', 'Y', 7418529630, 'N', 'Y', '2022-02-15'),
(3, 1, 'bob.johnson@example.com', 'password789', 'Bob Johnson', '1985-04-01', 'M', 'Y', 9638527410, 'Y', 'N', '2022-03-20'),
(4, 2, 'alice.williams@example.com', 'password012', 'Alice Williams', '1995-10-12', 'F', 'Y', 8527419630, 'N', 'Y', '2022-04-10'),
(5, 1, 'mike.davis@example.com', 'password345', 'Mike Davis', '1980-06-15', 'M', 'Y', 7418529630, 'Y', 'Y', '2022-05-25'),
(6, 2, 'emma.taylor@example.com', 'password678', 'Emma Taylor', '1991-03-22', 'F', 'Y', 9638527410, 'N', 'N', '2022-06-01'),
(7, 1, 'david.lee@example.com', 'password901', 'David Lee', '1988-09-18', 'M', 'Y', 8527419630, 'Y', 'Y', '2022-07-12'),
(8, 2, 'sophia.patel@example.com', 'password234', 'Sophia Patel', '1993-11-25', 'F', 'Y', 7418529630, 'N', 'Y', '2022-08-20'),
(9, 1, 'peter.brown@example.com', 'password567', 'Peter Brown', '1975-01-01', 'M', 'Y', 9638527410, 'Y', 'N', '2022-09-15'),
(10, 2, 'olivia.martin@example.com', 'password890', 'Olivia Martin', '1996-05-10', 'F', 'Y', 8527419630, 'N', 'Y', '2022-10-01');


-- dummy for user_account table
INSERT INTO `user_account`(`user_type_id`, `email`, `password`, `name`, `date_of_birth`, `gender`, `is_active`, `contact_number`, `sms_notification_active`, `email_notification_active`, `user_image`, `registration_date`) VALUES (1,'som@email.com','som@pass', 'Somnath Maity', '2024-09-28','M','Y','9234343434','Y','Y','','2024-09-28')

-- dummy data insert for seeker_profile table
INSERT INTO `seeker_profile`(`user_account_id`, `first_name`, `last_name`, `current_salary`, `is_anually_monthly`, `currency`) VALUES (5,'Somnath','Maity',500000,'A','INR')

-- populating skill_set table
INSERT INTO `skill_set`(`id`, `skill_set_name`) VALUES (0,'Java');
INSERT INTO `skill_set`(`id`, `skill_set_name`) VALUES (1,'Python');
INSERT INTO `skill_set`(`id`, `skill_set_name`) VALUES (2,'C++');
INSERT INTO `skill_set`(`id`, `skill_set_name`) VALUES (3,'JavaScript');
INSERT INTO `skill_set`(`id`, `skill_set_name`) VALUES (4,'Other');

-- get skill_set_id from skill_set_name
SELECT id FROM `skill_set` WHERE skill_set_name = "C++";

-- inserting data to business_stream table
INSERT INTO `business_stream`(`id`, `business_stream_name`) VALUES ('0','IT');
INSERT INTO `business_stream`(`id`, `business_stream_name`) VALUES ('1','Logistics');
INSERT INTO `business_stream`(`id`, `business_stream_name`) VALUES ('2','Bank');
INSERT INTO `business_stream`(`id`, `business_stream_name`) VALUES ('3','E-commerce');

-- dummy values for job_location
INSERT INTO job_portal.job_location (id, street_address, city, state, country, zip)
VALUES
(1, '123 Main St', 'New York City', 'New York', 'USA', '10001'),
(2, '456 Elm St', 'Los Angeles', 'California', 'USA', '90001'),
(3, '789 Oak St', 'Chicago', 'Illinois', 'USA', '60601'),
(4, '321 Maple St', 'Houston', 'Texas', 'USA', '77001'),
(5, '901 Broadway', 'Seattle', 'Washington', 'USA', '98101'),
(6, '345 Bloor St', 'Toronto', 'Ontario', 'Canada', 'M5S 1S2'),
(7, '678 Collins St', 'Melbourne', 'Victoria', 'Australia', '3000'),
(8, '234 Regent St', 'London', 'England', 'UK', 'W1B 3EG'),
(9, '567 Champs-Élysées', 'Paris', 'Île-de-France', 'France', '75008'),
(10, '890 Apollolaan', 'Amsterdam', 'North Holland', 'Netherlands', '1017 BA');

-- insert values to job_type
INSERT INTO `job_type`(`job_type`) VALUES ('Permanent');
INSERT INTO `job_type`(`job_type`) VALUES ('Temporary');
INSERT INTO `job_type`(`job_type`) VALUES ('Work From Home');
INSERT INTO `job_type`(`job_type`) VALUES ('In Office');
INSERT INTO `job_type`(`job_type`) VALUES ('Permanent Work From Home');
INSERT INTO `job_type`(`job_type`) VALUES ('Temporary In Office');

-- Inserting dummy values into job_post table

INSERT INTO job_portal.job_post 
(posted_by_id, job_type_id, company_id, is_company_name_hidden, 
created_date, job_description, job_location_id, is_active, salary_offered, experience_required)
VALUES
(11, 1, 1, 'N', '2022-01-01', 'Software Engineer', 1, 'Y', 80000, 2),
(12, 2, 1, 'Y', '2022-02-01', 'Data Scientist', 3, 'Y', 120000, 5),
(13, 3, 3, 'N', '2022-03-01', 'Marketing Manager', 5, 'Y', 90000, 3),
(11, 4, 4, 'Y', '2022-04-01', 'Product Manager', 2, 'Y', 100000, 4),
(12, 1, 1, 'N', '2022-05-01', 'Full Stack Developer', 4, 'Y', 70000, 2),
(13, 2, 3, 'Y', '2022-06-01', 'DevOps Engineer', 6, 'Y', 110000, 5),
(11, 3, 3, 'N', '2022-07-01', 'UX Designer', 7, 'Y', 80000, 3),
(12, 4, 4, 'Y', '2022-08-01', 'Business Analyst', 8, 'Y', 90000, 4),
(13, 1, 1, 'N', '2022-09-01', 'Frontend Developer', 9, 'Y', 60000, 2),
(11, 2, 4, 'Y', '2022-10-01', 'Backend Developer', 10, 'Y', 100000, 5);

-- dummy values for job_post_skill_set table
INSERT INTO job_post_skill_set (skill_set_id, job_post_id, skill_level)
VALUES
(0, 11, 2),
(1, 11, 3),
(2, 11, 1),
(3, 11, 4),
(4, 11, 2),
(0, 12, 1),
(1, 12, 4),
(2, 12, 3),
(3, 12, 2),
(4, 12, 1),
(0, 13, 4),
(1, 13, 2),
(2, 13, 1),
(3, 13, 3),
(4, 13, 4),
(0, 14, 3),
(1, 14, 1),
(2, 14, 4),
(3, 14, 2),
(4, 15, 1),
(0, 16, 2);

-- get job_card details from job_post table and others
version 1

select * from job_post 
INNER JOIN company on job_post.company_id = company.id
INNER JOIN company_image on job_post.company_id = company_image.company_id
INNER JOIN job_location on job_post.job_location_id = job_location.id
INNER JOIN job_post_skill_set on job_post.id = job_post_skill_set.job_post_id;

version 2

select * from job_post 
INNER JOIN company on job_post.company_id = company.id
INNER JOIN company_image on job_post.company_id = company_image.company_id
INNER JOIN job_location on job_post.job_location_id = job_location.id

version 3

select job_description, company_name, company_image, experience_required, salary_offered, street_address, city, state, country, zip, created_date from job_post 
INNER JOIN company on job_post.company_id = company.id
INNER JOIN company_image on job_post.company_id = company_image.company_id
INNER JOIN job_location on job_post.job_location_id = job_location.id


