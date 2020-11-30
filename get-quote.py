def trial():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[0])

trial()