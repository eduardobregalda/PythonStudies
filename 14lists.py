# list = used to store multiple itens in a single variable

food = ["pizza","hamburguer","hotdog","spaghetti","pudding"]

food[0] = "sushi"

food.append("ice cream")
food.remove(food[2]) # or food.remove("hotdog")
food.pop() # remove the last iten
food.insert(1,"cake")
food.sort() # sort in alphabetical order
#food.clear()

for x in food:
    print(x)