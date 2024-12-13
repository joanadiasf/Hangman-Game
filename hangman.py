import random

def hangman():
    words = ["computer","game","python","holidays"]

    secret_word = random.choice(words).lower()
    guessed_word = ["_" for _ in secret_word]
    attempts = 6
    used_letters = set()

    print("Welcome to the Hangman Game!")

    while attempts > 0:
        print("\nWords:", " ".join(guessed_word))
        print(f"Attemps left: {attempts}")
        print("Used letters:", ", ".join(sorted(used_letters)))

        guess = input("Your guess: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please, write just one letter.")
            continue

        if guess in used_letters:
            print("You already used this letter. Try again.")
            continue

        used_letters.add(guess)

        if guess in secret_word:
            print(f"Nice! The letter '{guess}' is in the word!")
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            print(f"What a shame! The letter '{guess}' isn't in the word.")
            attempts -= 1

        if "_" not in guessed_word:
            print("\nCongrats! You guessed the word:", secret_word)
            break
    else:
        print("\nYou lost! The word was:", secret_word)

if __name__ == "__main__":
    hangman()