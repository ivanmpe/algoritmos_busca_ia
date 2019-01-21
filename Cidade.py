class Cidade:
    def __init__(self, nome, distanciaObjetivo):
        self.nome = nome
        self.visitado = False
        self.adjacentes = []
        self.distanciaObjetivo = distanciaObjetivo
        
    def addCidadeAdjacente(self, cidade):
        self.adjacentes.append(cidade)


"""
c = Cidade("Maranguape", 202)
c.nome
c.visitado
c.adjacentes
c.distanciaObjetivo 
"""
