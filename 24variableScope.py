# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally scoped versions of a variable can be created

name = "eduardo" # global scope (available inside & outside functions)

def display_name():
    name = "bregalda"    # local scope (available only inside this function)
    print(name)


display_name()
print(name)       