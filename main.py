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
      else:
        print("Good job,", guess, "is in the word!")
        guessed_letters.append(guess)
        word_as_list = list(word_completion)
        indices = [i for i, letter in enumerate(word) if letter == guess]
        for index in indices:
          word_as_list[index] = guess
        word_completion = "".join(word_as_list)
        if "-" not in word_completion:
          guessed = True
    else:
      print("Not a valid guess.")
    print(word_completion)
    def sortString(guessed_letters): 
     return ''.join(sorted(guessed_letters))
    print ("Letters used:", sortString(guessed_letters))
    print("\n")
  if guessed:
    print("Congrats, you guessed the word! You win!")
  else:
    print("Sorry, you ran out of guesses. The word was " + word + ". Maybe next time!")
def main():
  word = get_word()
  play(word)
  cont = input("Play again? yes/no > ")
