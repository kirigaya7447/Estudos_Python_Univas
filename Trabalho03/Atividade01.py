ano = int(input("Digite seu ano de nascimento: "))

diferenca = 2025 - ano
if(diferenca >= 18):
    print("Você pode votar!")
elif(diferenca < 18):
    print("Você não pode votar!")
