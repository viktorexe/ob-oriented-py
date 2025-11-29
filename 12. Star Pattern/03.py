n = 10 

for row in range(1, n+1):
    for spaces in range(1, n-row+1):
        print(" ", end = ' ')
    for stars in range(1, row+1):
        print("*", end = ' ')
    print()