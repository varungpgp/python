#this code is for coursera python for everybody assignment 3_3
score = input("Enter Score: ")
score1 = float(score)
if score1 < 0.6:
    print("F")
elif score1 > 1.0:
    print("Error! please enter number between 0 t0 1.0")
elif score1 >= 0.9:
    print("A")
elif score1 >= 0.8:
    print("B")
elif score1 >= 0.7:
    print("C")
elif score1 >= 0.6:
    print("D")
