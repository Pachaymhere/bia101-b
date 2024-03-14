 # creation of array
array1 = [1,2,3,"thimphu", 2.5]
print(array1)

# retrieving
element1 = array1[0]
element2 = array1[4]
print (element1)
print (element2)
last_element = array1[-1]
print(last_element)
#modifying elements
array1[0] = 10
print (array1)

#getting number of elements in an arrey
no_of_elements=len(array1)
print (no_of_elements)

#slicing
elements = array1[0:4]
print (elements)

arr1=[1,10]
arr2=['thimphu','wangdue']
arr3=arr1+arr2
print(arr3)

number_to_check = 2
result = number_to_check in arr1
print('result', result)

#add elements
arrVariable=[1,2,3]
arrVariable.append(4)
# insert at a sepcific index
arrVariable.insert(1,10)
print(arrVariable)
#sort array
arrVariable.sort()
print(arrVariable)

#pop
arrVariable.pop(0)

stackVar = []
#adding to stack
stackVar.append(4)
stackVar.append(2)
stackVar.append(9)
stackVar.append(1)
print ('after appending', stackVar)
element = stackVar.pop()
print('after poppong', stackVar)


