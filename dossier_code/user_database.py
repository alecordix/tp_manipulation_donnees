import json
# with open('users.json') as json_data:
#     print(type(json_data))
class UserDatabase:
    def __init__(self, users):
        self.users = users

    def get_nb_users(self):
        users = 0
        for users in users.json :
            users += 1
        print("Le nombre de users est", {self.id})

    def load(self):
        with open('users.json', 'r') as read_file:
            users_json = json.load(read_file)
            for user in users_json:
                self.users.append(User(user.get("id"), user.get("nom"),user.get("prenom"),user.get("profession"), user.get("age"), user.get("sexe"), user.get("marie"), user.get("hobbies")))

    with open('users.json', 'r') as read_file:
        datas = json.load(read_file)
        for a in datas:
            print(a.get("id"))
        for b in datas:
            print(b.get("nom"))
        for c in datas:
            print(c.get("prenom"))
        for d in datas:
            print(d.get("profession"))
        for e in datas:
            print(e.get("age"))
        for f in datas:
            print(f.get("sexe"))
        for g in datas:
            print(bool(g.get("marie")))
        for h in datas:
            print(h.get("hobbies"))


class User:
    def __init__(self, id, age, gender, hobbies):
        self.id = id
        self.age = age
        self.gender = gender
        self.hobbies = hobbies

