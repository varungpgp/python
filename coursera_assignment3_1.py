#this code is for coursera python for everybody assignment 3.1
#######################################################################3
#Write a program to prompt the user for hours and rate per hour using
#input to compute gross pay. Pay the hourly rate for the hours up to 40
#and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45
# hours and a rate of 10.50 per hour to test the program
#(the pay should be 498.75). You should use input to read a string and float()
# to convert the string to a number. Do not worry about error checking the user
#input - assume the user types numbers properly.

hrs = input ("Enter hours: ")
hour = float(hrs)
rate = input ("rate per hour: ")
rates = float(rate)
if hour <= 40:
   hourRate = float(hour) * float(rate)
   print (hourRate)
elif hour >= 40:
     hourrate  = float(40) * float(rate)
     val = (float(hour)%40)
     vali = val * float(rate)
     valis = vali * 1.5
     value = hourrate + valis
     print(value)
