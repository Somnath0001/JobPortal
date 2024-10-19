from flask import Flask, render_template, request;
from register_handler import validateRegister;
from login_handler import validateUser;
from database import get_login_data, get_user_type_id, add_job_post, add_job_location, get_job_location_id, get_job_post_id, add_job_post_skill_set, add_job_post_activity, add_job_application_status, update_job_application_status, add_resume;
from job_seeker_profile_handler import handle_seeker_profile;
from educational_details_handler import handle_educational_details;
from skills_handler import handle_skills;
from experience_details_handler import handle_experience_details;
from company_profile_handler import handle_company_profile;
from user_session import get_id, set_id, clear_session;
from job_card_handler import generate_job_card_html;
from job_posting_handler import generate_job_posting_html_code;
from handle_check_application_status import generate_check_application_status_html;
from handle_manage_application_status import generate_manage_application_status_html;
from datetime import date;
from werkzeug.security import generate_password_hash;
from flask_session import Session;

app = Flask(__name__)
# Configure session settings:
# SESSION_PERMANENT: Sessions expire when the browser closes.
# SESSION_TYPE: Store sessions on the filesystem.
# Set a secret key for secure session management.
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = "your_secret_key_here"

# Initialize Flask-Session with the Flask application.
Session(app)

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
        set_id(id)
        # print(get_id())

        # Now based on user_type, let's render corresponding user dashboard page
        user_type_id = get_user_type_id(id)
        print(f"user_type_id: {user_type_id}")
        if (user_type_id == 1):
            return render_template('job_seeker_dashboard.html')
        elif (user_type_id == 2):
            return render_template('recruiter_dashboard.html')
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

# render company.html page
@app.route("/company_profile")
def company_profile():
    return render_template('company.html')

# render job_posting.html page
@app.route("/job_posting")
def job_posting():
    # return render_template('job_posting.html')
    return generate_job_posting_html_code()

# render job_card.html page
@app.route("/job_card")
def job_card():
    return generate_job_card_html()

# render check_application.html page
@app.route("/check_application_status_handler")
def check_application_status_handler():
    return generate_check_application_status_html()

# render manage_application.html page
@app.route("/manage_application")
def manage_application_status_handler():
    return generate_manage_application_status_html()

# logout
@app.route("/logout")
def logout():
    clear_session()
    print("User logout.")
    return render_template("index.html")

# render upload_resume.html page
@app.route("/upload_resume", methods=['GET', 'POST'])
def upload_resume():
    # POSt method - from client to server - When client submit the form
    if request.method == 'POST':
        # Get all the data from the page
        resume = request.files.get("resume")
        resume_data = resume.read()
        resume_filename = resume.filename
        user_account_id = get_id()
        print("User Id: ", user_account_id, "Resume Filename: ", resume_filename)
        # Add to resume table in database
        add_resume(user_account_id, resume_data, resume_filename)
        return "Resume Uploaded."
    # GET method - from server to client - When client request for the page
    else:
        return render_template("upload_resume.html")


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

    # Hash Password
    hashed_password = generate_password_hash(password)
    print(register_as, name, gender, dob, email, contact_number, hashed_password, profile_picture.filename, sms_notification, email_notification)
    # validate registration
    is_valid_register = validateRegister(register_as, name, gender, dob, email, contact_number, hashed_password, profile_picture, sms_notification, email_notification)
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
    # get data from experience_details.html
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

# return to dashboard based on user_type
@app.route("/return_to_dashboard")
def return_to_dashboard():
    # Now based on user_type, let's render corresponding user dashboard page
    id = get_id()
    user_type_id = get_user_type_id(id)
    print(f"user_type_id: {user_type_id}")
    if (user_type_id == 1):
        return render_template('job_seeker_dashboard.html')
    elif (user_type_id == 2):
        return render_template('recruiter_dashboard.html')

# handle company (create company profile) when user clicks submit button
@app.route("/company_profile_handler", methods=['POST'])
def company_profile_handler():
    # get data from company.html
    company_name = request.form.get('company-name')
    profile_description = request.form.get('profile-description')
    business_stream_id = request.form.get('business-stream')
    establishment_date = request.form.get('establishment-date')
    website_url = request.form.get('website-url')
    company_image = request.files.get('company-image')

    print(company_name, profile_description, business_stream_id, establishment_date, website_url, company_image.filename)
    # print all the data then do whatever next
    handle_company_profile(company_name, profile_description, business_stream_id, establishment_date, website_url, company_image)

    return return_to_dashboard()

# handle job_posint when user clicks submit button
@app.route("/job_posting_handler", methods=['POST'])
def job_posting_handler():
    print("job_postng_handler working")
    # get data from job_posting.html
    job_type_id = request.form.get('job-type')
    company_id = request.form.get('company-name')
    is_company_name_hidden = request.form.get('hide-company-name')
    job_description = request.form.get('job-description')
    existing_or_new_location = request.form.get('existing-or-new-location')
    if (existing_or_new_location == 'existing'):
        job_location_id = request.form.get('job-location')
        print('existing_job_location: ', job_location_id)

    elif (existing_or_new_location == 'new'):
        street_address = request.form.get('street-address')
        city = request.form.get('city')
        state = request.form.get('state')
        country = request.form.get('country')
        zip_code = request.form.get('zip-code')
        print('new_job_location: ', street_address, city, state, country, zip_code)

        # inserting data to job_location table
        add_job_location(street_address, city, state, country, zip_code)
        print('added to job_location.')
        
        # get the job_location_id from the table
        job_location_id = get_job_location_id(street_address, city, state, country, zip_code)

        print('job_location_id: ', job_location_id)
    
    experience_required = request.form.get('experience-required')
    salary_offered = request.form.get('salary-offered')
    apply_date = request.form.get('apply-date')

    print('other_job_posting_details: ', job_type_id, company_id, job_description, is_company_name_hidden, existing_or_new_location, experience_required, salary_offered, apply_date)

    posted_by_id = get_id()
    is_active = 'Y'
    created_date = date.today()

    # inserting data to job_post table
    add_job_post(posted_by_id, job_type_id, company_id, is_company_name_hidden, created_date, job_description, job_location_id, is_active, salary_offered, experience_required)
    print('added to job_post.')

    # inserting data to job_post_skill_set table
    # getting the job_post_id from the table
    job_post_id = get_job_post_id(posted_by_id, job_type_id, company_id, is_company_name_hidden, created_date, job_description, job_location_id, is_active, salary_offered, experience_required)
    print('job_post_id: ', job_post_id)

    no_of_skill_set_required = int(request.form.get('no-of-skill-set-required'))
    print('no_of_skill_set_required: ', no_of_skill_set_required)

    for i in range(no_of_skill_set_required):
        skill_set_id = request.form.get(f"required-skills-{i}")
        skill_level = request.form.get(f"required-skill-level-{i}")
        print('required_skill_set: ', skill_set_id, skill_level)
        add_job_post_skill_set(skill_set_id, job_post_id, skill_level)
        print('added to job_post_skill_set.')

    # inserting data to job_post_activity table
    add_job_post_activity(posted_by_id, job_post_id, apply_date)
    print('added to job_post_activity.')

    return """<h2 style="color:Green;">Job details added</h2>
                <a href=\"/return_to_dashboard\">Return to Dashboard</a>"""

# Apply job when 'Apply' button is pressed in job_card
@app.route("/apply", methods=["POST"])
def apply():
    user_account_id = get_id()
    job_post_id = request.form.get("job_post_id")
    print(job_post_id, user_account_id, 'pending')
    add_job_application_status(job_post_id, user_account_id, status="pending")

    return generate_job_card_html()

# Apply job_application_status when "Accept", "Reject" or "Schedule for Interview" button is clicked in "manage_applicaiton.html"
@app.route("/apply_job_application_status", methods=["POST"])
def apply_job_application_status():
    job_application_status_id = request.form.get('job_application_status_id')
    job_application_status = request.form.get('job_application_status')

    print(job_application_status_id, job_application_status)
    update_job_application_status(job_application_status_id, job_application_status)
    return generate_manage_application_status_html()


