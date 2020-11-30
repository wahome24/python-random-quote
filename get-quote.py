import random
result =random.randint(0,13)

def trial():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[result])

trial()