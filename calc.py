print("Select operation..")
print("1) Add  2)Subtract")
a = int(input("Choose: "))
b = True

while b == True:

    if a == 1 or 2:
        print("Input numbers:")
        x = int(input("First number: "))
        y = int(input("Second number: "))
        z = int(x+y or x-y)
        if a == 1:
            z == x+y
            print("Sum is: ", x+y)
        elif a == 2:
            z == x-y
            print("Sum is: ", x-y)
        c = int(input("Next calculation?  1/2:"))
        if c == 1:
            b == True
        elif c == 2:
            break
    else:
        print("Wrong input!")