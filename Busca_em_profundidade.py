"""
    Algoritmo responsavel por criar realizar busca em profundidade

"""

from Pilha import Pilha

class Busca_Em_Profundidade:
    def __init__(self, inicio, objetivo):
        self.inicio = inicio
        self.inicio.visitado = True
        self.objetivo = objetivo
        #fronteira armazena pilha de cidades que serão visitadas
        self.fronteira = Pilha(10000)
        self.fronteira.empilhar(inicio)
        self.achou = False
        
    def buscar(self):
        topo = self.fronteira.getTopo()
        
        if topo == self.objetivo :
            self.achou = True
            print("Objetivo {}" .format(self.objetivo.nome), "foi alcançado apartir de {}" .format(self.inicio.nome))
        else:
            print("Topo: {}".format(topo.nome))
            for adjacente in topo.adjacentes:
                if self.achou == False:
                    self.fronteira.empilhar(adjacente.cidade)
                    Busca_Em_Profundidade.buscar(self)
            #print("Desempilhou: {}" .format(self.fronteira.desempilhar().nome))
           
        
from Mapa import Mapa
mapa = Mapa()
profundidade = Busca_Em_Profundidade(mapa.portoUniao, mapa.canoinhas)
profundidade.buscar()
