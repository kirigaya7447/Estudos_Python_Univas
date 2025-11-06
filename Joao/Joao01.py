lista = [1,2,3,4,5,6,7,8,9,10]
print("O tamanho da lista é de", len(lista),"itens")

lista.sort()
print("Os números ordenados são: ", lista)

lista.reverse()
print("e os números ordenados inversamente são: ", lista)

print("Os três últimos números são:", lista[-3:])

print("O maior número é:", lista[0])

print("O menor número é:", lista[-1])