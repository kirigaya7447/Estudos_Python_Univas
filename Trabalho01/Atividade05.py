notaFinal = float(input("Digite sua nota final: "))

if(notaFinal >= 60):
    print("Parabéns! Você passou!")
elif(notaFinal < 60 and notaFinal >= 30):
    print("Você precisará realizar o exame de recuperação!")
else:
    print("Meus pêsames bixo! Reprovado!")