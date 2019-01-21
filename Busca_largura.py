from Fila import Fila 


class Busca_largura :

    def __init__(self, inicio, objetivo):
        self.inicio = inicio
        self.inicio.visitado = True
        self.objetivo = objetivo
        self.fronteira = Fila(10000)
        self.fronteira.enfileirar(inicio)
        self.achou = False
        
    def buscar(self):
            
        
        print("Objetivo: {} " .format(self.objetivo.nome))
        primeiro = self.fronteira.getPrimeiro()
        print("primeiro: {}" .format(primeiro.nome))
        
        if primeiro == self.objetivo:
            print("Objetivo {}" .format(self.objetivo.nome), "foi alcançado apartir de {}" .format(self.inicio.nome))
            self.achou = True
        else: 
            temp = self.fronteira.desinfileirar()
            print("Desinfileirou: {}" .format(temp.nome))
            for a in primeiro.adjacentes:
                print("Verificando se já visitado: {}" .format(a.cidade.nome))
                if a.cidade.visitado == False:
                   self.fronteira.enfileirar(a.cidade)
                   a.cidade.visitado = True
            if self.fronteira.numeroElementos > 0 :
               Busca_largura.buscar(self)
            else:
                print("Objetivo: ", format(self.objetivo.nome), "foi achado apartir de ", format(primeiro.nome))


from Mapa import Mapa
mapa = Mapa()
largura = Busca_largura(mapa.portoUniao, mapa.curitiba)
largura.buscar()
