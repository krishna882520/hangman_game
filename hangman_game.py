import random

# List of words to choose from
words = ['python', 'hangman', 'programming', 'developer', 'chatgpt']

# Choose a random word
word = random.choice(words)
guessed_word = ['_'] * len(word)
guessed_letters = []
tries = 6

print("Welcome to Hangman!")
print("You have", tries, "tries to guess the word.")

while tries > 0 and '_' in guessed_word:
    print("\nCurrent word: " + ' '.join(guessed_word))
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
        for i, letter in enumerate(word):
            if letter == guess:
                guessed_word[i] = guess
    else:
        print ("Wrong guess.")
        tries -= 1
        print(f"Tries left: {tries}")

if '_' not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)