from user_session import get_id;
from database import add_educational_details;

def handle_educational_details(certificate_name, major, institure_name, degree_start_date, degree_completion_date, percentage_obtained, cgpa):
    id = get_id()

    # insert data into DB
    print(id, certificate_name, major, institure_name, degree_start_date, degree_completion_date, percentage_obtained, cgpa)
    add_educational_details(id, certificate_name, major, institure_name, degree_start_date, degree_completion_date, percentage_obtained, cgpa)