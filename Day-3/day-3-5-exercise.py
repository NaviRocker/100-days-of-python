print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
combName = name1 + name2
combLower = combName.lower()
t = combLower.count("t")
r = combLower.count("r")
u = combLower.count("u")
e = combLower.count("e")
true = t + r + u + e
l = combLower.count("l")
o = combLower.count("o")
v = combLower.count("v")
love = l + o + v + e
loveScore = str(true) + str(love)
loveInt = int(loveScore)
if (loveInt < 10) or (loveInt > 90):
  print(f"Your score is {loveInt}, you go together like coke and mentos.")
elif (loveInt <= 50) and (loveInt >= 40):
  print(f"Your score is {loveInt}, you are alright together.")
else:
  print(f"Your score is {loveInt}")