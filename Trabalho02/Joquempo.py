import random

print("Joquempô")
contador = 0
pontosJ = 0;
pontosC = 0;

nome = input("Digite seu nome: ")
entrada = int(input("Escolha uma jogada\n(1-Tesoura)\n(2-Pedra)\n(3-Papel)\nOpção selecionada: "))

while(entrada != 0):
    alea = random.randint(1,3)

    if(alea == entrada):
        print("Empate!")
        pontosC += 1
        pontosJ += 1

    elif(alea == 1 and entrada == 2):
        print("Jogador", nome," ganhou!")
        print("Pedra ganha de tesoura")
        pontosJ += 1

    elif(alea == 1 and entrada == 3):
        print("Computador ganhou!")
        print("Papel perde de tesoura")
        pontosC += 1

    elif(alea == 2 and entrada == 1):
        print("Computador ganhou!")
        print("Tesoura perde de pedra")
        pontosC += 1

    elif(alea == 2 and entrada == 3):
        print("Jogador", nome," ganhou!")
        print("Papel ganha de pedra")
        pontosJ += 1

    elif(alea == 3 and entrada == 1):
        print("Jogador", nome," ganhou!")
        print("Tesoura ganha de papel")
        pontosJ += 1

    elif(alea == 3 and entrada == 2):
        print("Computador ganhou!")
        print("Pedra perde de papel")
        pontosC += 1
        
    else:
        print("Jogada inválida!")

    entrada = int(input("Escolha uma jogada\n(0-Sair do jogo)\n(1-Tesoura)\n(2-Pedra)\n(3-Papel)\nOpção selecionada: "))

print("O placar do jogo ficou:\n", nome, " | ", "Máquina\n", pontosJ, " | ",pontosC)