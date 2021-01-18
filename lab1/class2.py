class Pet():
    def __init__(self,name,species):
        self.name = name
        self.species = species
    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def changename(self,name):
        self.name = name            