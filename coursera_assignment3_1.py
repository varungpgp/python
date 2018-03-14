#this code is for coursera python for everybody assignment 3.1
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
