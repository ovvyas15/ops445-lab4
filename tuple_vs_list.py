# tuple_vs_list.py

# Creating tuples
t1 = ('Prime', 'Ix', 'Secundus', 'Caladan')
t2 = (1, 2, 3, 4, 5, 6)

# Retrieving values from tuples
print("Retrieving values from tuples:")
print(t1[0])           # Output: Prime
print(t2[2:4])        # Output: (3, 4)

# Checking for existence of values in tuples
print("\nChecking if values exist in tuple t1:")
print('Ix' in t1)     # Output: True
print('Geidi' in t1)  # Output: False

# Creating a list
list2 = ['uli101', 'ops235', 'ops335', 'ops445', 'ops535', 'ops635']

# Changing the value of the list
print("\nChanging value of the list:")
list2[0] = 'ica100'
print(list2[0])       # Output: ica100
print(list2)          # Output: ['ica100', 'ops235', 'ops335', 'ops445', 'ops535', 'ops635']

# Trying to change a value in a tuple (this will raise an error)
try:
    print("\nTrying to change a value in tuple t2:")
    t2[1] = 10          # This will raise a TypeError
except TypeError as e:
    print(f"Error: {e}")

# Creating a new tuple with a slice of t2
t3 = t2[2:3]
print("\nNew tuple created from a slice of t2:")
print(t3)             # Output: (3,)

# Iterating over tuple values using a for loop
print("\nIterating over values in tuple t1:")
for item in t1:
    print('item: ' + item)
