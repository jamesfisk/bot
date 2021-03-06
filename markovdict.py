from linkedwordlist import *
import json
import random

class markovdict (object):
  def __init__(self, words):
    self.model = {}
    self.words = words
    self.pi = node(words[0])
    self.lengths = []

    #populate model
    for k in range(11):
      self.lengths.append(k + 5)

    for i in range(len(words) - 1):
      #populate pi values
      if (i > 0):
        if (words[i - 1][-1] == "." and words[i].isalpha()):
          self.pi.insert(words[i])

      if (words[i] not in self.model):
        self.model[words[i]] = node(words[i + 1])
      else:
        self.model[words[i]] = self.model[words[i]].insert(words[i + 1])

    #run probabilities
    self.pi.calculate_prob()
    for elt in self.model:
      self.model[elt].calculate_prob()

  def get_sentence (self):
    length = random.choice(self.lengths)
    start = self.pi.choose()
    word = start
    for i in range(length):
      word = self.model[word].choose()
      start += " " + word
    return start

  def save_model(self, filename):
    json.dump(self.model, open(filename, "w"))
