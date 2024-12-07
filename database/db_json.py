import json

# lements returned from the database are returned as a tuple, so we need to convert them to a dictionary before returning them as JSON.

def get_dict_user(user_tuple):
    dict = {
        "id": user_tuple[0],
        "username": user_tuple[1],
        "password": user_tuple[2],
        "email": user_tuple[3]
    }
    return json.dumps(dict)

def get_dict_users(users_tuple):
    users = []
    for user in users_tuple:
        users.append(get_dict_user(user))
    return users