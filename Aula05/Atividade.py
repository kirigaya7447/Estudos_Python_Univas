print("Tabuada:")
num = int(input("Digite um número: "))
cont = 0
while(cont <= 10):
    print(num, "*", cont, "=", (num * cont))
    cont += 1

somaTudo = num
for soma in range(num):
    somaTudo += soma

print("\nA soma de todos os números até o", num, "é de", somaTudo)

print("\nCrie um usuário e senha:\n")
user = str(input("Digite seu nome de usuário: "))
senha = str(input("Digite sua senha: "))
while(senha == user):
    senha = str(input("Sua senha não pode ser igual ao usuário!\n Digite sua senha: "))

print("\nNúmero ímpares de 1 a 50:")
for isto in range(50):
    if(isto % 2 != 0):
        print(isto)

print("\nPotência:")
n1 = int(input("Digite um número: "))
n2 = int(input("Digite uma potência: "))

print(n1, "elevado a", n2, "é", (n1**n2))

print("\nFatorial:")
fat = int(input("Digite um número: "))

fatorando = fat
fatOriginal = fat
while(fat > 1):
    fatorando = fatorando * (fat - 1)
    fat -= 1

print("O fatorial de", fatOriginal, "é", fatorando)