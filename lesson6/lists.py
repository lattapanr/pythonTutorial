# String methods

users = ['Noey', 'Noon', 'Mum']

data = ['Noey', 30, True]

empy_list = []

print("Noey" in users) # True
print("Noey" in empy_list) # False

print(users[0]) # Noey
print(users[-1]) # Mum
print(users[-2]) # Noon

print(users.index('Noon')) # 1

print(users[0:2]) # ['Noey', 'Noon']
print(users[1:]) # ['Noon', 'Mum']
print(users[-3:-1]) # ['Noey', 'Noon']

print(len(data)) # 3

users.append('Apec')
print(users) # ['Noey', 'Noon', 'Mum', 'Apec']

users += ['Dickie']
print(users) # ['Noey', 'Noon', 'Mum', 'Apec', 'Dickie']

users.extend(['Michelle', 'David'])
print(users) # ['Noey', 'Noon', 'Mum', 'Apec', 'Dickie', 'Michelle', 'David']

# users.extend(data)
# print(users) # ['Noey', 'Noon', 'Mum', 'Apec', 'Dickie', 'Michelle', 'David', 'Noey', 30, True]

users.insert(0, 'Bob')
print(users)

users[2:2] = ['Eddie', 'Alex']
print(users)

users[1:3] = ["Robert", "Sarah"]
print(users)


users.remove("Robert")
print(users)

print(users.pop())

del users[0]
print(users)

#del data - once delete the variable it cant be called again else it would give an error
data.clear()
print(data)

users.insert(0, "Noey")
print(users)

users.remove("Sarah")
users.remove("Alex")
print(users)

users.append("David")
print(users)

users[1:2] = ['apec'] # lowercase comes after uppercase
users.sort()
print(users)

users.sort(key=str.lower)
print(users)


# Number methods
nums = [5, 56, 3, 8, 100]

nums.reverse()
print(nums) # [100, 8, 3, 56, 5]

# nums.sort(reverse=True)
# print(nums) # [100, 56, 8, 5, 3]

print(sorted(nums, reverse=True)) # not modify the original array

# copying a list
nums_copy = nums.copy()
my_nums = list(nums)
my_copy = nums[:]

print(nums)
print(my_nums)
my_copy.sort()
print(my_copy)

print(type(nums)) # <class 'list'>

my_list = list([16, "Noey", True])
print(my_list)

print("")

# Tuples - cannot be changed

my_tuple = tuple(("Noey", 30, True))
another_tuple = (3,4,1,6,2,2, 2)

print(my_tuple)
print(type(my_tuple))
print(type(another_tuple))

new_list = list(my_tuple)
new_list.append("Noon")
new_tuple = tuple(new_list)
print(new_tuple)

(one, two, *hey) = another_tuple
print(one) # 3
print(two) # 4
print(hey) # [1, 6, 2, 2]

print(another_tuple.count(2)) # 3









