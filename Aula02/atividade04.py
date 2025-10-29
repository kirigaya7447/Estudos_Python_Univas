idade = int(input("Digite sua idade: "))

if(idade < 16):
    print("Proibido voto!")
elif(idade >= 70):
    print("Voto opcional!")
elif(idade >= 16 and idade < 18):
    print("Voto opcional!")
elif(idade >= 18 and idade < 70):
    print("Voto obrigatório!")