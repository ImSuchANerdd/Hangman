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
