# Task is to create a calculator that works with arguments

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
elif a == str("d"):
    z = int(x)/int(y)
    print(z)
elif a == str("m"):
    z = int(x)*int(y)
    print(z)