from DataStructures import Linked_list

lista = Linked_list()
lista2 = Linked_list()

for i in range(10):
    lista.insert(i)
    
lista2.insert(10)
lista2.insert(20)

print(lista)
for i in lista: 
    print(i)

print(bool(lista))
print(tuple(lista))
print(lista == lista2)
print(lista.head)