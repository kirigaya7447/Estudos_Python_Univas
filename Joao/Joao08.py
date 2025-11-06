tupla = (0,1,2,3,4,5,6,7,8,9)

print("Números até o quarto elemento:", tupla[:4])

for nums in tupla:
    if(nums % 2 == 0):
        print("Número par: ", nums)