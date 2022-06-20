import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
output = random.randint(0,len(names)-1)
print(names[output] + " is going to but the meal today")