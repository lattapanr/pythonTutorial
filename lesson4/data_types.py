# String data type

# literal assignment
first = 'Lattapan'
last = 'Rachatapoonsawat'

# print(type(first))
# print(type(first) == str)
# print(isinstance(first,str))

# constructor function
# gelato = str('Pistacchio')
# print(type(gelato))
# print(type(gelato) == str)
# print(isinstance(gelato,str))

# Concatanation
# fullname = first + ' ' + last
# print(fullname)

# fullname += '!'
# print(fullname)

# Casting a number to a string
# decade = str(1990)
# print(type(decade))
# print(decade)

# statement = 'I like indie music from the' + ' ' + decade + 's.'
# print(statement)

# Multiple lines
multiline = '''
How you doin'

I'm Joey

                    Ugh
'''
print(multiline)

print('')

# Escaping special characters
sentence = 'I\'m hangry\tHey!\n\nWhat\'s the deal???'
print(sentence)

print('')

# String Methods

print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace('Joey', 'Noey'))
print(multiline)

print(len(multiline)) # 50
      
multiline += '                                         '
multiline = '                      ' + multiline
print(len(multiline)) # 113

print(len(multiline.strip())) # 48
print(len(multiline.lstrip())) # 90
print(len(multiline.rstrip())) # 71

print('')

# Build a menu
title = 'menu'.upper()
print(title.center(20, '=')) # ========MENU========
print('Milk'.ljust(16,'.')+ '$0.4'.rjust(4)) # Milk............$0.4
print('Bagle'.ljust(16,'.')+ '$2'.rjust(4)) # Bagle...........  $2
print('Cake'.ljust(16,'.')+ '$3'.rjust(4)) # Cake............  $3

print('')

# String Index Value
print(first[1]) # a
print(first[-1]) # n
print(first[1:-1]) # attapa
print(first[1:]) # attapan

print('')

# Some methods return boolean data
print(first.startswith('L')) # True
print(first.endswith('A')) # False

print('')

# Boolean data type
my_value = True 
x = bool(False)
print(type(x))
print(isinstance(my_value,bool))

print('')

# Numeric data types

# Integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int)) # <class 'bool'>

print('')

# Float type
gpa = 3.50
y = float(2.67)
print(type(gpa)) # <class 'int'>

print('')

# Complex type
comp_value = 5+3j
print(type(comp_value)) # <class 'complex'>
print(comp_value.real) # 5.0
print(comp_value.imag) # 3.0

print('')

# Buit-in functions for numbers

print(abs(gpa)) # 3.5
print(abs(gpa * -1)) # 3.5
print(round(gpa)) # 4
print(round(gpa, 1)) # 3.5

import math # should be moved to the top of the file

print(math.pi) # 3.141592653589793
print(math.sqrt(64)) # 8.0
print(math.ceil(gpa)) # 4
print(math.floor(gpa)) # 3

print('')

# Casting a string to a number
zipcode = '10001'
zip_value = int(zipcode)
print(type(zip_value)) # <class 'int'>

# Error if your attemp to cast incorrect data

zip_value = int('New York')



