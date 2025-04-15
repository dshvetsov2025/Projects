# Program for the BlackJack game
import p1_random as p1 # Importing a given file

rng = p1.P1Random()
# Variables that will be used
game_num = 0
player_win = 0
dealer_win = 0
game_ties = 0

while True:
    # Starting a new game
    game_num += 1
    print(f"\nSTART GAME #{game_num}\n")

    card = rng.next_int(13) + 1  # Random card [1, 13]
    if card == 1:
        hand = 1
        card_name = "ACE"
    elif 2 <= card <= 10:
        hand = card
        card_name = str(card)
    elif card == 11:
        hand = 10
        card_name = "JACK"
    elif card == 12:
        hand = 10
        card_name = "QUEEN"
    else:
        hand = 10
        card_name = "KING"

    print(f"Your card is a {card_name}!")
    print(f"Your hand is: {hand}\n") # Printing the required output in the correct format

    while True:
        print("1. Get another card")
        print("2. Hold hand")
        print("3. Print statistics")
        print("4. Exit") # Printing all the options for the input

        choice = input("\nChoose an option: ")

        if not choice.isdigit() or int(choice) not in {1, 2, 3, 4}:
            print("\nInvalid input!")
            print("Please enter an integer value between 1 and 4.\n")
            continue # Making sure that the choice is a valid input

        choice = int(choice) # Inputting a choice value

        if choice == 1: # Code for the correct output of the user selecting 1 as input
            card = rng.next_int(13) + 1
            if card == 1:
                hand += 1
                card_name = "ACE"
            elif 2 <= card <= 10:
                hand += card
                card_name = str(card)
            elif card == 11:
                hand += 10
                card_name = "JACK"
            elif card == 12:
                hand += 10
                card_name = "QUEEN"
            else:
                hand += 10
                card_name = "KING"

            print(f"\nYour card is a {card_name}!")
            print(f"Your hand is: {hand}\n") # Printing the correct output based on the user input

            if hand == 21:
                print("BLACKJACK! You win!\n")
                player_win += 1
                break
            elif hand > 21:
                print("You busted! Dealer wins.\n")
                dealer_win += 1
                break # Correct format for if you lose and win

        elif choice == 2: # Code for the correct output if the user selects 2 as input
            dealer_hand = rng.next_int(11) + 16
            print(f"\nDealer's hand: {dealer_hand}")
            print(f"Your hand is: {hand}\n")

            if dealer_hand > 21 or hand > dealer_hand:
                print("You win!\n")
                player_win += 1
            elif hand == dealer_hand:
                print("It's a tie!\n")
                print("No one wins!\n")
                game_ties += 1 # Code for a tie situation
            else:
                print("Dealer wins!\n")
                dealer_win += 1
            break

        elif choice == 3: # Code for the correct output if the user selects 3 as input
            total_games = player_win + dealer_win + game_ties
            win_percentage = (player_win / total_games * 100) if total_games > 0 else 0.0
            print(f"\nNumber of Player wins: {player_win}")
            print(f"Number of Dealer wins: {dealer_win}")
            print(f"Number of tie games: {game_ties}")
            print(f"Total # of games played is: {total_games}")
            print(f"Percentage of Player wins: {win_percentage:.1f}%\n")

        elif choice == 4: # Code for the correct output if the user selects 4 as input
            exit()