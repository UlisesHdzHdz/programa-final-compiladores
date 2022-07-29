
#from ast import If
from typing import List
#from pprint import pp
#from typing import final
from multiprocessing.reduction import duplicate
import re
import string
from unittest import result
from tokens import tokens
#from Interfaz import datos
resultfuncionesIndefinidas = []  # listo
funcion = []  # listo
entrada = []  # listo
entradafinal = []  # listo
resultFuncionesFinal = []  # listo
resultigual = []  # listo
resultsimbolo = []  # listo
resultcompuerta = []  # listo
resultllave1 = []  # listo
resultllave2 = []  # listo
entradasimbolo = [] # listo
resultError = []  # listo


a=5
class analizadorlexico:
    def analizador(self, palabras):
        # print('palabras .------',palabras)
        negacionnes=",".join(palabras)
      
        resultCaracteresEspeciales = []  # simbolo
        resultsimbolo = []
        resultDelimitadores = []
        print("--- Lexico ---")
        # -------SIMBOLO  ¬  -------------------------------------------------------------------
        for l in tokens.simbolo:
            for k in palabras:
                if (l == k):
                    resultsimbolo.append(k)
                    palabras.remove(l)

        # -------COMPUERTA * + -----------------------------------------------------------------
        for t in tokens.compuerta:
            for f in palabras:
                if (t == f):
                    resultcompuerta.append(t)
                    palabras.remove(t)
        # --------IGUAL  LLAVE 1  LLAVE2 ----------------------------------------------------------------

        for t in tokens.igual:
            for f in palabras:
                if (t == f):
                    resultigual.append(t)
                    palabras.remove(t)
        for t in tokens.llave1:
            for f in palabras:
                if (t == f):
                    resultllave1.append(t)
                    palabras.remove(t)
        for t in tokens.llave2:
            for f in palabras:
                if (t == f):
                    resultllave2.append(t)
                    palabras.remove(t)

        # --------FUNCIONES ENTRADA ERROR----------------------------------------------------------------
        for g in range(len(palabras)):
            dato = re.search("[a-zA-Z][a-zA-Z0-9_]*", palabras[g])
            if dato:
                # print("CUMPLIOO")
                resultfuncionesIndefinidas.append(palabras[g])
                # palabras.remove(palabras[g])
            else:
                dato1 = re.search("^[0-9]+$|,|.|-|{|}", palabras[g])
                if dato1:
                    #print("es un digito")
                    resultError.append(palabras[g])
                else:
                    #print("Error: ", palabras[g])
                   #resultError.append(palabras[g])
                   print("")
        # --------separacion de entrada y funcion ----------------------------------------------------------------
      
        # print("Token funcion entrada todooo   = ", resultfuncionesIndefinidas)
      

        for i in resultfuncionesIndefinidas:
            if (len(i) > 2):
                 print("")
                #print("es un funcion")
                 funcion.append(i)
            else :
               # print("es un  entrada con negacion")
                entrada.append(i)
                # print('esto trea entrada ',entrada)
    
        # --------separacion de la entrada y la negacion ----------------------------------------------------------------
           
        entradasimbolo2=",".join(entrada)
        # print("ESTA ES LA NUEVA ",entradasimbolo2)

        entradass = re.findall(r'[a-zA-Z]{1,100}',entradasimbolo2) # para extraer las entradas
        negacion = re.findall(r'[¬]',negacionnes) # para extraer simbolo negado

        # --------resultado Final----------------------------------------------------------------
        print("--- Lista de tokes ---")
        print("Entrada = ", entradass ," = ",len(entradass))
        print("Funcion = ", funcion ," = ",len(funcion))
        print("Token  igual = ", resultigual," = ",len(resultigual))
        print("Token simbolo = ", negacion," = ",len(negacion))
        print("Token compuerta = ", resultcompuerta," = ",len(resultcompuerta))
        print("Token llave [ = ", resultllave1," = ",len(resultllave1))
        print("Token llave ] =", resultllave2," = ",len(resultllave2))
        print("Token error = ", resultError," = ",len(resultError))

       
        
        
        

   
