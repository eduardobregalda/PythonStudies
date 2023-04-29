# for loop =    a statement that will execute it's block of code
#                      a limited amount of times
#
#                     while loop = unlimited
#                     for loop = limited

import time

#for i in range(10):          conta de 1 a 10  se fosse  print(i) printaria de 0 a 9
    #print(i+1)

#for i in range(50,100+1,2):     conta de 50 a 100 de 2 em 2 
    #print(i)

#for i in "Bro Code":            printa letra por letra
    #print(i)

for seconds in range(10,0,-1):       # -1 pois é contagem regressiva de 1 em 1
    print(seconds)
    time.sleep(1)
print("Happy New Year!")