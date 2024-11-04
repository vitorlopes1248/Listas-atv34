a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
intervalo=a[1:10]
print(f"O intervalo da lista: {intervalo}")

#intervalo de 8 a 13
intervalo=a[9:14]

#numeros pares da lista
print("Os numeros pares são: ")
for par in range(0,16,2):
    print(par)

#numeros impares da lista
print("Os numeros impares são: ")
for impar in range(0,16,2):
    print(impar-1)

#todos os multiplos de 2,3 e 4
dois=2
tres=3
quatro=4
for i in range(dois,tres,quatro):
    if i % dois and tres or quatro == 0:
        print(f"os multiplos sao:{i} ")
    else:
        print('inexistente!')

#lista reversa
a.reverse()
print(a)

#Razão entre a soma do intervalo de 10 a 15 pelo intervalo de 3 a 9 em float
intervalo2=a[10:16]
intervalo3=a[3:10]
soma2=sum(intervalo2)
soma3=sum(intervalo3)
razão=soma3/soma2
print(razão)