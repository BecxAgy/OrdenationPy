import random 


def bubble_sort(v):
    fim = len(v) 
    print(fim)

    while(fim -1 > 0):
        i = 0
        while(i < fim - 1 ):     
            if(v[i] > v[i+1]):             
                #troca da posição atual pela proxima, já a anterior é maior que a proxima
                temp = v[i]
                v[i] = v[i+1]
                v[i+1] = temp
            i+=1        
        fim -= 1
                

vetor = list(range(0,10))

random.shuffle(vetor)
print(vetor)
bubble_sort(vetor)

print(vetor)

