from Cidade import Cidade
from Adjacente import Adjacente

class Mapa:
    portoUniao = Cidade("Porto Uniao", 203)
    pauloFrontin = Cidade("Paulo Frontin", 172)
    canoinhas = Cidade("Canoinhas", 141)
    irati = Cidade("Irati", 139)
    palmeira = Cidade("Palmeira", 59)
    campoLargo = Cidade("Campo Largo", 27)
    curitiba = Cidade("Curitiba", 0)
    balsaNova = Cidade("Balsa Nova", 41)
    araucaria = Cidade("Araucaria", 23)
    saoJose = Cidade("São josé dos pinhais", 13)
    contenda = Cidade("Contenda", 39)
    mafra = Cidade("Mafra", 94)
    tijucas = Cidade("Tijucas do sul", 56)
    lapa = Cidade("Lapa", 74)
    saoMateus = Cidade("Sao Mateus do Sul", 123)
    tresBarras = Cidade("Tres barras", 131)

    portoUniao.addCidadeAdjacente(Adjacente(canoinhas))
    portoUniao.addCidadeAdjacente(Adjacente(saoMateus))
    portoUniao.addCidadeAdjacente(Adjacente(pauloFrontin))

    pauloFrontin.addCidadeAdjacente(Adjacente(irati))
    pauloFrontin.addCidadeAdjacente(Adjacente(portoUniao))
    
    canoinhas.addCidadeAdjacente(Adjacente(tresBarras))
    canoinhas.addCidadeAdjacente(Adjacente(portoUniao))
    canoinhas.addCidadeAdjacente(Adjacente(mafra))
    
    irati.addCidadeAdjacente(Adjacente(palmeira))
    irati.addCidadeAdjacente(Adjacente(saoMateus))
    irati.addCidadeAdjacente(Adjacente(pauloFrontin))

    
    palmeira.addCidadeAdjacente(Adjacente(irati))
    palmeira.addCidadeAdjacente(Adjacente(saoMateus))
    palmeira.addCidadeAdjacente(Adjacente(campoLargo))
    
    campoLargo.addCidadeAdjacente(Adjacente(palmeira))
    campoLargo.addCidadeAdjacente(Adjacente(balsaNova))
    campoLargo.addCidadeAdjacente(Adjacente(curitiba))
    
    curitiba.addCidadeAdjacente(Adjacente(campoLargo))
    curitiba.addCidadeAdjacente(Adjacente(balsaNova))
    curitiba.addCidadeAdjacente(Adjacente(araucaria))
    curitiba.addCidadeAdjacente(Adjacente(saoJose))
    
    balsaNova.addCidadeAdjacente(Adjacente(campoLargo))
    balsaNova.addCidadeAdjacente(Adjacente(curitiba))
    balsaNova.addCidadeAdjacente(Adjacente(contenda))
    
    araucaria.addCidadeAdjacente(Adjacente(curitiba))
    araucaria.addCidadeAdjacente(Adjacente(contenda))
    
    saoJose.addCidadeAdjacente(Adjacente(tijucas))
    saoJose.addCidadeAdjacente(Adjacente(curitiba))
    
    contenda.addCidadeAdjacente(Adjacente(balsaNova))
    contenda.addCidadeAdjacente(Adjacente(araucaria))
    contenda.addCidadeAdjacente(Adjacente(lapa))
    
    mafra.addCidadeAdjacente(Adjacente(lapa))
    mafra.addCidadeAdjacente(Adjacente(tijucas))
    mafra.addCidadeAdjacente(Adjacente(canoinhas))
    
    tijucas.addCidadeAdjacente(Adjacente(saoJose))
    tijucas.addCidadeAdjacente(Adjacente(mafra))
    
    
    lapa.addCidadeAdjacente(Adjacente(mafra))
    lapa.addCidadeAdjacente(Adjacente(saoMateus))
    lapa.addCidadeAdjacente(Adjacente(contenda))
    
    saoMateus.addCidadeAdjacente(Adjacente(palmeira))
    saoMateus.addCidadeAdjacente(Adjacente(lapa))
    saoMateus.addCidadeAdjacente(Adjacente(irati))
    saoMateus.addCidadeAdjacente(Adjacente(tresBarras))
    saoMateus.addCidadeAdjacente(Adjacente(portoUniao))
    
    tresBarras.addCidadeAdjacente(Adjacente(saoMateus))
    tresBarras.addCidadeAdjacente(Adjacente(canoinhas))

    
    