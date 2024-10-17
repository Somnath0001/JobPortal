from database import get_login_data;
from werkzeug.security import check_password_hash, generate_password_hash;

def validateUser(email, password):
    result = get_login_data(email)

    # verify username and password
    if (result):    
        # email exists
        if (check_password_hash(result[3], password)):
            print(f"\"{email}\" logged in successfully.")
            return True
        else:
            print(f"Login failed for \"{email}\" - incorrect password.")
            return False
    else:
        # email doesn't exist
        print(f"Invalid username - \"{email}\".")
        return False