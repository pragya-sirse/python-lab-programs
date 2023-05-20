def swap():
 x = int(input("Enter value: "))
 y = int(input("Enter value: "))
 print("Before swapping a:", x)
 print("Before swapping b:", y)

 x, y = y, x
 print("After swapping a :", x)
 print("After swapping b :", y)

swap()