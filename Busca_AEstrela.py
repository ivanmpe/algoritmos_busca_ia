from VetorOrdenadoAdjacente import VetorOrdenadoAdjacente


class Busca_AEstrela:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.achou = False
        
    def buscar(self, atual):
        print("\nAtual: {}" .format(atual.nome))
        atual.visitado = True
        
        if atual == self.objetivo:
            print("Objetivo {} foi alcançado. " .format(self.objetivo.nome))
            self.achou = True
        else:
            self.fronteira = VetorOrdenadoAdjacente(len(atual.adjacentes))
            for a in atual.adjacentes:
                if a.cidade.visitado == False:
                    a.cidade.visitado = True
                    self.fronteira.inserir(a)
            self.fronteira.mostrar()
            if self.fronteira.getPrimeiro() != None:
                Busca_AEstrela.buscar(self, self.fronteira.getPrimeiro())



from Mapa import Mapa
mapa = Mapa()
aestrela = Busca_AEstrela(mapa.curitiba)
aestrela.buscar(mapa.portoUniao)        
 