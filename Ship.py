
class Ship:

    def __init__(self, name = "Vaisseau", hull = 50, fuel = 50, energy = 50) -> None:
        self.nom = name
        self.coque = [hull]*2
        self.carburant = [fuel]*2
        self.energie = [energy]*2
        self.cargaison = ["Vide"]*10


    def cargo_spot_is_empty(self, spot = 0):
        return self.cargaison[spot] == "Vide"


    def fill_cargo_spot(self, spot = 0, content = ["H",1]):
        if self.cargo_spot_is_empty(spot):
            self.cargaison[spot] = content

    def replace_cargo_spot(self, spot = 0, content = "Vide"):
        self.cargaison[spot] = content

    def empty_cargo_spot(self, spot = 0):
        self.cargaison[spot] = "Vide"

    def add_to_cargo_spot(self, spot = 0, n = 0):
        self.cargaison[spot] += n

    def check_cargo_spot(self, spot = 0, content = "Vide"):
        return [self.cargaison[spot][0] == content[0], self.cargaison[spot][1] == content[1]]

    def str_cargo_spot(self, spot = 0):
        return f"{self.cargaison[spot][0]},{self.cargaison[spot][1]}"

    
    def str_cargo(self):
        chaine = ""
        for n in range(len(self.cargaison)):
            if self.cargo_spot_is_empty(n):
                chaine = chaine + "Vide"
            else:
                chaine = chaine + self.str_cargo_spot(n)

            chaine = chaine + "\n"
        return chaine[:-1]
    
    def save_cargo(self):
        chaine = self.str_cargo()
        f = open(f"{self.nom}_cargo.txt","w")
        f.write(chaine)
        f.close()

    def load_cargo(file_name):
        f = open(file_name+"_cargo.txt","r")
        chaine = f.read()
        f.close()

        cargo = []
        l = chaine.split("\n")
        for val in l:
            if val == "Vide":
                cargo.append(val)

            else:
                val = val.split(",")
                cargo.append([val[0],int(val[1])])

        return cargo

    
    def __str__(self) -> str:
        chaine = f"{self.nom}\nCoque: {self.coque}      Carburant: {self.carburant}      Energie: {self.energie}"
        return chaine

    def __repr__(self) -> str:
        return f"###{self.nom}"
    
    def neat_str_ship(self, n_lignes = 4):
        ratio = len(self.cargaison)//n_lignes
        chaine = str(self)+"\n\nCargo: \n"
        for i in range(n_lignes-1):
            chaine = chaine+"\n"
            for j in range(ratio):
                chaine = chaine+str(self.cargaison[i*ratio+j])

        chaine = chaine+"\n"
        for val in self.cargaison[(i+1)*ratio:]:
            chaine = chaine+str(self.cargaison[i*ratio+j])
        
        return chaine
    
    


# TEST ==============================================================================

if __name__ == "__main__":
    pass

    # Vaisseau = Ship()
    # print(Vaisseau)
    # print(repr(Vaisseau))
    # Vaisseau.fill_cargo_spot()
    # Vaisseau.save_cargo()

    # cargo = Ship.load_cargo(Vaisseau.nom)
    # Vaisseau.cargaison = cargo

    # print(Vaisseau.str_cargo())

    # print("THAT's ALL.")