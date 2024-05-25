num1 = 11
num2 = num1

print("Before changing the value of num2")
print("\nnum1 is : ",num1)
print("num2 is : ",num2)

print("num1 points to : ",id(num1) )
print("num2 points to : ",id(num2) )

num2 =22

print("\nAfter changing the value of num2")
print("\nnum1 is : ",num1)
print("num2 is : ",num2)

print("num1 points to : ",id(num1) )
print("num2 points to : ",id(num2) )
