for i in range(10):
    for j in range(1):
        print("*", end=" ")
    for j in range(i):
        print(" " ,end=" ") 
    print("*",end=" ")
    for j in range(8-i):
        print(" ",end=" ")
    if i !=9:
        for j in range(1):
            print("*",end=" ")
    print()