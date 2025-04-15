# Code for the pakudex file

# Importing a class from pakuri file
from pakuri import Pakuri

# Function that is used for sorting Pakuri by species names
def get_species_name(pakuri):
    return pakuri.get_species()

# Creating the Pakudex class
class Pakudex:
    def __init__(self, capacity=20):
        self.capacity = capacity
        self.pakuri_list = []

    # Returning the number of Pakuri currently in the Pakudex
    def get_size(self):
        return len(self.pakuri_list)

    # Returning the maximum capacity of the Pakudex
    def get_capacity(self):
        return self.capacity

    # Returning a list of the species names, or simply None if the list is empty
    def get_species_array(self):
        if len(self.pakuri_list) == 0:
            return None
        return [pakuri.get_species() for pakuri in self.pakuri_list]

    # Returning the stats, like attack, defense, and speed, of the specified species
    def get_stats(self, species):
        for pakuri in self.pakuri_list:
            if pakuri.get_species() == species:
                return [pakuri.get_attack(), pakuri.get_defense(), pakuri.get_speed()]
        return None

    # Sorting the internal list of Pakuri in alphabetical order by the species names
    def sort_pakuri(self):
        self.pakuri_list.sort(key=get_species_name)

    # Adding a new Pakuri to the Pakudex if there's space and it is not going to be a duplicate
    def add_pakuri(self, species):
        if len(self.pakuri_list) >= self.capacity:
            return False  # Figuring if Pakudex is full

        for pakuri in self.pakuri_list:
            if pakuri.get_species() == species:
                return False  # Duplicating species

        self.pakuri_list.append(Pakuri(species))
        return True

    # Evolving a Pakuri of the given species if found
    def evolve_species(self, species):
        for pakuri in self.pakuri_list:
            if pakuri.get_species() == species:
                pakuri.evolve()
                return True
        return False
