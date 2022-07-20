'''Stefanie Soares
Algoritmos em Bioinformatica
Atividade 05 - Parte 2 '''


import numpy as np
from itertools import product
import itertools


#Variáveis globais
match_score = 1
mismatch = -1
gap = -2
seq1 = ('ACACACTA')
seq2 = ('AGCACACA')


#----------INICIAlIZAÇÃO E SCORING----------


def matriz(i, j):
    M = np.zeros((i, j)) #Condição de início


    for i, j in itertools.product(range(1, M.shape[0]), range(1, M.shape[1])): #Percorre linhas e colunas da nossa matriz
        if seq1[i-1] == seq2 [j-1]: #Acerto, ou seja, match
            match = M[i-1, j-1] + match_score
        else:
             match=  M[i-1, j-1] + mismatch #Erro, não iguais
        dele = M[i-1, j] + gap
        inse = M[i,j-1] + gap
        M[i,j]= max (0, match, dele, inse)
    return M, match, dele, inse


#----------ALINHAMENTO----------


def traceback(M, m, d, i):
    aux1, aux2= ' ',' '


    for i in range (len(seq1)+1):
        for j in range (len(seq2)+1):
            if M[i][j] != 0:
                if (M[i][j] == m):
                            aux1 = aux1 + seq1[i - 1]
                            aux2 = aux2 + seq2[j - 1]
                            i = i - 1
                            j = j - 1
                elif M[i][j] ==d:
                            aux1 = aux1 + seq1[i - 1]
                            aux2 = aux2 + '-'
                            i = i - 1
                elif M[i][j] == i:
                            aux1 = aux1 + '-'
                            aux2 = aux2 + seq2[j - 1]
                            j = j - 1
    return aux1, aux2


#main
i = len(seq1)+1
j=len(seq2)+1
M, m, d, i = (matriz(i, j))
print(traceback(M, m, d, i))