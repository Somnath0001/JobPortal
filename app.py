from flask import Flask, render_template, request;
import mysql.connector;
from register_handler import validateRegister;
from login_handler import validateUser;

app = Flask(__name__)

@app.route("/") #default route
def home(): # route function "home"
    return render_template('index.html')

# when login buttion is pressed, it will return string or html page
@app.route("/login_handler", methods=['POST'])
def login_handler():
    # get username and password from html
    email = request.form.get('email')
    password = request.form.get('password')

    # validate login
    if validateUser(email, password):
        # return f"Welcome {email}! you've logged in."
        return render_template('user_dashboard.html')
    else:
        return '<p>Login Falied. <a href="/login">login</a></p>'


@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/login")
def login():
    return render_template('index.html')

@app.route("/user_dashboard")
def user_dashboard():
    return render_template('user_dashboard.html')

@app.route("/job_seeker_profile")
def job_seeker_profile():
    return render_template('job_seeker_profile.html')

@app.route("/educational_details")
def educational_details():
    return render_template('educational_details.html')

@app.route("/skills")
def skills():
    return render_template('skills.html')

@app.route("/experience_details")
def experience_details():
    return render_template('experience_details.html')

@app.route("/register_handler", methods=['POST'])
def register_handler():
    # get all the details from the register.html
    register_as = request.form.get('register-as')
    name = request.form.get('name')
    gender = request.form.get('gender')
    dob = request.form.get('dob')
    email = request.form.get('email')
    contact_number = request.form.get('contact-number')
    password = request.form.get('password')
    profile_picture = request.files.get('profile-picture')
    sms_notification = request.form.get('sms-notification')
    email_notification = request.form.get('email-notification')

    print(register_as, name, gender, dob, email, contact_number, password, profile_picture.filename, sms_notification, email_notification)
    is_valid_register = validateRegister(register_as, name, gender, dob, email, contact_number, password, profile_picture, sms_notification, email_notification)
    if (is_valid_register):
        return "<p>Registration Successful ! <a href=\"/login\">login</a></p>"
    else:
        return f"<p>\"{email}\" is already registered. <br>Please login using the above email or register with another email.<br> <a href=\"/login\">login</a></p>"

