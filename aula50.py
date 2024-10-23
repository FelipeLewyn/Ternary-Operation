"""
Lista de Lista e seus indices
"""
salas = [
    # 0
    ['maria', 'helena',],   # 0
    #0
    ['elaine', ],   # 1
    # 0
    ['luiz', 'joão', 'eduarda', ],   # 2
]

print(salas[0][1]) #primeiro [] = lista, segundo = [] indice 
print(salas[2][2])
print(salas[2][2][2])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)