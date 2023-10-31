import random


def selection_sort(v):
    i = 0
    tam = len(v)

    while i < tam - 1:
        menor = i
        #j é sempre o próximo 
        j = i + 1
        #procura quem é o menor
        while j < tam :
            if(v[j] < v[menor]):
                menor = j
            j+=1

        if v[menor] != v[i]:
            temp = v[i]
            v[i] = v[menor]
            v[menor] = temp

        i+=1



vetor = list(range(0,10))

random.shuffle(vetor)
print(vetor)
selection_sort(vetor)

print(vetor)
