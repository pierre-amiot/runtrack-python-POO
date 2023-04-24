class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages

    def get_titre(self):
        return self.__titre

    def set_titre(self, titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_nb_pages(self):
        return self.__nb_pages

    def set_nb_pages(self, nb_pages):
        if nb_pages > 0:
            self.__nb_pages = nb_pages
        else:
            print("Erreur: Le nombre de pages doit être un entier positif.")

    def __str__(self):
        return f"Titre: {self.__titre}\nAuteur: {self.__auteur}\nNombre de pages: {self.__nb_pages}"

# exemple d'utilisation
livre = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", 3000)
print(livre)
livre.set_nb_pages(-50) # va afficher un message d'erreur