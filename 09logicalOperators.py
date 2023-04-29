#logical operators  (and,or) = used to check if two or more conditoional statements is true 

temp = int(input("what is the temperature outside?"))

if temp >= 0 and temp <= 30:
    print("the temperature is good today!")
    print("go outside!")
elif temp < 0 or temp > 30:
    print("the temperature is bad today!")
    print("stay inside!")