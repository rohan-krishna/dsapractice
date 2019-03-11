import array

# Array to include signed integers
arr = array.array('i', [1,2])

# print the original array
print("The newly created Array is:", end=" ")

for i in range(0,2):
    print(arr[i], end=" ")

print("\r")

# append a new element to array
arr.append(3)

#array insertion
arr.insert(2, 5)

print("\r")

# printing array after insertion 
print ("The array after insertion is : ", end="") 
for i in range (0, 4): 
    print (arr[i], end=" ") 
