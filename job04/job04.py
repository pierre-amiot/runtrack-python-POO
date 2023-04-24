class Personne:
    def __init__(self, nom="", prenom=""):
        self.nom = nom
        self.prenom = prenom
    
    def SePresenter(self):
        return "Je m'appelle {} {}".format(self.prenom, self.nom)


# Instanciation de deux objets de la classe "Personne"
personne1 = Personne("Doe", "John")
personne2 = Personne("Dupond", "Jean")

# Appel de la méthode "SePresenter()" sur les deux objets
print(personne1.SePresenter())
print(personne2.SePresenter())