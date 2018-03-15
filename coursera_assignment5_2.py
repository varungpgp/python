#this code is for python for everybody assignment 5.2
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
