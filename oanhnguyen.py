#VARIABLE

##Declare
a=1
b=5
print(a+b)
print('I have'+' '+ str(a) +' '+'apple')         #str to convert int to str

##Loop
a=a+10                                           #update value by adding 2
a+=10                                            #update value by adding 2
a-=3                                             #update value by substract 3 
print (a)

##If
if a>20:
    print('Too much')
elif a>15:                                       #add AND condition
    print('Much')
    if a>17:                                     #nest condition to check a condition, only if another condition is true.
       print('Fairly much')
else:
    print('Little')


#ARRAY                                            # Fixed lenght, same datatype, stored contiguously in memory
##Declare
myFruits = ['banana','apple','orange']
##Manipulate
myFruits.append('oanh')                           #insert new value to the end
myFruits.insert(0,'uyen')                         #insert new value into a specific position
myFruits.pop(2)                                   #delete a value of a specific position
print(myFruits)
##Count length
print(len(myFruits))
##Loop array                                      #to view one by one values in the array
for fruit in myFruits:
  print(fruit)
  if fruit=='banana':
   print('I have a banana')
   break
#  OR
# for i in range(len(myFruits)):                  #Range to count variable for the indexes
#   print(myFruits[i])


#LOOP
## While Loop                                     #Best to use when you DON'T know how many times the code should run.
import random                                     #Import the random module to use its functionality  

dice = random.randint(1, 6)                       # Generate a random integer between 1 and 6 and store it in 'dice'  
print(dice)                                       
count = 1                                         # Initialize a counter for the number of rolls  

while dice != 6:                                  # Continue rolling until a 6 is rolled  
    dice = random.randint(1, 6)                   # Roll the dice again  
    print(dice)                                   # Print the result of each roll  
    count += 1                                    # Increment the counter  

print('You got 6!')                               # Print a message when a 6 is rolled  
print('You rolled', count, 'times')               # Print the total number of rolls  

## For Loop                                       # Best to use when you know how many times the code should run.
for i in range(10,0,-1)                           # Iterate from 10 down to 1 (exclusive of 0) with a step of -1.
print(i)                                          # Print the current value of 'i' in each iteration.
print('Liftoff!')