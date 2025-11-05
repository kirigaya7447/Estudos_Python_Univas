nums = [1,2,3,4,5,6,7,8,9,10]

print(nums)

print("____________________________________________")

fruits = ["Morango", "Quiabo", "Pimentão", "Xuxu", "Beringela", "Laranja", "Maracujá", "Pimenta"]

print("As duas primeiras frutas:", fruits[:2])
print("As duas últimas frutas:", fruits[-2:])

print("A lista possui", len(fruits), "frutas")

print("A última fruta é:", fruits[-1])

fruits.reverse()
print("Lista inversa:", fruits)

print("Posições pares:", fruits[0 :: 2])
print("Posições ímpares: ", fruits[1 :: 2])
