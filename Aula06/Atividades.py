dic = {"nome": "Carlos", "idade": 28, "profissao": "Desenvolvedor"}

print(dic["nome"], "atua como", dic["profissao"])

print("\n________________\n")

dic.update({"cidade": "Belo Horizonte"})

print(dic)

print("\n________________\n")

dic.pop("idade")

print(dic)

print("\n________________\n")

print("os índices do dicionário são: ", list(dic.keys()))
print("Os valores do dicionário são: ", list(dic.values()))

print("\n________________\n")

dic.update({"idade": 28})

print("Idade atual é", dic["idade"])

dic.update({"idade": 29})

print("A idade ajustada é", dic["idade"])
