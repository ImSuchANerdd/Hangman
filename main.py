run = main.py

import random
from words import word_list

def get_word():
  word = random.choice(word_list)
  return word.lower()


def play(word):
  word_completion = "_" * len(word)
  guessed = False
  guessed_letters = []
  guessed_words = []
  guesses = 5

print("Let's play Hangman")
print(display_hangman(guesses))
print(word_completion)
print("\n")
while not guessed and guesses > 0:
  guess = input("Please guess a letter or word: ").upper()
if len(guess) == 1 and guess.isalpha():
  if guess in guessed_letters:
    print("You already guessed the letter", guess)
  elif guess not in word:
    print(guess, "is not in the word.")
    tries -= 1
    guessed_letters.append(guess)
  else:
    print("Good job, ", guess, "is in the word!")
    guessed_letters.append(guess)
    word_as_list = list(word_completion)
    indices = [i for i, letter in enumerate(word) if letter == guess]
    for index in indices:
      word_as_list[index] = guess
    word_completion = "".join(word_as_list)
    if "_" not in word_completion:
      guessed = True
elif len(guess) == len(word) and guess.isalpha()
  if guess in guessed_words:
    print("You already guessed that")
  elif guess != word:
    print(guess, "is not in the word.")
    tries -= 1
    guessed_words.append(guess)
  else:
    guessed = True
    word_completion = word
else:
  print ("Not a valid guess.")
print(display_hangman(guesses))
print(word_completion)
print("\n")

if guessed:
  print("Congratulations, you won!")
else:
  print("Sorry, out of tries. The word was" + word + ". Maybe next time.")


def print_scaffold(guesses, wd):
  if (guesses == 0)
    print "__________"
    print "I      I"
    print "I"
    print "I"
    print "I"
    print "I"
    print "__________"
  elif (guesses == 1)
    print "__________"
    print "I      I"
    print "I      O"
    print "I"
    print "I"
    print "I"
    print "__________"
  elif (guesses == 2)
    print "__________"
    print "I      I"
    print "I      O"
    print "I     \l"
    print "I"
    print "I"
    print "__________"
  elif (guesses == 3)
    print "__________"
    print "I      I"
    print "I      O"
    print "I     \l/"
    print "I"
    print "I"
    print "__________"
  elif (guesses == 4)
    print "__________"
    print "I      I"
    print "I      O"
    print "I     \l/"
    print "I     /"
    print "I"
    print "__________"
    elif (guesses == 5)
    print "__________"
    print "I      I"
    print "I      O"
    print "I     \l/"
    print "I     / \"
    print "I"
    print "__________"

def main():
  word = get_word()
  play(word)
  while input("Play again? (Y/N) ").upper == "Y":
    word = get_word()
    play(word)

if __name__ == "__main__":
  main()