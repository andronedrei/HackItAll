import json

# lements returned from the database are returned as a tuple, so we need to convert them to a dictionary before returning them as JSON.

def get_dict_user(user_tuple):
    dict = {
        "id": user_tuple[0],
        "username": user_tuple[1],
        "password": user_tuple[2],
        "email": user_tuple[3],
        "first_name": user_tuple[4],
        "last_name": user_tuple[5],
        "age": user_tuple[6],
        "phone": user_tuple[7],
        "date_of_birth": user_tuple[8],
        "national_country": user_tuple[9],
        "national_city": user_tuple[10],
        "residence_country": user_tuple[11],
        "residence_city": user_tuple[12],
        "profile_picture": user_tuple[13],
        "latitude": user_tuple[14],
        "longitude": user_tuple[15]
    }
    return json.dumps(dict)

def get_dict_users(users_tuple):
    users = []
    for user in users_tuple:
        users.append(get_dict_user(user))
    return users