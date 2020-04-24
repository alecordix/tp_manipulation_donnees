import json

"""
Déclaration des classes 
(cela revient à créer un nouveau type que l'on pourra utiliser lors de la création de nos variables)
"""


class UserDatabase:

    def __init__(self, users_list):
        self.users_list = users_list

    def display(self):
        print("Utilisateurs présents dans la base:")
        for u in self.users_list:
            print("{ id:", u.id, ", age:", u.age, ", sexe:", u.sexe, ", hobbies:", u.hobbies, "}")

    def display_age(self):
        print("L'age des utilisateurs présents dans la base:")
        for u in self.users_list:
            print("age:", u.age)

    def get_nb_users(self):
        print()
        users_list = self.users_list
        users = 0
        for u in users_list:
            users += 1
        print("Le nombre de users est")
        return users

    def cal_average(self):

        for u in self.users_list:
            total = []
            for u in self.users_list:
                total.append(u.age)
                for u in total:
                    if type(u) is not int:
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


    def compute_segmentation(self):
        for u in self.users_list:
            tot_ids = []
            for u in self.users_list:
                if (u.sexe == 'homme' or u.sexe =='Homme') and (u.age >= 25 and u.age <= 30) and ('cinema' or 'Cinema' in u.hobbies):
                    tot_ids.append(u.id)
            return tot_ids

    def get_random_users(self):
        import random
        tot_ids = []
        x = random.randint(1,len(self.users_list))
        print("Le chiffre aléatoire est :", x)
        for u in self.users_list:
            tot_ids.append(u.id)
        result= random.sample(tot_ids, x)
        return result


    def load(self):
        with open('users.json', 'r') as read_file:
            users_json = json.load(read_file)
            for user in users_json:
                self.users_list.append(User(user.get("id"), user.get("age"), user.get("sexe"), user.get("hobbies")))

class User:
    def __init__(self, id, age, sexe, hobbies):
        self.id = id
        self.age = age
        self.sexe = sexe
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

#le sexe des utilisateurs dans la base
print()
age_user = database.display_age()

print()
avg_age = database.cal_average()
print("La moyenne d'age est :", avg_age)

print()
best_hobbies = database.get_top_3_hobbies()
print("La liste des hobbies est :", best_hobbies)


print()
id_male_cinema = database.compute_segmentation()
print("Les id des hommes de 25 à 30 ans inclus et qui aiment le cinema sont:", id_male_cinema)

# selection
print()
random_users = database.get_random_users()
print("Liste de users aléatoires :", random_users)