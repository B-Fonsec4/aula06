import os

os.system('cls')


# senha = '54321'
# leitura = ''
# while leitura != senha:
#     leitura = input('Digite a senha: ')
#     if leitura == senha:
#         print('Acesso liberado')
#     else:
        # print('Senha incorreta,tente novamente!')
# i = 0
# while True:
#     print(i)
#     i +=1
# contador = 10  
# while contador != 0:
#     print(contador)
#     contador -= 1

# s = 0
# c = 1
# while c < 4:
#     n = int(input('Informe um número: '))
#     s += n
#     c +=1
# print('O total é', s)

# n = ''
# resp = 'S'
# while resp != 'N':
#     n = input('Digite um texto: ')
#     resp = input('Quer continuar S/N: ')[0].upper()
# print(n)

n = s = 0
while True:
    n = int(input('Número: '))
    if n == 999:
        break
    s = s + n
print(s)