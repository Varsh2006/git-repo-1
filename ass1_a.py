def add(x, y):
    return(x+y)

def subtract(x, y):
    return(x-y)

def multiply(x, y):
    return(x*y)

def divide(x, y):
    return(x/y)

a=int(input('enter first number:'))
b=int(input('enter second number:'))

print('Calculator menu')
print('1.add')
print('2.subtract')
print('3.multiply')
print('4.divide')
print('5.exit')\

while(True):
    ch=int(input('enter ur choice:'))
    if ch in (1,2,3,4,5):
        if ch==1:
         c=a+b
         print('Add:',c)
        elif ch==2:
         c=a-b
         print('Subtract:',c)
        elif ch==3:
         c=a*b
         print('Multiply:',c)
        elif ch==4:
         c=a/b
         print('Divide:',c)
        elif ch==5:
         break
    else:
        print('Invalid choice try again')