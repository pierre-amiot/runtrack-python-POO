class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

# Création d'un objet de la classe "Operation"
op = Operation(12, 3)

# Impression des valeurs des attributs "nombre1" et "nombre2" en console
print(op.nombre1)
print(op.nombre2)