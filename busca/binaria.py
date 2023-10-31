def busca_binaria(x, vetor):
   inicio = 0
   fim = len(vetor) - 1

   while(inicio <= fim ):
        meio = (inicio+fim)/2

        if(vetor[meio] == x):
            return meio
        
        if(vetor[meio] < x): #desloca para direita
            inicio = meio + 1
        else:
            fim = meio
      



vetor = list(range(0,10))

print(vetor)

x = 10 
busca_binaria(x,vetor)

print(vetor)