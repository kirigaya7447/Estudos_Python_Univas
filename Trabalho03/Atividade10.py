def fatorial(num):
    n = num
    fat = n
    for cont in range(1, num):
        fat = fat * (n - 1)
        n -= 1
    return fat

num = fatorial(int(input("Digite um número: ")))
print("O fatorial é: ", num)