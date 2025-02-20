import random as rand


#slot machine symbols
symbols = ['🍍', '🍒', '🍉', '🍎', '⭐', '👽']

# Starting balance
balance = 100
spin_cost = 10  # Cost of each spin


#checking the win of the slots 3 in a row
def check_win(spin_result):
# If all three symbols are the same, it's a win
    if spin_result[0] == spin_result[1] == spin_result[2]:
        print("You Win!")
        return True
    else:
        print("Sorry, you lose. Try again!")
        return False



def spin_slot_machine():
    # Randomly selects 3 symbols for the slot machine
    spin_result = rand.choices(symbols, k=3)
    return spin_result

def display_result(spin_result):
    print("||", " || ".join(spin_result), "||")
    print("-" * 20)


def main():
    global balance
    print("Welcome to the Slot Machine!")
    print(f"You start with ${balance}.")

    while True:
        if balance < spin_cost:
            print(f"You don't have enough money to spin! Game over.")
            break

        # tells user to start a spin and then minus the cost from said spin
        input(f"Press Enter to spin... (Cost: ${spin_cost})")
        balance -= spin_cost

        # Spin the slot machine
        spin_result = spin_slot_machine()


        # Display the result
        display_result(spin_result)

        # Check if the player wins and update balance
        if check_win(spin_result):

            # To make it simple, reward is a fixed amount
            balance += 100  # Winning player gets The amount set
            print(f"Congratulations! You earned $100.")

        # Display the current balance
        print(f"Your current balance is: ${balance}")

        play_again = input("Do you want to play again? (y/n): ")

        if play_again.lower() != 'y':
            print(f"Thanks for playing! Your final balance is: ${balance}")
            break


if __name__ == "__main__":
    main()