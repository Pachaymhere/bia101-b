#Searching
#sorting

# !problem 1
# ?input
user_input = [1,2,3,4,5,6,7,8,9,11]
# ?Q: check to see if a certain number exist in the user inpur array
n = 4
#linear search
for e in user_input:
    if e == n:
        print("Found")
    else:
     print("Not Found")

#if else, for loops, print, calculations (+.-)
     
#linear search (2nd example)
result = False #!a variable to keep track of your answer
for e in user_input:
   if e == n:
      result = True

if result == True:
   print('Found')

else: 
   print('Not Found')

#time: O(n)
input = [1,2,3,4,5]
for i in input:
    print('hi')
    if i == 1: #O(1)
         break # O(1) because it will ignore the following codes
    print('hi')
    continue #O(n)
   
input = [1,1,1,1] # O(n^2) because we have 2 (for loops)
for i in input: # O(n^2) + n
      print('i')
      for k in input:
        print('hi')

for m in input: # n
 print('bye') # O(n^2) + n. Because 1 for loop is outside the first for loop
 break #O(n^2)

