# Outer loop: Decides number of rows
# Inner Loop: Decides number of stars in each 

# *
# **
# ***
# ****
# *****


for row in range(1, 6):
    for star in range(1, row+1):
        print("*", end='')
    print()
