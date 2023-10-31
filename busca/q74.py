#Escreva um programa que armazene um vetor de até 30 inteiros. O programa deve fornecer as seguintes operações:
#a. Inserir um elemento no final do vetor
#b. Inserir um elemento em uma dada posição
#c. Remover um elemento de uma posição indicada
#d. Remover todos elementos iguais a um valor indicado
#e. Gerar um novo array sem duplicidades a partir deste array

def append_v(vetor , value, n):

    vetor[n-1] = value; 
    
def insert_in_pos(vetor, valor, pos):
    vetor[pos] = valor

def remove_in_pos(vetor, pos, n):
    # empurro para trás ->
    while(pos < n-3):
        vetor[pos] = vetor[pos+1]
        pos+=1
    
def remove_x(v, x, n):
    i = 0
    j = 0
 
    while(j < n):
        if (v[j] != x):
            v[i] = v[j]
            i+=1
        j+=1
    return i
    

vetor = list([1,1,4,5,6,7,8,9,1,1,1,5,6,7,10])

print(vetor)
#append_v(vetor, 99, 30)
#insert_in_pos(vetor, 27, 4 , 30)
#remove_in_pos(vetor,4,len(vetor))
remove_x(vetor, 5,len(vetor) )
print(vetor)



