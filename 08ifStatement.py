# if statement = a block of code that will execute if it's condition is true

age = int(input("How old are you? "))

if age == 100:
    print("you are a century old")
elif age >= 18:
    print( "you are an adult")
elif age < 0:
    print("you havent been born yet")  
else: 
    print("you are a child")
