""" Algoritmos em Bioinformática
Nome: Stefanie Soares """

import string

arquivo= open('Corona_genomicl.fasta', 'r+')
arquivo.readline()  #Lê a primeira linha e descarta
filedata = (arquivo.read()[1:])
filedata = filedata.replace('A', 't')
filedata = filedata.replace('T', 'a')
filedata = filedata.replace('C', 'g')
filedata = filedata.replace('G', 'c')
novo = open("ex07_a.txt", "w")
novo.write (filedata.upper())
arquivo.close()
novo.close()





