import json

# with open('users.json') as json_data:
#     print(type(json_data))

class User:
    def __init__(self, id, age, gender, hobbies):
        self.id = id
        self.age = age
        self.gender = gender
        self.hobbies = hobbies

class UserDatabase:

    def __init__(self):
        self.users = []  # au départ la liste des utilisateurs est vide, on la remplit en appelant la méthode load()

    def get_nb_users(self):
        liste_users = self.users
        nb = 0
        for nb in users.json:
            nb += 1
        print("Le nombre d'utilisateurs est : ", {self.id})

    def load(self):
        with open('users.json', 'r') as read_file:
            users_json = json.load(read_file)
            for user in users_json:
                # Vous ne passer pas les bons attributs pour créer un utilisateur (on a besoin uniquement de: id, age, gender, hobbies)
                self.users.append(User(user.get("id"), user.get("age"), user.get("gender"), user.get("hobbies")))

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

print()



"""
Code executé
"""
database = UserDatabase()
database.load()
database.get_nb_users()
