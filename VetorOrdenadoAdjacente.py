class VetorOrdenadoAdjacente:
    def __init__(self, tamanho):
        self.numeroElementos = 0
        self.adjacentes = [None] * tamanho
    
    def inserir(self, adjacente):
       if self.numeroElementos == 0:
           self.adjacentes[0] = adjacente
           self.numeroElementos = 1 
           return 
       
       posicao = 0
       i = 0
       while i<self.numeroElementos:
           if adjacente.distanciaAEstrela > self.adjacentes[posicao].distanciaAEstrela:
               posicao +=1
           i +=1
           
       for k in range(self.numeroElementos, posicao, -1):
          self.adjacentes[k] = self.adjacentes[k-1]
           
       self.adjacentes[posicao] = adjacente
       self.numeroElementos = self.numeroElementos+1
    
    def getPrimeiro(self):
        return self.adjacentes[0].cidade
    
    def mostrar(self):
        for i  in range(0, self.numeroElementos):
            print("{} - {}" .format(self.adjacentes[i].cidade.nome, self.adjacentes[i].distanciaAEstrela))