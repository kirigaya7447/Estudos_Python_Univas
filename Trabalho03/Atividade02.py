senha = input("Digite a senha: ")

while(senha != "1234"):
    print("Senha inválida!")
    print("Acesso negado!")
    senha = input("Redigite a senha: ")

print("Senha correta!")
print("Acesso permitido!")