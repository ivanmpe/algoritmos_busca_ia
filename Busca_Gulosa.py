"""
Algoritmo responsavel por fazer Busca Gulosa ate o Objetivo Curitiba
"""
from VetorOrdenado import VetorOrdenado


class Busca_gulosa:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.achou = False
        
    def buscar(self, atual):
        print("\nAtual: {}" .format(atual.nome))
        atual.visitado = True
        
        if atual == self.objetivo:
            self.achou = True
        else: 
            self.fronteira = VetorOrdenado(len(atual.adjacentes))
            for i in atual.adjacentes:
                if i.cidade.visitado == False:
                    i.cidade.visitado = True
                    self.fronteira.inserir(i.cidade)
            self.fronteira.mostrar()
            if self.fronteira.getPrimeiro() != None:
                Busca_gulosa.buscar(self, self.fronteira.getPrimeiro())


from Mapa import Mapa
mapa = Mapa()
gulosa = Busca_gulosa(mapa.curitiba)
gulosa.buscar(mapa.portoUniao)
            
            