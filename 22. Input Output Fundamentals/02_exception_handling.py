# Instead of crashing the program we print an error message
# try:
#     code
# except:
#     error aaya toh
# else:
#     error nahi aaya toh
# finally:
#     hamesha chalega



try:
    num = int(input("Please enter a number: "))
except:
    print("An internal error occured!")
else:
    print('Entered number is:',num)
finally:
    print("End of program")