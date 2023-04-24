class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        
    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print(resultat)

# Création d'un nouvel objet de la classe "Operation"
op2 = Operation(12, 3)

# Appel de la méthode "addition" sur le nouvel objet "op2"
op2.addition()