import random
from words import word_list

def get_word():
  word = random.choice(word_list)
  return word.upper()

def play(word):
  word_completion = "-" * len(word)
  guessed = False
  guessed_letters = []
  tries = 5
  print("\n")
  print("Let's play Hangman!")
  print("\n")
  print("\n")
  print("You can guess 5 times. Use them carefully...")
  print("\n")
  print("The word consists of", len(word), "letters.")
  print("\n")
  while guessed == False and tries > 0:
    print('You have ' + str(tries) + ' tries left.')
    guess = input("Please guess a letter: ").upper()
    if len(guess) == 1 and guess.isalpha():
      if guess in guessed_letters:
        print("You already guessed the letter", guess)
      elif guess not in word:
        print(guess, "is not in the word.")
        tries -= 1
        guessed_letters.append(guess)
