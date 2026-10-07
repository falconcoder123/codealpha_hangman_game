import random

def play_hangman():
    words = [
        "python", "coding", "laptop", "github", "program",
        "computer", "developer", "keyboard", "software"
    ]

    word = random.choice(words)
    guessed = set()
    chances = 6

    print("Welcome to Hangman!")
    print("Guess the word.")

    while chances > 0:
        display = ""

        for letter in word:
            if letter in guessed:
                display += letter + " "
            else:
                display += "_ "

        print("\nWord:", display)
        print("Chances left:", chances)
        print("Guessed:", " ".join(sorted(guessed)) if guessed else "None")

        if "_" not in display:
            print("Congratulations! You guessed the word:", word)
            break

        guess = input("Enter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Enter only one letter.")
            continue

        if guess in guessed:
            print("You already guessed that letter.")
            continue

        guessed.add(guess)

        if guess in word:
            print("Correct!")
        else:
            chances -= 1
            print("Wrong guess.")

    if chances == 0:
        print("\nGame Over!")
        print("The word was:", word)


if __name__ == "__main__":
    play_hangman()