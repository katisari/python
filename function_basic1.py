def a():
    return 5
print(a()) 
OUTPUT: 5    


def a():
    return 5
print(a()+a())     
OUTPUT: 10


def a():
    return 5
    return 10
print(a())     
OUTPUT: 5


def a():
    return 5
    print(10)
print(a())     
OUTPUT: 5


def a():
    print(5)
x = a()
print(x)     
OUTPUT: 5 NONE


def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))   
OUTPUT: 3, 5, ERROR


def a(b,c):
    return str(b)+str(c)
print(a(2,5))
OUTPUT: 25


def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a)  
OUTPUT: ERROR


def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))     
OUTPUT: 7, 14, 21


def a(b,c):
    return b+c
    return 10
print(a(3,5))     
OUTPUT: 8


b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)  
OUTPUT: 500, 500, 300, 500


b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
OUTPUT: 500,500,300,500  


b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
OUTPUT: 500, 500, 300, 300


def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
OUTPUT: 1,3,2


def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
OUTPUT: 1, 3, 5, 10
