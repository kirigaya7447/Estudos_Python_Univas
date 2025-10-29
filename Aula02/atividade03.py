num = int(input("Digite um número: "))
num1 = int(input("Digite outro número: "))
num2 = int(input("Digite outro número: "))

if(num < num1 and num < num2):
    if(num1 < num2):
        print(num, num1, num2)
    elif(num1 > num2):
        print(num, num2, num1)

elif(num1 < num and num1 < num2):
    if(num < num2):
        print(num1, num, num2)
    elif(num > num2):
        print(num1, num2, num)

elif(num2 < num and num2 < num1):
    if(num1 < num):
        print(num2, num1, num)
    elif(num1 > num):
        print(num2, num, num1)