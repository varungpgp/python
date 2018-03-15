#this code is excersice of python for everybody 5.1
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
