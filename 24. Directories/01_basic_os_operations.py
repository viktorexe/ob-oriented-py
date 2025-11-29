# OS Module will be used

# Get path of directory
import os 
print(os.getcwd())

# What all inside directory
print(os.listdir())

# Create a test folder in workspace
os.mkdir("Test")

# Check if something exists
print(os.path.exists("Test"))

# Change current dir
os.chdir("Test")
print(os.getcwd())

# Delete
import os
os.rmdir("Test")
