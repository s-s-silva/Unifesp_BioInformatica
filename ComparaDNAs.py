"""  Comparando sequencias de DNA. Faça um código em
python que faça a leitura dos seguintes arquivos:
Seq_a.fasta e Seq_b.fasta. Após a leitura das sequencias
contidas nos arquivos,
O código deve imprimir na tela:
a. O número de nucleotídeos diferentes entre as
sequencias. Fazer somente nas 200 primeiras
posições da sequência.
b. As posições, na string, em que aparece essas
mudanças """


cont = int
cont = 0

r1 = open('seq_a.fasta', 'r')
r2 = open('seq_b.fasta', 'r')
r1.readline()
r2.readline()
x=r1.read()[0:200]
y=r2.read()[0:200]


for j in range (0,200):
    if x[j] != y [j]:
        cont = cont + 1
        print(f'a posição {j} foi trocado {x[j]}->{y[j]}')
print(f'O numero de nucleotidos diferentes é {cont}')
r1.close()
r2.close()