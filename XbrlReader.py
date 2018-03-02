# -*- coding: utf-8 -*-
"""
Created on timelessness

@author: Emiliano Hernandez
"""
#import re
#import numpy
#import pandas as pd
#from pandas.io.json import json_normalize
import os
def getinfo(stock,trimestre,anio,xbrlcode):
    periodo=str(trimestre)+"-"+str(anio)
    xbrldirectory = currentdirectory = os.getcwd()+"/xbrl"
    filename = xbrldirectory+"/"+stock+"_"+periodo+".json"
    jsoonfule = open(filename,"r",encoding="utf8").read()
    #bloque = jsoonfule.split("\""+xbrlcode+"\" : [ \"",2)[1].split("\"",1)[0]
    lookone = "ifrs-full_"+xbrlcode
    looktwo = "ifrs_"+xbrlcode
    if lookone in jsoonfule:
        blockspre = jsoonfule.split("\""+lookone+"\" : [ \"", 2)[1].split("]",1)[0].split("\"")
    elif looktwo in jsoonfule:
        blockspre = jsoonfule.split("\"" + looktwo + "\" : [ \"", 2)[1].split("]", 1)[0].split("\"")
    blocks = [blockspre[0],blockspre[2]]
    print(blocks)
    for n in blocks:
        valor = jsoonfule.split(n)[3].split("\"Valor")[1]
        contexto = jsoonfule.split(n)[3].split("IdContexto")[1].split("IdUnidad")[0].split("\"")[2]
        contextofinal = jsoonfule.split(contexto,3)[2].split("Fecha",2)[1].split(": \"",2)[1].split("T",1)[0]
        print(contextofinal)
        valorfinal = valor.split("\"")[2]
        #tiempo = jsoonfule.splot()
        print(int(valorfinal))

#getinfo("BEVIDES",4,2014,"EquityAndLiabilities")