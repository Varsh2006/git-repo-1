def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

temp=float(input('enter the temperature:'))

print('Temperature convertor')
print('1.Celsius to Fahrenheit')
print('2.Fahrenheit to Celsius')
print('3.Exit')

while(True):
    ch=int(input('enter ur choice:'))
    if ch in (1,2,3):
        if ch==1:
          result = celsius_to_fahrenheit(temp)      
          print(f"{temp}°C is equal to {result}°F")
        elif ch==2:
           result = fahrenheit_to_celsius(temp)
           print(f"{temp}°F is equal to {result}°C")
        elif ch==3:
           break
    else:
        print('Invalid choice try again')