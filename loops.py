#loop over an array
fruits = ['a','b','c']
for p in fruits:
    print (p)

# for loop through each evelement
# at each stage, if the element is 'a'
# print true
for e in fruits:
    if e == 'a':
        print('True')
# loop through each evelement
# at each stage, if the element is 'c'
# print true
for e in fruits: # 1.e = 'a', 2.e = 'b 3. e = 'c'
    if e == 'c':
        print('True')
    if e == 'b':
        print('True')

# Iterate over a string
greeting = "Hello"
for char in greeting:
    print(char)
    # Exercise: check if the string contains vowel

#Iterate over a range
    for i in range(20):
        print (10)
        print (11)
        print (12)
        print ('----------')
        for i in range(5,14,2): #5-13
            print(i)

#! while loops 
#basic while loop

count = 0
while count < 5:
    print (count)
    count = count + 1 #output: 0 1 2 3 4  

#user input string is unknown
#print every char of the string     
s = 'pachay m'
counter = 0
length_s =  len(s)   
print('counter:', counter)
print('len s:', length_s)
print('going in loop')
while counter < length_s:
    print('counter:', counter)
    char = s[1]
    print(char)
    counter = counter + 1
# 0 1 2 3 4 