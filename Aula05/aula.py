cont = 0
print("Loop while: ")
while(cont < 5):
    print(cont)
    cont += 1

print("\n")
print("_________________________________\nLoop for:")

for cont in range(5):
    print(cont)
    cont += 1 

print("_________________________________\nFor em listas:")

lista = ["A", "E", "I", "O", "U"]

for a in lista:
    print(a)

print("_________________________________\Tabuada:")

num = int(input("Digite um número: "))

if(num >= 1 and num <= 10):
    cont = 1
    while(cont <= 10):
        print(num, "*", cont, "=", (num*cont))
        cont += 1