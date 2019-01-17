class Cidade:
    def __init__(self, nome):
        self.nome = nome
        self.visitado = False
        self.adjacentes = []
        
    def addCidadeAdjacente(self, cidade):
        self.adjacentes.append(cidade)


"""c = Cidade("Maranguape")
c.nome
c.visitado
c.adjacentes """
