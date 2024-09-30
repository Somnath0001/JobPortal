import mysql.connector
from config import DB_CONFIG
from datetime import date

def connect_db():
    return mysql.connector.connect(**DB_CONFIG)

def get_login_data(email):
    db = connect_db()
    cursor = db.cursor()
    query = "SELECT * FROM user_account WHERE email = %s"
    cursor.execute(query, (email, ))
    result = cursor.fetchone()
    db.close()
    return result

def add_user(user_type_id, email, password, name, dob, gender, is_active, contact_number, sms_notification, email_notification, profile_picture_data, registration_date):
    db = connect_db()
    cursor = db.cursor()
    query = "INSERT INTO `user_account`(`user_type_id`, `email`, `password`, `name`, `date_of_birth`, `gender`, `is_active`, `contact_number`, `sms_notification_active`, `email_notification_active`, `user_image`, `registration_date`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (user_type_id, email, password, name, dob, gender, is_active, contact_number, sms_notification, email_notification, profile_picture_data, registration_date))
    db.commit()
    db.close()

def add_seeker_profile(id, first_name, last_name, current_salary, salary_frequency, currency):
    db = connect_db()
    cursor = db.cursor()
    query = "INSERT INTO `seeker_profile`(`user_account_id`, `first_name`, `last_name`, `current_salary`, `is_anually_monthly`, `currency`) VALUES (%s,%s,%s,%s,%s,%s)"
    cursor.execute(query, (id, first_name, last_name, current_salary, salary_frequency, currency))
    db.commit()
    db.close()

def add_educational_details(id, certificate_name, major, institure_name, degree_start_date, degree_completion_date, percentage_obtained, cgpa):
    db = connect_db()
    cursor = db.cursor()
    query = "INSERT INTO `education_detail`(`user_account_id`, `certificate_degree_name`, `major`, `institute_university_name`, `starting_date`, `completion_date`, `percentage`, `cgpa`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(query, (id, certificate_name, major, institure_name, degree_start_date, degree_completion_date, percentage_obtained, cgpa))
    db.commit()
    db.close()

def add_seeker_skill_set(id, skill_set_id, skill_level):
    db = connect_db()
    cursor = db.cursor()
    query = "INSERT INTO `seeker_skill_set`(`user_account_id`, `skill_set_id`, `skill_level`) VALUES (%s,%s,%s)"
    cursor.execute(query, (id, skill_set_id, skill_level))
    db.commit()
    db.close()

def add_skill_set(id, skill_set_name):
    db = connect_db()
    cursor = db.cursor()
    query = "INSERT INTO `skill_set`(`id`, `skill_set_name`) VALUES (%s,%s);"
    cursor.execute(query, (id, skill_set_name))
    db.commit()
    db.close()

def get_skill_set_id(skill_set_name):
    db = connect_db()
    cursor = db.cursor()
    query = "SELECT id FROM `skill_set` WHERE skill_set_name = %s;"
    cursor.execute(query, (skill_set_name, ))
    result = cursor.fetchone()[0]
    db.close()
    return result

def add_experience_details(id, company_name, currently_working, job_title, start_date, end_date, description, city, state, country, business_stream_id):
    db = connect_db()
    cursor = db.cursor()
    query = "INSERT INTO `experience_detail`(`user_account_id`, `is_current_job`, `start_date`, `end_date`, `job_title`, `company_name`, `job_location_city`, `job_location_state`, `job_location_country`, `description`, `business_stream_id`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(query, (id, currently_working, start_date, end_date, job_title, company_name, city, state, country, description, business_stream_id))
    db.commit()
    db.close()

def get_user_type_id(user_account_id):
    db = connect_db()
    cursor = db.cursor()
    query = "SELECT user_type_id FROM user_account WHERE id = %s"
    cursor.execute(query, (user_account_id, ))
    result = cursor.fetchone()[0]
    db.close()
    return result


def get_cars():
    db = connect_db()
    cursor = db.cursor()
    query = "SELECT * FROM cars"
    cursor.execute(query)
    results = cursor.fetchall()
    db.close()
    return results

def add_car(car_data):
    db = connect_db()
    cursor = db.cursor()
    query = "INSERT INTO cars (company, name, make, model) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, tuple(car_data.values()))
    db.commit()
    db.close()

def search_car(name):
    db = connect_db()
    cursor = db.cursor()
    query = "SELECT * FROM cars WHERE name LIKE %s"
    cursor.execute(query, (f"%{name}%",))
    results = cursor.fetchall()
    db.close()
    return results