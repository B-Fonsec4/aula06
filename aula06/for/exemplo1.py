import os

os.system('cls')

# for e in range(1,9):
#     print(e)

# nome ='python'
# for e in nome:
#     print(e)

# i = int(input('Valor: '))
# f = int(input('Valor final: '))
# for e in range(i, f):
#     print(e)

# s = 0
# for e in range(5):
#     n = int(input('Valor: '))
#     s = s + n
# print(f'O total é {s}')

# lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for e in lista:
#     lista.reverse()
# print(lista)

# for e in range (10, 0, -1):
#     print(e)

n = int(input('Digite um numero: '))

for e in range(1, n+1):
    if n % e ==0:
        print (e)
