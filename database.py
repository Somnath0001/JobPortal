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