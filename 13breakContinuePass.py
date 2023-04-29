# Loop control statements = change a loops execution from its normal sequence

# break = used to trminate the loop entirely
# continue = skips to the next itineration of the loop
# pass = does nothing, acts as a placeholder

while True:
    name = input("enter your name: ")
    if name != "":
        break

phoneNumber = "123-456-7890"

for i in phoneNumber:
    if i == "-":
        continue
    print(i, end="")

for i in range(0,21):
    if i == 13:
        pass
    else:
        print(i) 
