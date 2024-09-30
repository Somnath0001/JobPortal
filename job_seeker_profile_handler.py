from database import add_seeker_profile;
from user_session import get_id;

def handle_seeker_profile(first_name, last_name, current_salary, salary_frequency, currency):
    # get the user_account_id from user_session
    id = get_id()

    if (salary_frequency == 'Annually'):
        salary_frequency = 'A'
    elif (salary_frequency == 'Monthly'):
        salary_frequency = 'M'

    # insert seeker profile details
    print(id, first_name, last_name, current_salary, salary_frequency, currency)
    add_seeker_profile(id, first_name, last_name, current_salary, salary_frequency, currency)
