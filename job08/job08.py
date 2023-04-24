class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self._titre = titre
        self._auteur = auteur
        self._nb_pages = nb_pages
        self._disponible = True

    def get_titre(self):
        return self._titre

    def set_titre(self, titre):
        self._titre = titre

    def get_auteur(self):
        return self._auteur

    def set_auteur(self, auteur):
        self._auteur = auteur

    def get_nb_pages(self):
        return self._nb_pages

    def set_nb_pages(self, nb_pages):
        if isinstance(nb_pages, int) and nb_pages > 0:
            self._nb_pages = nb_pages
        else:
            print("Le nombre de pages doit être un entier positif")

    def get_disponible(self):
        return self._disponible

    def verification(self):
        return self._disponible == True

    def emprunter(self):
        if self.verification() == True:
            self._disponible = False
            print("Le livre a bien été emprunté")
        else:
            print("Le livre n'est pas disponible")

    def rendre(self):
        if self.verification() == False:
            self._disponible = True
            print("Le livre a bien été rendu")
        else:
            print("Le livre n'a pas été emprunté")

mon_livre = Livre("Harry Potter à l'école des sorciers", "J.K. Rowling", 300)

print(mon_livre.verification()) # True
mon_livre.emprunter() # Le livre a été emprunté.
print(mon_livre.verification()) # False
mon_livre.rendre() # Le livre a été rendu.
print(mon_livre.verification()) # True