class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = kilometrage
        self.en_marche = False
        self.reservoir = 50

    def get_marque(self):
        return self.marque

    def set_marque(self, marque):
        self.marque = marque

    def get_modele(self):
        return self.modele

    def set_modele(self, modele):
        self.modele = modele

    def get_annee(self):
        return self.annee

    def set_annee(self, annee):
        self.annee = annee

    def get_kilometrage(self):
        return self.kilometrage

    def set_kilometrage(self, kilometrage):
        self.kilometrage = kilometrage

    def get_en_marche(self):
        return self.en_marche

    def set_en_marche(self, en_marche):
        self.en_marche = en_marche

    def get_reservoir(self):
        return self.reservoir

    def verifier_plein(self):
        return self.reservoir

    def demarrer(self):
        if self.verifier_plein() > 5:
            self.en_marche = True

    def arreter(self):
        self.en_marche = False
     # Instanciation d'un objet de la classe Voiture
voiture = Voiture("Renault", "Clio", 2015, 50000)

# Accès aux attributs de l'objet
print("Marque :", voiture.get_marque())
print("Modèle :", voiture.get_modele())
print("Année :", voiture.get_annee())
print("Kilométrage :", voiture.get_kilometrage())
print("Réservoir :", voiture.get_reservoir())
print("En marche :", voiture.get_en_marche())

# Modification de l'attribut en_marche
voiture.set_en_marche(True)
print("En marche :", voiture.get_en_marche())

# Appel de la méthode demarrer
voiture.demarrer()
print("En marche :", voiture.get_en_marche())

# Appel de la méthode arreter
voiture.arreter()
print("En marche :", voiture.get_en_marche())   