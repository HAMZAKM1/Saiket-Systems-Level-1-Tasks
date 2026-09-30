import random

def play_number_guessing_game():
    """
    Interactive Number Guessing Game.
    Generates a random integer between 1 and 100 and provides directional hints.
    """
    print("=" * 50)
    print("           WELCOME TO THE NUMBER GUESSING GAME          ")
    print("=" * 50)
    print("I have selected a random number between 1 and 100.")
    print("Can you guess what it is?\n")

    secret_number = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        try:
            user_input = input("Enter your guess (1-100): ").strip()
            
            if not user_input.isdigit():
                print("⚠️ Invalid input! Please enter a valid integer between 1 and 100.\n")
                continue

            guess = int(user_input)
            
            if guess < 1 or guess > 100:
                print("⚠️ Out of range! Please enter a number from 1 to 100.\n")
                continue

            attempts += 1

            if guess < secret_number:
                print("📉 Too low! Try a higher number.\n")
            elif guess > secret_number:
                print("📈 Too high! Try a lower number.\n")
            else:
                guessed_correctly = True
                print("\n" + "=" * 50)
                print("🎉 CONGRATULATIONS! YOU GUESSED IT! 🎉")
                print("=" * 50)
                print(f"Target Number  : {secret_number}")
                print(f"Total Attempts : {attempts}")
                print("=" * 50)

        except ValueError:
            print("⚠️ Invalid input! Please enter a valid integer.\n")

if __name__ == "__main__":
    play_number_guessing_game()