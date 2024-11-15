# -*- coding: utf-8 -*-

# Définition des classes
class Employe:
    def __init__(self, identifiant, nom):
        self.id = identifiant
        self.nom = nom
        self.type = "Employé"
    
    def __repr__(self):
        chaine = f"{self.type} {self.id} : {self.nom}"
        return chaine
    
class Responsable(Employe):
    def __init__(self, identifiant, nom, rang):  
        self.id = identifiant
        self.nom = nom
        self.type = "Responsable"
        self.number = rang
  
    def __repr__(self):
        chaine = f"{self.type} {self.id} : {self.nom} (number {self.number})"
        return chaine
    
    def engueuler(self, employe):
        print(f"Alors, tu bosses un peu {employe.nom} ou quoi ?!!")

# Programme principal
        
monEmploye = Employe("E001", "DURAND")
print(monEmploye)

monResponsable = Responsable("R001", "MARTIN", 2)
print(monResponsable)