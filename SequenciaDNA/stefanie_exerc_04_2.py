""" Algoritmos em Bioinformática
Nome: Stefanie Soares """

seq = input ('Digite uma sequencia de DNA: ').upper().strip() #Letra maiúscula (upper) e sem espaço (strip) para normalização

#------------------// Sequência válida ou inválida //--------------------
na, nt, ng, nc = int, int, int, int

na = seq.count('A') #Retorna quantas letras A existem na sequência
nt = seq.count('T')
ng = seq.count('G')
nc = seq.count('C')

if (na+nt+ng+nc) != (len(seq)): #Verifica se o usuário não digitou uma letra diferente das disponíveis 
    print('Sequencia de DNA invalida')
    exit()  #Abandona o programa e não passa pelo restante do código

#------------------// Saídas //--------------------

print(f'O numero total de nucleotideos da sequencia digitada é {(len(seq))}') #Retorna o tamanho da string
print(f'A sequencia digitada possui:\n{na} Adenina (A)\n{ng} Guanina (G)\n{nc} Citosina (C)\n{nt} Timina (T)')
print(f'A frequencia de nucleotidos na sequencia é')
print(f'{((na*100)/(na+nt+ng+nc)):.2f}% Adenina (A)\n{((ng*100)/(na+nt+ng+nc)):.2f}% Guanina(G)\n{((nc*100)/(na+nt+ng+nc)):.2f}% Citosina (C)\n{((nt*100)/(na+nt+ng+nc)):.2f}% Timina (T)')
