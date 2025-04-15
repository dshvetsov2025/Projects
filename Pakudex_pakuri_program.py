# Code for the main part of the project

# Importing the Pakudex and Pakuri classes
from Pakudex_main import Pakudex
from Pakudex_pakuri import Pakuri


# Function to display the main menu with needed choices
def display_menu():
    print("\nPakudex Main Menu")
    print("-----------------")
    print("1. List Pakuri")
    print("2. Show Pakuri")
    print("3. Add Pakuri")
    print("4. Evolve Pakuri")
    print("5. Sort Pakuri")
    print("6. Exit\n")


# Functon for the processes behind the menu options
def main():
    print("Welcome to Pakudex: Tracker Extraordinaire!")

    # Creating a loop to input a valid capacity
    while True:
        try:
            capacity = int(input("Enter max capacity of the Pakudex: "))
            if capacity <= 0:
                print("Please enter a valid size.")
            else:
                break
        except ValueError:
            print("Please enter a valid size.")

    # Creating a variable of Pakudex with the given capacity
    pakudex = Pakudex(capacity)
    print(f"The Pakudex can hold {capacity} species of Pakuri.")

    # Loop to incorporate the processes for the menu options
    while True:
        display_menu()  # Showing the  menu options
        choice = input("What would you like to do? ")

        # Listing all Pakuri in the Pakudex
        if choice == "1":
            species_list = pakudex.get_species_array()
            if species_list is None:
                print("No Pakuri in Pakudex yet!")
            else:
                print("Pakuri In Pakudex:")
                for i in range(len(species_list)):
                    print(f"{i + 1}. {species_list[i]}")

        # Showing details of a specific Pakuri
        elif choice == "2":
            name = input("Enter the name of the species to display: ")
            stats = pakudex.get_stats(name)
            if stats is None:
                print("Error: No such Pakuri!")
            else:
                print(f"\nSpecies: {name}")
                print(f"Attack: {stats[0]}")
                print(f"Defense: {stats[1]}")
                print(f"Speed: {stats[2]}")

        # Adding a new Pakuri to the Pakudex
        elif choice == "3":
            if pakudex.get_size() >= pakudex.get_capacity():
                print("Error: Pakudex is full!")
            else:
                name = input("Enter the name of the species to add: ")
                if pakudex.add_pakuri(name):
                    print(f"Pakuri species {name} successfully added!")
                else:
                    print("Error: Pakudex already contains this species!")

        # Evolving a Pakuri
        elif choice == "4":
            name = input("Enter the name of the species to evolve: ")
            if pakudex.evolve_species(name):
                print(f"{name} has evolved!")
            else:
                print("Error: No such Pakuri!")

        # Sorting the Pakuri in alphabetical order
        elif choice == "5":
            pakudex.sort_pakuri()
            print("Pakuri have been sorted!")

        # Exiting the program
        elif choice == "6":
            print("Thanks for using Pakudex! Bye!")
            break

        # Handling invalid menu selections
        else:
            print("Unrecognized menu selection!")


# Necessary code to run the program
if __name__ == "__main__":
    main()
