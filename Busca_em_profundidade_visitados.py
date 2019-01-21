"""
    Algoritmo responsavel por criar realizar busca em profundidade com lista de visitados

"""

from Pilha import Pilha

class Busca_Em_Profundidade_Visitados:
    def __init__(self, inicio, objetivo):
        self.inicio = inicio
        self.inicio.visitado = True
        self.objetivo = objetivo
        #fronteira armazena pilha de cidades que serão visitadas
        self.fronteira = Pilha(1000)
        self.fronteira.empilhar(inicio)
        self.achou = False
        
    def buscar(self):
        topo = self.fronteira.getTopo()
        print("Topo: {}".format(topo.nome))
        
        if topo == self.objetivo:
            print("Objetivo {}" .format(self.objetivo.nome), "foi alcançado apartir de {}" .format(self.inicio.nome))
            self.achou = True
        else:
            for adjacente in topo.adjacentes:
                if self.achou == False:
                    print("Verificando se ja visitado: {}".format(adjacente.cidade.nome))
                    if adjacente.cidade.visitado == False:
                        adjacente.cidade.visitado = True
                        self.fronteira.empilhar(adjacente.cidade)
                        Busca_Em_Profundidade_Visitados.buscar(self)
        #print("Desempilhou: {}" .format(self.fronteira.desempilhar().nome))
    
   
                
from Mapa import Mapa
mapa = Mapa()
profundidade = Busca_Em_Profundidade_Visitados(mapa.portoUniao, mapa.curitiba)
profundidade.buscar()
