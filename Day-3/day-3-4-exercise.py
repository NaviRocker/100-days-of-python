# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if size == "S":
  initial_price = 15
  if add_pepperoni == "Y":
    initial_price += 2
elif size == "M":
  initial_price = 20
  if add_pepperoni == "Y":
    initial_price += 3
else:
  initial_price = 25
  if add_pepperoni == "Y":
    initial_price += 3

if extra_cheese == "Y":
  bill = initial_price + 2

print(f"Your final bill is ${bill}")