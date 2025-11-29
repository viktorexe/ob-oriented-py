# When python wants to open a file form our system,
# it opens it,
# does its work,
# then closes it
# For reading, writing data
# Syntax: file = open("filename", "mode")

# Using logging to just create the sample.txt
import logging

logging.basicConfig(filename = 'sample.txt', level = logging.INFO)


# Opening
f = open("sample.txt", "w")
f.write("Hello")
f.close()

# Reading and printing 
g = open("sample.txt", "r")
data = g.read()
print(data)
g.close()

# Append
# h = open("sample.txt", "a")
# h.write("New text")
# data2 = h.write()
# h.close()