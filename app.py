from flask import Flask, render_template, request;
from register_handler import validateRegister;
from login_handler import validateUser;
from user_session import get_id, update_id;
from database import get_login_data;
from job_seeker_profile_handler import handle_seeker_profile;
from educational_details_handler import handle_educational_details;
from skills_handler import handle_skills;
from experience_details_handler import handle_experience_details

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

        # add user_session
        id = get_login_data(email)[0]
        update_id(id)
        # print(get_id())

        return render_template('user_dashboard.html')
    else:
        return '<p>Login Falied. <a href="/login">login</a></p>'


# render register.html page
@app.route("/register")
def register():
    return render_template('register.html')

# render index.html page
@app.route("/login")
def login():
    return render_template('index.html')

# render user_dashboard.html page
@app.route("/user_dashboard")
def user_dashboard():
    return render_template('user_dashboard.html')

# render job_seeker_profile.html page
@app.route("/job_seeker_profile")
def job_seeker_profile():
    return render_template('job_seeker_profile.html')

# render educational_details.html page
@app.route("/educational_details")
def educational_details():
    return render_template('educational_details.html')

# render skills.html page
@app.route("/skills")
def skills():
    return render_template('skills.html')

# render experience_details.html page
@app.route("/experience_details")
def experience_details():
    return render_template('experience_details.html')

# handle registration when user clicks submit button
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
    # validate registration
    is_valid_register = validateRegister(register_as, name, gender, dob, email, contact_number, password, profile_picture, sms_notification, email_notification)
    if (is_valid_register):
        return "<p>Registration Successful ! <a href=\"/login\">login</a></p>"
    else:
        return f"<p>\"{email}\" is already registered. <br>Please login using the above email or register with another email.<br> <a href=\"/login\">login</a></p>"

# handle job_seeker_profile when user clicks submit button
@app.route("/job_seeker_profile_handler", methods=['POST'])
def job_seeker_profile_builder():
    # get data from job_seeker_profile.html
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    current_salary = request.form.get('current_salary')
    salary_frequency =request.form.get('salary_frequency')
    currency = request.form.get('currency')

    print(first_name, last_name, current_salary, salary_frequency, currency)
    handle_seeker_profile(first_name, last_name, current_salary, salary_frequency, currency)
    return render_template('educational_details.html')

# handle educational_details when user clicks submit button
@app.route("/educational_details_handler", methods=["POST"])
def educational_details_handler():
    # get data from educational_details.html page
    certificate_name = request.form.get('certificate-name')
    major = request.form.get('major')
    institure_name = request.form.get('institute-name')
    degree_start_date = request.form.get('degree-start-date')
    degree_completion_date = request.form.get('degree-completion-date')
    percentage_obtained = request.form.get('percentage-obtained')
    cgpa = request.form.get('cgpa')

    print(certificate_name, major, institure_name, degree_start_date, degree_completion_date, percentage_obtained, cgpa)
    handle_educational_details(certificate_name, major, institure_name, degree_start_date, degree_completion_date, percentage_obtained, cgpa)
    return render_template('skills.html')

# handle skills when user clicks submit button
@app.route("/skills_handler", methods=['POST'])
def skills_handler():
    skill_name = request.form.get('skill-name')
    skill_level = request.form.get('skill-level')

    print(skill_name, skill_level)
    handle_skills(skill_name, skill_level)
    return render_template('skills.html')

# handle experience_details when user clicks submit button
@app.route("/experience_details_handler", methods=['POST'])
def experience_details_handler():
    company_name = request.form.get('company-name')
    currently_working = request.form.get('currently-working')
    job_title = request.form.get('job-title')
    start_date = request.form.get('start-date')
    end_date = request.form.get('end-date')
    description = request.form.get('description')
    city = request.form.get('city')
    state = request.form.get('state')
    country = request.form.get('country')
    business_stream_id = request.form.get('business-stream')

    print(company_name, currently_working, job_title, start_date, end_date, description, city, state, country, business_stream_id)
    handle_experience_details(company_name, currently_working, job_title, start_date, end_date, description, city, state, country, business_stream_id)

    return "Experience added."