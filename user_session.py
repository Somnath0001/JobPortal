from flask import session

def get_id():
    return session["user_id"]

def set_id(user_id):
    session["user_id"] = user_id

def clear_session():
    session.pop("user_id", None)

