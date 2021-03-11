
def pertence(tupla, item1, item2):
    if(item1 in tupla and item2 in tupla):
        return True
    else:
        return False


# tupla = (1, 2, 3, 4, 5, 6, 7)
# print(pertence(tupla, 1, 8))
# print(pertence(tupla, 10, 7))
# print(pertence(tupla, 2, 3))
# print(pertence(tupla, 7, 6))
# print(pertence(tupla, 11, 18))

def substituir(lista, velho, novo):
    lista2 = []
    for i in lista:
        if(i == velho):
            lista2.append(novo)
        else:
            lista2.append(i)
    return lista2


# lista = [2, 2, 3, 4, 4, 6, 7]
# print(substituir(lista, 2, 99))
# print(substituir(lista, 4, 77))
# lista_modificada = substituir(lista, 2, 4)
# print(substituir(lista_modificada, 4, 1))

def posicoes_lista(lista, item):
    lista_nova = []
    for indice in range(0, len(lista)):
        if lista[indice] == item:
            lista_nova.append(indice)
    return tuple(lista_nova)

# lista = [2, 2, 3, 4, 4, 6, 7]
# print(posicoes_lista(lista, 2))
# print(posicoes_lista(lista, 4))


def reprovados(alunos):
    reprovados = []
    for nome in alunos:
        total_notas = sum(alunos[nome])
        quantidade_notas = len(alunos[nome])
        media = total_notas/quantidade_notas

        if media < 6:
            reprovados.append(nome)

    return reprovados

# alunos = {
#     'Augusto': [4.5, 7.0, 6.0],
#     'Denise': [9.0, 8.5, 9.5],
#     'Ana Paula': [3.5, 7.0, 6.5],
#     'Marcelo': [9.0, 10.0, 7.0]
# }
# print(reprovados(alunos))

def incluir_nota(alunos, nome, nota):
    if(nome in alunos):
        alunos[nome].append(nota)
    return alunos

# alunos = {
#     'Augusto': [4.5, 7.0, 6.0],
#     'Denise': [9.0, 8.5, 9.5],
#     'Ana Paula': [3.5, 7.0, 6.5],
#     'Marcelo': [9.0, 10.0, 7.0]
# }

# print(incluir_nota(alunos, 'Augusto', 7.0))

def menores_notas(alunos):
    menores_notas = {}
    for nome in alunos:
        menores_notas[nome] = min(alunos[nome])
    return menores_notas


alunos = {
    'Augusto': [4.5, 7.0, 6.0],
    'Denise': [9.0, 8.5, 9.5],
    'Ana Paula': [3.5, 7.0, 6.5],
    'Marcelo': [9.0, 10.0, 7.0]
}
# print(menores_notas(alunos))