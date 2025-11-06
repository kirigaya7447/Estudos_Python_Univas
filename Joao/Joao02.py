nomes = ["ana", "paula", "pedro", "otavio", "antonio", "giulia", 
         "luis", "leilaine", "wanderley", "celso"]

print("Três primeiros nomes são:", nomes[:3])

nomes.sort()
print("Nomes em ordem alfabética:")

for nome in nomes:
    print(nome)

print("\nNomes em maiúsculo:\n")
for nome in nomes:
    print(nome.upper())
