value = 1

# while value < 10:
#   print(value)
#   if value == 5:
#     break
#   value += 1


# Skip a value
# while value < 10:
#   value += 1
#   if value == 5:
#     continue
#   print(value)

# Else to add another line
# while value < 10:
#   value += 1
#   if value == 5:
#     continue
#   print(value)
# else:
#   print("Value is now equal to " + str(value))
  
names = ["Noey", "Noon", "Mum"]
# for str in names:
#   print(str)

# for str in "Mississippi":
#   print(str)

# for str in names:
#   if str == "Noon": # stop at Noon
#     break
#   print(str)

# for str in names:
#   if str == "Noon": # skip Noon
#     continue
#   print(str)

# for str in range(16):
#   print(str)

# for str in range(13,16): # 13 14 15
#   print(str)


# for str in range(0,100, 6): 
#   print(str)
# else:
#   print("Glad that\'s over.")

names = ["Noey", "Noon", "Mum"]
actions = ["sleeps", "eats", "sews", "codes"]

# for name in names:
#   for action in actions:
#     print(name + " " + action + ".")


for action in actions:
  for name in names:
    print(name + " " + action + ".")