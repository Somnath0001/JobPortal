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

def add_company_profile(company_name, profile_description, business_stream_id, establishment_date, website_url):
    db = connect_db()
    cursor = db.cursor()
    query = "INSERT INTO `company`(`company_name`, `profile_description`, `business_stream_id`, `establishment_date`, `company_website_url`) VALUES (%s,%s,%s,%s,%s)"
    cursor.execute(query, (company_name, profile_description, business_stream_id, establishment_date, website_url))
    db.commit()
    db.close()

def get_company_id(company_name):
    db = connect_db()
    cursor = db.cursor()
    query = "SELECT id FROM company WHERE company_name = %s"
    cursor.execute(query, (company_name, ))
    result = cursor.fetchone()[0]
    db.close()
    return result

def add_company_image(company_id, company_image_data):
    db = connect_db()
    cursor = db.cursor()
    query = "INSERT INTO `company_image`(`company_id`, `company_image`) VALUES (%s,%s)"
    cursor.execute(query, (company_id, company_image_data))
    db.commit()
    db.close()

def get_all_job_post():
    db = connect_db()
    cursor = db.cursor()
    query = "SELECT * FROM `job_post` LIMIT 10;"
    cursor.execute(query)
    result = cursor.fetchall()
    db.close()
    return result

def get_company(company_id):
    db = connect_db()
    cursor = db.cursor()
    query = "SELECT * FROM `company` WHERE id = %s;"
    cursor.execute(query, (company_id, ))
    result = cursor.fetchone()
    db.close()
    return result

def get_one_company_image(company_id):
    db = connect_db()
    cursor = db.cursor()
    query = "SELECT * FROM `company_image` WHERE company_id = %s LIMIT 1;"
    cursor.execute(query, (company_id, ))
    result = cursor.fetchone()
    db.close()
    return result

def get_seeker_skill_set(skill_set_id):
    db = connect_db()
    cursor = db.cursor()
    query = "SELECT * FROM `seeker_skill_set` WHERE skill_set_id = %s;"
    cursor.execute(query, (skill_set_id, ))
    result = cursor.fetchone()
    db.close()
    return result

def get_job_card_data():
    db = connect_db()
    cursor = db.cursor()
    query = """select job_description, company_name, company_image, experience_required, salary_offered, street_address, city, state, country, zip, created_date, job_post.id from job_post 
                INNER JOIN company on job_post.company_id = company.id
                INNER JOIN company_image on job_post.company_id = company_image.company_id
                INNER JOIN job_location on job_post.job_location_id = job_location.id"""
    cursor.execute(query)
    result = cursor.fetchall()
    db.close()
    return result

def add_job_post(posted_by_id, job_type_id, company_id, is_company_name_hidden, created_date, job_description, job_location_id, is_active, salary_offered, experience_required):
    db = connect_db()
    cursor = db.cursor()
    query = "INSERT INTO `job_post`(`posted_by_id`, `job_type_id`, `company_id`, `is_company_name_hidden`, `created_date`, `job_description`, `job_location_id`, `is_active`, `salary_offered`, `experience_required`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(query, (posted_by_id, job_type_id, company_id, is_company_name_hidden, created_date, job_description, job_location_id, is_active, salary_offered, experience_required))
    db.commit()
    db.close()

def add_job_location(street_address, city, state, country, zip_code):
    db = connect_db()
    cursor = db.cursor()
    query = "INSERT INTO `job_location`(`street_address`, `city`, `state`, `country`, `zip`) VALUES (%s,%s,%s,%s,%s)"
    cursor.execute(query, (street_address, city, state, country, zip_code))
    db.commit()
    db.close()

def get_job_location_id(street_address, city, state, country, zip_code):
    db = connect_db()
    cursor = db.cursor()
    query = "SELECT `id` from job_location WHERE street_address=%s AND city=%s AND state=%s AND country=%s AND zip=%s;"
    cursor.execute(query, (street_address, city, state, country, zip_code))
    result = cursor.fetchone()[0]
    db.close()
    return result

def add_job_post_skill_set(skill_set_id, job_post_id, skill_level):
    db = connect_db()
    cursor = db.cursor()
    query = "INSERT INTO `job_post_skill_set`(`skill_set_id`, `job_post_id`, `skill_level`) VALUES (%s,%s,%s);"
    cursor.execute(query, (skill_set_id, job_post_id, skill_level))
    db.commit()
    db.close()


def add_job_post_activity(user_account_id, job_post_id, apply_date):
    db = connect_db()
    cursor = db.cursor()
    query = "INSERT INTO `job_post_activity`(`user_account_id`, `job_post_id`, `apply_date`) VALUES (%s,%s,%s);"
    cursor.execute(query, (user_account_id, job_post_id, apply_date))
    db.commit()
    db.close()

def get_job_post_id(posted_by_id, job_type_id, company_id, is_company_name_hidden, created_date, job_description, job_location_id, is_active, salary_offered, experience_required):
    db = connect_db()
    cursor = db.cursor()
    query = f"SELECT `id` FROM job_post WHERE posted_by_id={posted_by_id} AND job_type_id={job_type_id} AND company_id={company_id} AND is_company_name_hidden='{is_company_name_hidden}' AND created_date='{created_date}' AND job_description='{job_description}' AND job_location_id={job_location_id} AND is_active='{is_active}' AND salary_offered={salary_offered} AND experience_required={experience_required}"
    cursor.execute(query)
    result = cursor.fetchone()[0]
    db.close()
    return result

def get_all_job_type():
    db = connect_db()
    cursor = db.cursor()
    query = "SELECT * FROM `job_type` WHERE 1"
    cursor.execute(query)
    result = cursor.fetchall()
    db.close()
    return result

def get_all_company():
    db = connect_db()
    cursor = db.cursor()
    query = "SELECT * FROM `company` WHERE 1"
    cursor.execute(query)
    result = cursor.fetchall()
    db.close()
    return result

def get_all_location():
    db = connect_db()
    cursor = db.cursor()
    query = "SELECT * FROM `job_location` WHERE 1"
    cursor.execute(query)
    result = cursor.fetchall()
    db.close()
    return result

def get_all_skill_set():
    db = connect_db()
    cursor = db.cursor()
    query = "SELECT * FROM `skill_set` WHERE 1"
    cursor.execute(query)
    result = cursor.fetchall()
    db.close()
    return result

def get_all_job_type():
    db = connect_db()
    cursor = db.cursor()
    query = "SELECT * FROM `job_type` WHERE 1"
    cursor.execute(query)
    result = cursor.fetchall()
    db.close()
    return result

def add_job_application_status(job_post_id, user_account_id, status):
    db = connect_db()
    cursor = db.cursor()
    query = f"INSERT INTO `job_application_status`(`job_post_id`, `user_account_id`, `status`) VALUES (%s,%s,%s)"
    cursor.execute(query, (job_post_id, user_account_id, status))
    db.commit()
    db.close()

def is_job_applied(job_post_id, user_account_id):
    db = connect_db()
    cursor = db.cursor()
    query = f"SELECT EXISTS (SELECT 1 FROM job_application_status WHERE job_post_id={job_post_id} AND user_account_id={user_account_id})"
    cursor.execute(query)
    result = cursor.fetchone()
    db.close()
    if (result[0] == 0):
        return False 
    else:
        return True 
    
def applied_jobs(user_account_id):
    db = connect_db()
    cursor = db.cursor()
    query = f"SELECT job_post.job_description, job_post.is_company_name_hidden, company.company_name, status, application_date FROM `job_application_status` JOIN job_post ON job_application_status.job_post_id = job_post.id JOIN company ON job_post.company_id = company.id WHERE user_account_id={user_account_id}"
    cursor.execute(query)
    result = cursor.fetchall()
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