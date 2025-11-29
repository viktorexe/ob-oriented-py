# Basic read operations on file
# Again manually creating reading_methods.txt if not present using logging
import logging 
logging.basicConfig(filename = 'reading_methods.txt', level=logging.INFO)
logging.info("Start of program")
logging.info("Program has been started")

# read(): Reads everything
a = open('reading_methods.txt', 'r')
data = a.read()
print(data) # Whole fle becomes a string
a.close()

# readline(): Reading line by line
b = open('reading_methods.txt', 'r')    
line1 = b.readline() # By default reads first line
print(line1)
line2 = b.readline() # Reads line 2
b.close()

# readlines(): Makes different lines as elements of a list
c = open('reading_methods.txt', 'r')
lines = c.readlines()
print(lines)
c.close()