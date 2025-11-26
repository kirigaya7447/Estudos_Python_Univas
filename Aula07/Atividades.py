def linha():
    print("\n____________________________\n")

def par(num):
    if(num % 2 == 0):
        print("Número par!")
    else:
        print("Número ímpar!")


def media(a,b,c):
    media = (a + b + c) / 3
    return media

def mensagem():
    print("Saudações patriotas!")

def dobro(num):
    num = num * 2
    return num

def maior(n1, n2):
    if(n1 > n2):
        maior = "O maior número é " + str(n1)
    elif(n2 > n1):
        maior = "O maior número é " + str(n2)
    else:
        maior = "Os números são iguais!"
    return maior

def mult(n1, n2):
    mult = n1 * n2
    return mult

def nomeIdade(nome, idade):
    dic = {"nome": nome, "idade": idade}
    return dic

def quadrado(lado):
    lado = lado ** 2
    return lado 

print(par(2))
linha()
print(media(4,5,6))
linha()
mensagem()
linha()
print(dobro(22))
linha()
print(maior(65465465, 986455164))
linha()
print(mult(123456, 987654))
linha()
print(nomeIdade("João Henrique", 20))
linha()
print(quadrado(6))