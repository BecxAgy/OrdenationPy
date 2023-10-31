import random

def busca_sequencial_sentinela(x, vetor):
    i = 0
    vetor.append(x)

    while(vetor[i] != x):
        i+=1
    #você esta no index da ultima posição? 
    if(i == len(vetor) - 1):
        return -1

    return i


vetor = list(range(0,10))

print(vetor)

x = 10 
busca_sequencial_sentinela(x,vetor)

print(vetor)


