# Dictionaries
band = {
  "vocals": "Plant",
  "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)

print(type(band)) # <class 'dict'>
print(len(band)) # 2

# Access items
print(band["vocals"]) # Plant
print(band.get("guitar")) # Page

# List all keys
print(band.keys())

# List all values
print(band.values())

# List of key/vakue pairs as tuples
print(band.items())

# Verify a key exist
print("guitar" in band) # True
print("triangle" in band) # False

# Change values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})

print(band) # {'vocals': 'Coverdale', 'guitar': 'Page', 'bass': 'JPJ'}

# Remove items
print(band.pop("bass")) # JPJ
print(band) # {'vocals': 'Coverdale', 'guitar': 'Page'}

band["drums"] = "Bonham"
print(band) # {'vocals': 'Coverdale', 'guitar': 'Page', 'drums': 'Bonham'}

print(band.popitem()) # tuple - ('drums', 'Bonham')
print(band) # {'vocals': 'Coverdale', 'guitar': 'Page'}

# Delete and clear
band["drums"] = "Bonham"
del band["drums"]
print(band) # {'vocals': 'Coverdale', 'guitar': 'Page'}

band2.clear
print(band2)

del band2

# Copy dictionaries
band2 = band # create a reference
print("Bad copy!")
print(band2) # {'vocals': 'Coverdale', 'guitar': 'Page'}
print(band) # {'vocals': 'Coverdale', 'guitar': 'Page'}

band2["drums"] = "Noey"
print(band) # {'vocals': 'Coverdale', 'guitar': 'Page', 'drums': 'Noey'}

band3 = band.copy()
band3["drums"] = "Noon"
print("Good copy!")
print(band) # {'vocals': 'Coverdale', 'guitar': 'Page', 'drums': 'Noey'}
print(band2) # {'vocals': 'Coverdale', 'guitar': 'Page', 'drums': 'Noey'}

# Or use the dict() contructor function
band4 = dict(band)
print("Another good copy")
print(band3) # {'vocals': 'Coverdale', 'guitar': 'Page', 'drums': 'Noon'}

# Nested dictionaries
member1 = {
  "name": "Noey",
  "instrument": "drums"
}

member2 = {
  "name": "Noon",
  "instrument": "bass"
}

band = {
  "member1": member1,
  "member2": member2,
}

print(band) # {'member1': {'name': 'Noey', 'instrument': 'drums'}, 'member2': {'name': 'Noon', 'instrument': 'bass'}}
print(band["member1"]["name"]) # Noey

# Sets
nums = {1, 2, 3, 4}

nums2 = set((1,2,3,4))

print(nums)
print(nums2)
print(type(nums)) # <class 'set'>
print(len(nums)) # 4

# No duplicates allowed
nums = {1, 2, 3, 3}
print(nums) # {1, 2, 3}

# True is a dupe of 1 and False is a dupe of 0
nums = {1, True, False, 3, 0, 4}
print(nums) # {False, 1, 3, 4} - ignore the duplicates of 0 and 1. False comes before 0, so False is chosen and 1 comes before True, so 1 is chosen

# Check if a value is in a set 
print(2 in nums)

# But you cannot refer to an element in the set with and index position or a key


# Add a new element to a set
nums.add(8)
print(nums) # {False, 1, 3, 4, 8}

# Add elements from one set to another
more_nums = {5, 6, 7}
nums.update(more_nums)
print(nums) # {False, 1, 3, 4, 5, 6, 7, 8}

# You can use update() with lists, tuples, and dictionaries, too.

# Merge two sets to create a new set
one = {1, 2, 3}
two = {5, 6, 7}

my_new_set = one.union(two)
print(my_new_set) # {1, 2, 3, 5, 6, 7}

# Keep only the duplicates
one = {1, 2, 2}
two = {5, 1, 7}

one.intersection_update(two)
print(one) # 1

# Keep everything except the duplicates
one = {1, 2, 2}
two = {5, 1, 7}

one.symmetric_difference_update(two)
print(one) # {2, 5, 7}