welcome_message = """Welcome to the Python Cafe!
Here is what is available"""

item1= "1 - Bread - $1.00"
item2 = "2 - Water - $0.10"
item3 = "3 - Bonbons - $5.00"

print(welcome_message)
print(item1)
print(item2)
print(item3)

chosen_item = int(input("Type which item number you would like\n"))
amount = int(input("How many?\n"))

if chosen_item == 1:
  print(f"You chose {amount} Bread")
  cost = 1.0 * amount
  print(f"Total is ${cost}")
elif chosen_item == 2:
  print(f"You chose {amount} Water")
  cost = 0.1 * amount
  print(f"Total is ${cost}")
elif chosen_item == 3:
  print(f"You chose {amount} Bonbon")
  cost = 5.0 * amount
  print(f"Total is ${cost}")
else:
  print("Something went wrong")
