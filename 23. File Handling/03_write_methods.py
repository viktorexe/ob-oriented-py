# Write methods are like read methods, difference is that file contents are modified
# Manually creating a file
import logging
logging.basicConfig(filename='write_operations.txt', level=logging.INFO)

# write(): Write in file, only accepts string
a = open('write_operations.txt', 'w')
a.write('Line 1\n')
a.write('Line 2')
a.close()

# writelines(): Write multiple lines at once
b = open('write_operations.txt', 'w')
lines_list = ['Line 1\n', 'Line 2\n', 'Line 3\n']
b.writelines(lines_list)
b.close

