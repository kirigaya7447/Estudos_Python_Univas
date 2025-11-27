def area(tam, larg):
    area = tam * larg
    return area

larg = int(input("Digite a largura do terreno: "))
tam = int(input("Digite o tamanho do terreno: "))
a = area(tam, larg)

print("A área total do terreno é", a)