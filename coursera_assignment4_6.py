#this code is for coursera python for everybody assignment 4.6
#########################################################################
#4.6 Write a program to prompt the user for hours and rate per hour using
#input to compute gross pay. Award time-and-a-half for the hourly rate for
#all hours worked above 40 hours. Put the logic to do the computation of
#time-and-a-half in a function called computepay() and use the function to do
#the computation. The function should return a value. Use 45 hours and a rate
#of 10.50 per hour to test the program (the pay should be 498.75). You should
#use input to read a string and float() to convert the string to a number.
#Do not worry about error checking the user input unless you want to - you can
#assume the user types numbers properly. Do not name your variable sum or use
# the sum() function.


def computepay(h,r):
    hourrate  = float(40) * float(r)
    val = (float(h)%40)
    vali = val * float(r)
    valis = vali * 1.5
    value = hourrate + valis
    return value

hrs = input("Enter Hours:")
hr = float(hrs)
rate = input("enter rate per hour")
ra = float(rate)
if hr <= 40:
   hourRate = float(hr) * float(ra)
   print (hourRate)
elif hr >= 40:
     p = computepay(hr,ra)
     print(p)
