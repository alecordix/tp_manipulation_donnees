import json

"""
Déclaration des classes 
(cela revient à créer un nouveau type que l'on pourra utiliser lors de la création de nos variables)
"""


class UserDatabase:

    def __init__(self, users_list):
        """
        Attributs de la classe UserDatabase:
        J'ai renommé users en users_list pour que le nom soit plus parlant
            * users_list  : une liste d'objets de type User
                ==> si on est à l'intérieur de la classe : on accède à cette variable avec self.users_list
                ==> si on est à l'extérieur de la classe :
                    on accède à cette variable à partir d'une variable de type UserDatabase préalablement créée
                    exemple:
                         database = UserDatabase()  # je crée une variable de type UserDatabase
                         database.users_list        # j'accède à la liste de cette database
        """
        self.users_list = users_list

    def display(self):
        # J'ai ajouté cette méthode pour vous permettre d'afficher le contenu de UserDatabase
        # (contenu = les utilisateurs présents dans la base)
        print("Utilisateurs présents dans la base:")
        for u in self.users_list:
            print("{ id:", u.id, ", age:", u.age, ", gender:", u.gender, ", hobbies:", u.hobbies, "}")

    def display_age(self):
        # J'ai ajouté cette méthode pour vous permettre d'afficher le contenu de UserDatabase
        # (contenu = les utilisateurs présents dans la base)
        print("L'age des utilisateurs présents dans la base:")
        for u in self.users_list:
            print("age:", u.age)

    # def get_nb_users_old(self):
    #     # TODO: à supprimer ==> je laisse le code ici pour vous faire quelques retours
    #     users = 0
    #     for users in users.json : # ATTENTION à votre nommage: ici users est l'entier déclaré à la ligne précédente (donc il n'a pas d'attribut json)
    #         users += 1
    #     print("Le nombre de users est", {self.id})  # le mot-clé self permet d'accéder aux attributs de la classe dans laquelle on se trouve (self.id ne fonctionne que si on est à l'intérieur de la classe User)
    #     # retourner le nombre d'utilisateurs
    #     # (sinon ce ne sera pas possible de faire un test unitaire sur cette méthode)
    #     return users

    def get_nb_users(self):
        print()
        # j'ai apporté les corrections nécessaires pour que votre code fonctionne
        users_list = self.users_list  # liste des utilisateurs présents dans la base
        users = 0
        for u in users_list:
            users += 1
        print("Le nombre de users est")
        return users  # je retourne le nombre d'utilisateurs

    def cal_average(self):

        for u in self.users_list:
            total = []
            for u in self.users_list:
                total.append(u.age)
                for u in total:
                    if type(u) is not int :
                        total.remove(u)
        print(total)
        somme = sum(total)
        moyenne = somme / len(total)
        print("Il y a", len(total),"utilisateurs qui ont rentré leur âge")
        print("La somme des âges est de :", sum(total))
        return moyenne

    def get_top_3_hobbies(self):
        import collections
        for u in self.users_list:
            tot_hobbies = []
            for u in self.users_list:
                tot_hobbies.extend(u.hobbies)
        low = [x.lower() for x in tot_hobbies]
        populaire = collections.Counter(low).most_common(3)
        return populaire


    def load(self):
        with open('users.json', 'r') as read_file:
            users_json = json.load(read_file)
            for user in users_json:
                self.users_list.append(User(user.get("id"), user.get("age"), user.get("gender"), user.get("hobbies")))

    # with open('users.json', 'r') as read_file:
    #      datas = json.load(read_file)
    #      for a in datas:
    #          print(a.get("id"))
    #      for b in datas:
    #          print(b.get("nom"))
    #      for c in datas:
    #          print(c.get("prenom"))
    #      for d in datas:
    # #
    # print(d.get("profession"))
    # #
    # for e in datas:
    # #
    # print(e.get("age"))
    # #
    # for f in datas:
    # #
    # print(f.get("sexe"))
    # #
    # for g in datas:
    # #
    # print(bool(g.get("marie")))
    # #
    # for h in datas:
    #
    # print(h.get("hobbies"))


class User:
    def __init__(self, id, age, gender, hobbies):
        self.id = id
        self.age = age
        self.gender = gender
        self.hobbies = hobbies


"""
Code executé
"""

# création d'une base de données
empty_list = []
empty_list_age = []
database = UserDatabase(empty_list)  # création d'une variable database de type UserDatabase, la base est vide au départ
database.load()  # chargement du Json dans la variable database (on ajoute tous les utilisateurs à la liste database.users_list)
database.display()  # affichage du contenu de la variable database (on appelle la méthode display)

# nombre d'utilisateurs dans la base "database"
cnt_users = database.get_nb_users()
print(cnt_users)

# l'age des utilisateurs dans la base
print()
age_user = database.display_age()

print()
avg_age = database.cal_average()
print("La moyenne d'age est :", avg_age)

print()
best_hobbies = database.get_top_3_hobbies()
print("La liste des hobbies est :", best_hobbies)
# moyenne d'age utilisateurs

# moyenne_age = database.get_age_average()
# print(moyenne_age)
