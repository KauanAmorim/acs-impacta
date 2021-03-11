def pilha_par_impar(pilha):
    pilha_par = []
    pilha_impar = []

    for i in pilha:
        if i % 2 == 0:
            pilha_par.append(i)
        else:
            pilha_impar.append(i)

    return pilha_par, pilha_impar

