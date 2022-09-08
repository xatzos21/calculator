import sys

x = sys.argv[1]
y = sys.argv[2]
a = sys.argv[3]

if a == str("a"):
    z = int(x)+int(y)
    print(z)
elif a == str("s"):
    z = int(x)-int(y)
    print(z)