#this code is for python for everybody assignment 5.2
#############################################################################
#5.2 Write a program that repeatedly prompts a user for integer numbers until
#the user enters 'done'. Once 'done' is entered, print out the largest and
#smallest of the numbers. If the user enters anything other than a valid number
#catch it with a try/except and put out an appropriate message and ignore the
#number. Enter 7, 2, bob, 10, and 4 and match the output below


largest = 0
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        val = float(num)
    except:
           print("Invalid input")
    if smallest is None:
       smallest = val
    elif val < smallest:
         smallest = val

    elif  val > largest:
          largest = val
          large = int(largest)
          small = int(smallest)

print("Maximum is", large)
print("Minimum is", small)
