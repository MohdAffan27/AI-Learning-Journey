# Sorting Arrays
# The np.sort() function sorts NumPy arrays in ascending order and can also sort structured arrays based on specific fields.

# Note: Strings with prefix b'' indicate byte strings (fixed-length string in NumPy). S10 means each string can store up to 10 bytes.

import numpy as np

dtype = [('name', 'S10'), ('year', int), ('cgpa', float)]
vals  = [('Hrithik', 2009, 8.5),
         ('Ajay',    2008, 8.7),
         ('Pankaj',  2008, 7.9),
         ('Aakash',  2009, 9.0)]

a = np.array(vals, dtype=dtype)

print(np.sort(a, order='name'))
print(np.sort(a, order=['year', 'cgpa']))
