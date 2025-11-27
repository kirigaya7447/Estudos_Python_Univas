d = {"nome" : "", "idade" : "", "telefone" : "", "endereco" : ""}

d.update({"nome" : input("Digite seu nome: ")})
d.update({"idade" : input("Digite sua idade: ")})
d.update({"telefone" : input("Digite seu telefone: ")})
d.update({"endereco" : input("Digite seu endereço: ")})

titulos = d.keys()
valores = d.values()

for cont in titulos:
    print(cont, "|", end="")

print("")
for cont1 in valores:
    print(cont1, "|", end="")
