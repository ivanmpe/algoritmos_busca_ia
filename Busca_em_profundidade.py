from Pilha import Pilha

class Busca_Em_Profundidade:
    def __init__(self, inicio, objetivo):
        self.inicio = inicio
        self.inicio.visitado = True
        self.objetivo = objetivo
        #fronteira armazena pilha de cidades que serão visitadas
        self.fronteira = Pilha(100)
        self.fronteira.empilhar(inicio)
        
        
    def buscar(self):
        topo = self.fronteira.getTopo()
        print("Topo: {}".format(topo.nome))

        for adjacente in topo.adjacentes:
            print("Verificando se ja visitado: {}".format(adjacente.cidade.nome))
            if adjacente.cidade.visitado == False:
                adjacente.cidade.visitado = True
                self.fronteira.empilhar(adjacente.cidade)
                Busca_Em_Profundidade.buscar(self)
        print("Desempilhou: {}" .format(self.fronteira.desempilhar().nome))
       
        
from Mapa import Mapa
mapa = Mapa()
profundidade = Busca_Em_Profundidade(mapa.portoUniao, mapa.curitiba)
profundidade.buscar()
