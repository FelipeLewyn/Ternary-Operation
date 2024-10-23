"""
Split e join com list e str
split - divide uma string 
join - une uma string
"""
frase =  'Olha só que, coisa interessante'
lista_frases_cruas = frase.split(',')

lista_frases = []
for i,frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases[i].strip()) #o stri retira os espaços [l] corta da esquerda [r] corta da direita

# print(lista_frases_cruas)
# print(lista_frases)
frases_unidas = '-'.join(lista_frases)
print(lista_frases)