# Code for the pakuri file

# Creating the Pakuri class
class Pakuri:
    def __init__(self, species):
        # Storing the species names
        self.species = species

        # Initializing stats using formulas:
        self.attack = (len(species) * 7) + 9
        self.defense = (len(species) * 5) + 17
        self.speed = (len(species) * 6) + 13

    # Get method for species name
    def get_species(self):
        return self.species

    # Get method for attack stats
    def get_attack(self):
        return self.attack

    # Get method for defense stats
    def get_defense(self):
        return self.defense

    # Get method for speed stats
    def get_speed(self):
        return self.speed

    # Set method for updating attack stats
    def set_attack(self, new_attack):
        self.attack = new_attack

    # Evolving the Pakuri — doubling attack, quadrupling defense, and tripling speed
    def evolve(self):
        self.attack *= 2
        self.defense *= 4
        self.speed *= 3
