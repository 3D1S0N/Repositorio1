a = input("entre un número ")
b = input("entre otro número ")
c = int(input("entre un tercer número "))
d = int(input("entre un cuarto número "))

if  b > a:
    print(c+d, end=",",)
    print(a+b)
else:
    if a == b:          
        print(a,d)  

    else:
        print(a, b, c, d, sep ="")