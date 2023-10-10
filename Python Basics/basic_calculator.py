num1 =  float(input("Enter 1st number:"))
num2 =  float(input("Enter 2nd number:"))
op = input("Enter the operator: ")
# # result = int(num1) * int(num2) #for int
# result = float(num1) * float(num2)
# print("The multiplication of {num1} and {num2} is: ", result)
# # print("The multiplication of" + int(num1) + "and" + int(num2) + "is: ", result)

if op == "+":
    print(num1 + num2)
elif op == "-":
    print (num1 - num2 )
elif op == "*" :
    print(num1 * num2)
elif op == "/" :
    print(num1 / num2)
else:
    print("Enter a valid operator")