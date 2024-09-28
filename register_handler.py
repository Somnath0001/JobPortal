from datetime import date;
from database import get_login_data, add_user;

def validateRegister(register_as, name, gender, dob, email, contact_number, password, profile_picture, sms_notification, email_notification):
    if (register_as == 'recruiter'):
        user_type_id = 1
    elif (register_as == 'Job Seeker'):
        user_type_id = 2

    profile_picture_data = None  # Initialize with default value
    if profile_picture:
        # Read file contents
        profile_picture_data = profile_picture.read()

    if (gender == 'male'):
        gender = 'M'
    elif (gender == 'female'):
        gender = 'F'
    elif (gender == 'other'):
        gender = 'O'

    is_active = 'Y'

    if (sms_notification == 'yes'):
        sms_notification = 'Y'
    elif (sms_notification == 'no'):
        sms_notification = 'N'

    if (email_notification == 'yes'):
        email_notification = 'Y'
    elif (email_notification == 'no'):
        email_notification = 'N'
        
    registration_date = date.today()

    # check if user exists
    result = get_login_data(email)
    if (result):
        # user exists
        print(f"User \"{email}\" already exists !")
        return False
        
    else:
        # add user
        add_user(user_type_id, email, password, name, dob, gender, is_active, contact_number, sms_notification, email_notification, profile_picture_data, registration_date)
        print(f"registration completed for \"{email}\".")
        return True