from user_session import get_id;
from database import add_experience_details;

def handle_experience_details(company_name, currently_working, job_title, start_date, end_date, description, city, state, country, business_stream_id):
    # get id from user_session
    id = get_id()

    # insert into DB
    add_experience_details(id, company_name, currently_working, job_title, start_date, end_date, description, city, state, country, business_stream_id)

# in experience_details.html - add one field called business stream (0 - IT, 1 - Logistics, 2 - Bank, 3 - E-commerce)
# modify in app.py - experience_details_handler - it should take business stream

