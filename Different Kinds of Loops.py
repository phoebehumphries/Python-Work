#~~~~~~~WHILE LOOP~~~~

count = 0
#this is what count equals to at the start
while (count < 11):
#this is while count is below 9, keep repeating the following loop.
   print ('The count is:', count)
   #printing what count equals, in the loop until we reach 9.
   count = count + 1
   #whatever count equals, you add 1 each time onto the previous number.


num_list = [1, 2, 3, 4, 5]
#the list of numbers
for num2 in (num_list):
    #stating that the list is num2, and is written as a list
    print(num2)
    #prints the list

print()
    
#the list of numbers
for num in reversed(num_list):
#stating that num would be the reverse of num_list
    print (num),
# prints 5 4 3 2 1

print()

count = 0
while count < 5:
    #this makes the code run until its less than 5.
   print (count," is  less than 5")
   #numbers go up from 0 and if they are less than 5, they are put in this.
   count = count + 1
   #adds one to the number, until it hits 5.
else:
   print (count," is not less than 5")
   #if the number is above/equal to 5 then its put in this instead.

print()

#~~~~~~~INFINTE LOOP BELOW~~~~~~


var = 1
while var == 1:
# This constructs an infinite loop
   num = input("Enter a number  :")
   print ("You entered: ", num)

print ("Good bye!")
