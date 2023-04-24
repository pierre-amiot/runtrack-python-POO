class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""
    
    def vieillir(self):
        self.age += 1


# Instanciation d'un objet de la classe "Animal"
mon_animal = Animal()

# Affichage de l'âge initial de l'animal
print("Age de l'animal : {} ans".format(mon_animal.age))

# Faire vieillir l'animal
mon_animal.vieillir()

# Affichage de la nouvelle age de l'animal
print("Age de l'animal : {} ans".format(mon_animal.age))
class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""
    
    def vieillir(self):
        self.age += 1
    
    def nommer(self, nom):
        self.prenom = nom


# Instanciation d'un objet de la classe "Animal"
mon_animal = Animal()

# Nommer l'animal
mon_animal.nommer("Luna")

# Affichage du nom de l'animal
print("Nom de l'animal : {}".format(mon_animal.prenom))