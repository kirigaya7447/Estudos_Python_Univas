nums = (1,8,6,7,5)
print(nums)
print(nums[:3])
print(nums[-2:])

nums2 = (47,9,34,2,3,6764,98,0,5,3)
print(nums2[:4])

print("Pares: ")
for cont in nums2:
    if(cont % 2 == 0):
        print(cont, end=",")
    else:
        print("", end="")

print("\nÍmpares: ")
for cont in nums2:
    if(cont % 2 != 0):
        print(cont, end=",")
    else:
        print("", end="")

fruits = ["Maçã verde", "Acerola", "Morte"]
print("\n", fruits)
fruits.append("Raiva")
print(fruits)

teenTitans = ["Camisola", "Meia", "Torso", "Sapato", "Calça"]
print(teenTitans)
teenTitans.remove("Camisola")
print(teenTitans)
print(len(teenTitans))

alea = [23,4,5,6,4,3322,4,5,67,8,4465,7878,324,3,54,21313,816,900,989]
alea.sort()
print(alea)

