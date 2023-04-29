# nested loops = The "inner loop" will finish all of it's iterations before finishing one iteneration of the "outer loop"

rows = int(input("how many rows?: "))
columns = int(input("how many columns?: "))
symbol = input("enter a symbol to use:")

for i in range(rows):
    for j in range(columns):
        print(symbol,end="")   #end="" serve para nao gerar nova linha a cada iteração
    print()