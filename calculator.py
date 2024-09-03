num1 = input("Enter any 1st number: ")
oprator = input("Enetr oprater(+,-,*,/): ")
num2 = input("Enter any 2nd number: ")
num1 = int(num1)
num2 = int(num2)

if oprator == '+':
    result = num1+num2
elif oprator == '-':
    result = num1-num2
elif oprator == '*':
    result = num1*num2
elif oprator == '/':
    if num2 != 0:
        result=num1/num2
    else:
        result="Error! division by zero"
else:
    result ="Invalid oprators"
print("The result is: ",result)


