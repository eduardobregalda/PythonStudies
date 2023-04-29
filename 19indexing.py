# index operator [] = gives access to a sequence's element(element,lists,tuples)

name = "eduardo bregalda"

#if(name[0].islower()):
#    name = name.capitalize()     #if the first letter is not capitalized, the capitalize method makes the change to capitalize

first_name = name[0:8]  # [:8]
last_name = name[8:16]  # [8:] 
last_character = name[-1]

print(first_name)
print(last_name)
print(last_character)
print(name)