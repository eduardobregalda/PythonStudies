# dictionary =  a collection of {key:value} pairs
#                        ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

   
#print(capitals.get("Germany"))
#print(capitals.keys())
#print(capitals.values())

capitals.update({"Germany":"Berlin"}) #adding a key and a value to it
capitals.update({"USA":"Las vegas"})  #changing the value of an existing key
capitals.pop({"Germany"})
capitals.clear()

#print(capitals.items())
for key,value in capitals.items():
    print(key,value)
     