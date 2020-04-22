# Manipulation de données

Critères de notation:

* Difficulté du sujet choisi 
* Lisibilité du code
* Effort de groupe, au moins 1 commit par membre du groupe (pas de commit = pas de note!)

## Enoncé du problème

Le service marketing désire développer une application pour automatiser la segmentation de sa base client.  

Il nous demande d'effectuer un POC (Proof Of Concept) pour démontrer la faisabilité d'une telle application.  
  
Pour ce faire, nous disposons d'un extrait de la base de données client au format Json (`users.json`).

Le format JSON (JavaScript Object Notation) est un format de données qui permet de représenter de l’information structurée.  
  
Exemple d'un fichier au format Json:  
  
```javascript  
{  
    "spé-data": {  
        "école": "digital-campus",  
        "étudiants": 3,  
	"année": "2019-2020",
	"elèves": ["toto", "tutu", "tata"]
    }  
}  
```

## Modélisation

On modélisera le problème à l'aide de deux classes :

* une classe `UserDatabase` qui modélise la base des utilisateurs

* une classe `User` qui représente un utilisateur
 
Un utilisateur possède plusieurs attributs :

* `id` : le numéro de l'utilisateur
* `age` : l'age le l'utilisateur
* `gender` : le sexe de l'utilisateur
* `hobbies` : la liste de leurs hobbies 

La base d'utilisateurs est composée:

* d'un seul attribut: une liste d'utilisateurs `users`
* d'une méthode `load` qui prend en paramètre le chemin vers un fichier json, le lit et charge les données (cf exemple en Annexe).

## Implémentation

Le but de l'exercice est d'implémenter les méthodes suivantes dans la classe `UserDatabase` :

* `get_nb_users` retourne le nombre d'utilisateurs
* `get_age_average` retourne la moyenne d'âge des utilisateurs
* `get_top_3_hobbies` retourne les 3 hobbies les plus courants
* `compute_segmentation` retourne la liste des ids utilisateur qui sont des hommes entre 25 et 30 ans(inclus) et qui aiment le cinéma
* `get_random_users` prend en paramètre un nombre `n` et retourne une liste aléatoire de `n` ids utilisateur.
 
## Tests unitaires

Écrire des tests unitaires vérifiant le bon fonctionnement des méthodes implémentées.

## Annexes

Pour lire le fichier data.json contenant : 
  
```javascript  
[  
  { "champs1": "c1", "champs2": ["tata", "toto"] },  
  { "champs1": "c2", "champs2": ["tutu" ] }  
]   
```

On peut utiliser le programme suivant:

```python
import json  
 
with open('data.json', 'r') as json_file:  
    datas = json.load(json_file)  
    for d in datas:  
        print(d.get("champs1"))  
        for l in d.get("champs2"):  
            print(l)
```
