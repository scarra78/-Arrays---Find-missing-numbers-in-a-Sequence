import random


randomlist = []


def array():
    global randomlist

    x = int(input("please enter the number of postive numbers you want to input: ")) #this is to input the ammount of number in an array or numbers 

    for i in range(0, x): #genrates x ammount of numbers.
        n = random.randint(1,99)
        if n not in randomlist:
         randomlist.append(n)

    randomlist.sort()
    y = max(randomlist)
    v = min(randomlist)
    z=v
    for i in range(v, y):   # finds missing number 
        if z not in randomlist and z%2==0:  #if you remove everything after and it will find the next missing number odd or even 
            print(randomlist)
            print(f"\n the missing positive number is {z} ")
            break
        else:
            z += 1


array()

