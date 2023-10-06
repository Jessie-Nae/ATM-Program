#-----------------------TASK
'''Assuming you have a list : 12,10,32,3,66,17,42,99,20 stored in 'xy' variable:
    A: write a loop that prints each of the number on a new line.
    B: write a loop that prints each number and its square on a new line.
    C: write a loop that adds all the number from the list into a  var called 'total' which you first have to initialize as = '0'.
    D: print the product of all the numbers in the list.
    '''

#----------------------SOLUTION
#create a 'list'
xy = [12,10,32,3,66,17,42,99,20]


# -A-:using 'for' loop to loop through each value of the list
print("Answer to question A :")

for item in xy:
    print(item)


# -B-:using 'for' loop to tranverse through each value of the list and print its square
print("Answer to question B :")

for item in xy:
    square = item*item
    print(item,square)


# -C-:using 'for' loop and arithmetic operator 
print("Answer to question C :")

total = 0
for item in xy:
    total += item 
    print(total)



# -D-:using arithmetic operator to calculate the product of the list
print("Answer to question D :")

product =1
for item in xy:
    product = product*item

print(product)