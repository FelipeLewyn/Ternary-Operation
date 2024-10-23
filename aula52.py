# Desemcompactamento em chamadas 
# de métodos e funções 
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'python', 'é', 'legal'

# a, b, c, *_ = lista
# print(a,c)
for nome in lista:
    print(nome, end=' ') # o end determina como será organizado cada item 

# ou 

print(*lista)
print(*string)

salas = [
    # 0
    ['maria', 'helena',],   # 0
    #0
    ['elaine', ],   # 1
    # 0
    ['luiz', 'joão', 'eduarda', ],   # 2
]

print(*salas, sep='\n') # o sep determina como a proxima linha será tratada