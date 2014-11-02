from markovdict import *
import io

def main():
  textfile = io.open("plathbelljar2.txt", "r", encoding='utf-8')
  line = textfile.readline()
  strlist = []
  while (line):
    strlist += line.split()
    line = textfile.readline()

  sonnet_model = markovdict(strlist)
  print
  for i in xrange(14):
    print sonnet_model.get_sentence()
  print
main()
