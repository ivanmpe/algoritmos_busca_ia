# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 01:54:09 2019

@author: Ivan Alves
"""

class VetorOrdenado:
    def __init__(self, tamanho):
        self.numeroElementos = 0
        self.cidades = [None] * tamanho
    
    def inserir(self, cidade):
       if self.numeroElementos == 0:
           self.cidades[0] = cidade
           self.numeroElementos = 1 
           return 
       
       posicao = 0
       i = 0
       while i<self.numeroElementos:
           if cidade.distanciaObjetivo> self.cidades[posicao].distanciaObjetivo:
               posicao +=1
           i +=1
           
       for k in range(self.numeroElementos, posicao, -1):
          self.cidades[k] = self.cidades[k-1]
           
       self.cidades[posicao] = cidade
       self.numeroElementos = self.numeroElementos+1
    
    def getPrimeiro(self):
        return self.cidades[0]
    
    def mostrar(self):
        for i  in range(0, self.numeroElementos):
            print("{} - {}" .format(self.cidades[i].nome, self.cidades[i].distanciaObjetivo))