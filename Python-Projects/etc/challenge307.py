thisArray1 = range(4) # Step 1
thisArray2 = reversed(range(4)) # Step 2
thisArray3 = reversed(range(2, 9, 2)) # Step 3

def arrayLoop(x):
    for i in x:
        print(i)
    print("\n")

arrayLoop(thisArray1)
arrayLoop(thisArray2)
arrayLoop(thisArray3)