#this code is for coursera python for everybody assignment 4.6
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
