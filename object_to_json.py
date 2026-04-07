import json

class User:
    def __init__(self):
        self.username = 'user'
        self.email = 'something@mail.com'

def create_new_user(json_str):

    try:
        data = json.loads(json_str)
    except json.JSONDecodeError:
        return User()

    if 'username' in data and 'email' in data:
        new_user = User()
        new_user.username = data['username']
        new_user.email = data['email']
        return new_user
    return User()

def user_to_json(user_obj):
    return json.dumps(user_obj.__dict__)
