l1 = int(input("Digite o primeiro lado do triângulo: "))
l2 = int(input("Digite o segundo lado do triângulo: "))
l3 = int(input("Digite o terceiro lado do triângulo: "))

if(l1 == l2 and l2 == l3):
    print("Triângulo equilátero!")
elif(l1 == l2 and l1 != l3 or l1 == l3 and l1 != l2 or l2 == l3 and l2 != l1):
    print("Triângulo isósceles!")
else:
    print("Triângulo escaleno!")