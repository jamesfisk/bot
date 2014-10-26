from markovdict import *
import io

def main():
  string = io.open("Sonnets.txt", "r").read() 
  strlist = string.split()

  sonnet_model = markovdict(strlist)
  #sonnet_model.save_model("sonnet_dict.txt")
  #for item in sonnet_model.model:
    #print item, ":  ", str(sonnet_model.model[item])
  #print sonnet_model.pi
  print
  for i in xrange(14):
    print sonnet_model.get_sentence()
  print
  """
  head = node(strlist[0])
  for elt in strlist:
    head = head.insert(elt)
  #print(str(head))
  head.calculate_prob()
  #print(str(head))
  iterator = head
  sumall = 0.0
  for j in xrange(14):
    for i in xrange(10):
      print head.choose(),
    print
  """
main()
