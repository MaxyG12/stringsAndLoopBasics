rainBow = input("What sentence do you want rainbow-ising?\n")
for letter in rainBow:
  if letter.lower() == "r":
    print('\033[31m', end='') #red
  elif letter.lower() == "b":
    print('\033[34m', end='') #blue
  elif letter.lower() == "g":
    print('\033[32m', end='') #green
  elif letter.lower() == "p":
    print('\033[35m', end='') #purple
  elif letter.lower() == "y":
    print('\033[33m', end='') #yellow
  elif letter.lower() == " ":
    print('\033[0m', end='') #default
  print(letter, end="")

