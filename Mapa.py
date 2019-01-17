from Cidade import Cidade
from Adjacente import Adjacente

class Mapa:
    portoUniao = Cidade("porto uniao")
    pauloFrontin = Cidade("Paulo Frontin")
    canoinhas = Cidade("Canoinhas")
    irati = Cidade("Irati")
    palmeira = Cidade("Palmeira")
    campoLargo = Cidade("Campo Largo")
    curitiba = Cidade("Curitiba")
    balsaNova = Cidade("Balsa Nova")
    araucaria = Cidade("Araucaria")
    saoJose = Cidade("São josé dos pinhais")
    contenda = Cidade("Contenda")
    mafra = Cidade("Mafra")
    tijucas = Cidade("tijucas do sul")
    lapa = Cidade("Lapa")
    saoMateus = Cidade("Sao Mateus do Sul")
    tresBarras = Cidade("Tres barras")

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

    
    