from linkedwordlist import *

def main():
  string = "This Awful sentence has many Words words Words"
  strlist = string.split()
  head = node(strlist[0])
  for elt in strlist:
    head = head.insert(elt)
  print(str(head))
  head.calculate_prob()
  print(str(head))
  iterator = head
  sumall = 0.0
  while(iterator != None):
    sumall += iterator.prob
    print(str(sumall))
    iterator = iterator.nextw

main()
