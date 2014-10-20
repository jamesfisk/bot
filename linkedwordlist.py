from __future__ import division

class node (object):
  def __init__(self, word):
    self.word = word    #Word (string)
    self.count = 1      #Word count
    self.prob = 0.0     #Word probability
    self.nextw = None   #Next node

  def insert(self, word):
    head = self
    retainer = head     #Preserve the original head while iterating
    previous = head     #Remember previous node
    while(head != None and head.word <= word):
      if (head.word == word):
        head.count += 1
        return retainer
      previous = head
      head = head.nextw
    new_node = node(word)
    if (word < previous.word):
      new_node.nextw = previous
      return new_node
    new_node.nextw = previous.nextw
    previous.nextw = new_node
    return retainer

  def calculate_prob(self):
    total = 0
    head = self
    while(head != None):
      total += head.count
      head = head.nextw
    head = self
    if (total == 0):
      return 
    while(head != None):
      head.prob = head.count / total
      head = head.nextw
    return

  #Print a linked list
  def __str__(self):
    link_list = ""
    head = self
    while (head != None):
      link_list += "(\"" + head.word + "\", " + str(head.count) + ", " + str(head.prob) + ") "
      head = head.nextw
    return link_list

 
