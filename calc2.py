import sys

x = sys.argv[1]
y = sys.argv[2]
a = sys.argv[3]

if a == 1:
    z = int(x)+int(y)
    print(z)
elif a == 2:
    z = int(x)-int(y)
    print(z)