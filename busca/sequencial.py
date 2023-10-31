import random

def busca_sequencial(x, vetor):
    i = 0
    while(i < len(vetor)):
        if(vetor[i] == x):
            return i
        i+=1

    return -1


vetor = list(range(0,10))

print(vetor)

x = 10 
busca_sequencial(x,vetor)

print(vetor)