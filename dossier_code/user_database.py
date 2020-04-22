import json
with open('users.json') as json_data:
    print(type(json_data))
class UserDatabase:
    def __init__(self, users):
        self.users = users

    with open('users.json', 'r') as read_file:
        datas = json.load(read_file)
        for a in datas:
            print(a.get("id"))
            for l in d.get("champs2"):
                print(l)
class User:
    def __init__(self, id, age, gender, hobbies):
        self.id = id
        self.age = age
        self.gender = gender
        self.hobbies = hobbies