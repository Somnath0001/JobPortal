from database import get_skill_set_id, add_seeker_skill_set;
from user_session import get_id;

def handle_skills(skill_name, skill_level):
    # get the id of the skill_name from skill_set table
    skill_set_id = get_skill_set_id(skill_name)
    print(f"skill_set_id: {skill_set_id}")

    # get id of the user_session
    id = get_id()

    # insert into seeker_skill_set table
    add_seeker_skill_set(id, skill_set_id, skill_level)



