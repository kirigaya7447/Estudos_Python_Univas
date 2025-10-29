a = input("Digite um lado do triângulo: ")
a = int(a)
b = input("Digite um lado do triângulo: ")
b = int(b)
c = input("Digite um lado do triângulo: ")
c = int(c)

if(a != b) and (a != c) and (b != c):
    print("Escaleno")
elif(a == b) and (b == c):
    print("Equilátero")
else:
    print("Isósceles")
