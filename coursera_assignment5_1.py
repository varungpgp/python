#this code is excersice of python for everybody 5.1
##############################################################################
#Exercise 1: Write a program which repeatedly reads numbers until the user
#enters "done". Once "done" is entered, print out the total, count, and average
#of the numbers. If the user enters anything other than a number, detect their
#mistake using try and except and print an error message and skip to the next number.


Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.333333333333333
va = 0.0
count = 0
while 1:
      var = input("enter a number: ")
      if var == 'done':
         break
      try:
          v = float(var)
      except:
             print("bad data invalid input")
      va = va + v
      count = count + 1
print("Total sum:",va)
print("count:",count)
print(va,count,va/count)
