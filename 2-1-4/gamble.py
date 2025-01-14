import random

# List of slot machine symbols
symbols = ['🍒', '🍋', '🍉', '🍊', '⭐', '🍀']


def spin_slot_machine():
    # Randomly select 3 symbols for the slot machine
    spin_result = random.choices(symbols, k=3)

    return spin_result


def display_result(spin_result):
    print("||", " || ".join(spin_result), "||")
    print("-" * 20)


def check_win(spin_result):
    # If all three symbols are the same, it's a win
    if spin_result[0] == spin_result[1] == spin_result[2]:
        print("You win! 🎉")
    else:
        print("Sorry, you lose. Try again!")


def main():
    print("Welcome to the Slot Machine! 🎰")

    while True:
        input("Press Hit Enter to spin...")  # Wait for the user to press Enter

        # Spin the slot machine
        spin_result = spin_slot_machine()

        # Display the result
        display_result(spin_result)

        # Check for a win
        check_win(spin_result)

        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
