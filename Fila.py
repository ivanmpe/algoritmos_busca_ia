"""
    Fila Circular
"""

class Fila:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.cidades = [None] * self.tamanho
        self.inicio = 0
        self.fim = -1
        self.numeroElementos = 0
        
        
    def enfileirar(self, cidade):
            if self.fim == self.tamanho -1:
                self.fim = -1
            self.fim += 1 
            self.cidades[self.fim] = cidade
            self.numeroElementos += 1
      
    
    def desinfileirar(self):
     
        temp = self.cidades[self.inicio]
        self.inicio += 1
        if self.inicio == self.tamanho:
            self.inicio = 0
        self.numeroElementos-=1
        return temp
     
    
    def getPrimeiro(self):
        return self.cidades[self.inicio]
    
    def filaVazia(self):
        return self.numeroElementos == 0
    
    def filaCheia(self):
        return self.numeroElementos == self.tamanho



from Mapa import Mapa
mapa = Mapa()
fila = Fila(5)
fila.enfileirar(mapa.irati)
fila.enfileirar(mapa.canoinhas)
fila.getPrimeiro().nome
   
    
    
    
    
    