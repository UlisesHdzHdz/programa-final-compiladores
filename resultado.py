
from tkinter import END
from tkinter import *
from tkinter import messagebox as MessageBox
from tabla import tablaLogica
from tabla import logica
from analizador import*
import re
import sys
sys.path.append("analizador")
import analizador as i
import numpy as np

def creaMatriz(n,m):
    matriz = []
    for i in range(n):
     a = [0]*m
     matriz.append(a)
    return matriz

class resultadoOut:

  def resultadoF(self,palabras):
    print("-------------------------------------------RESULTADO----------------------")  
    ne=" ".join(palabras)
    print("palabras ",ne)
    a = np.array(ne)
    entradasF = []
    for element in entrada:
     if element not in entradasF:
        entradasF.append(element)
    print("a ",entradasF)            #1
    
  
    entradaNegada = re.findall("¬\s[a-zA-Z][a-zA-Z0-9_]*",ne)

    print("b ",entradaNegada)       #2
   

    partes = re.findall("\(([^)]*)\)", ne)
    print("c ",partes)          #3

    filaX=len(entradaNegada)+len(partes)
    print("filas x ",filaX)
    columnaY = pow(2,len(entradasF))+1
    print("columna Y ",columnaY)

    

    matriz = []
    for i in range(columnaY):
      matriz.append([0] * filaX)

    # for i in range(filaX):
    #   for j in range(columnaY):
      #     matriz[i][j]="holA"
    cont=0
    for i in range(len(entradasF)):
      #  matriz[0][cont]=entradasF[i] 
       tablaLogica().va[0][cont]=entradasF[i]
       logica().v1[cont]=entradasF[i]
       cont +=1

  
    cont=0
    for i in range(len(entradaNegada)):
       matriz[0][cont]=entradaNegada[i]
         
       cont +=1
    # for i in range(len(partes)):
    #    matriz[0][cont]=partes[i]  
    #    cont +=1
   
    #-------------imprime resultados
    print("La matriz es la siguiente:")
    for filaX in tablaLogica().va:
        for valor in filaX:
            print("\t", valor, end=" ")
        print()
     #------------------------------manipulando operaciones entradas negadas
    
    # for j in range(len(filaX)):
    #   for i in range(1,columnaY):
    #    a=matriz[0][j]

    a=len(entradaNegada)
    entradasimbolo2=" ".join(entradaNegada)
    va1 = re.findall("[a-zA-Z][a-zA-Z0-9_]*",entradasimbolo2)
    # print(va1)
    al=len(va1)
    # for x in range(0,len(filaX)):
    #  print("en x",matriz[0][x])

     
    for buscar in range(al):
      # print("buscar",va1[buscar])
      if(va1[buscar] in logica().v1):
           xx=logica().v1.index(va1[buscar])
           for i in range(1,columnaY):
            a = tablaLogica().va[i][xx]
            if(a==1):
                matriz[i][xx]=0
            else:
             matriz[i][xx]=1
  #------------------------------manipulando operaciones *
      
    # matrizOp = []
    # conx=0
    # for i in range(len(partes)):
    #   entradasimbolo2="".join(partes[i])
    #   hola_limpio = entradasimbolo2.strip()
    #   separado_por_espacios = hola_limpio.split(" ")
    #   print("Separado por espacios es:", separado_por_espacios)
    #   tam=len(separado_por_espacios)
    #   for j in range(tam):
    #     # print("sdsd", separado_por_espacios[j])
        
    #     if(separado_por_espacios[j] in logica().v1):

    #         xx=logica().v1.index(separado_por_espacios[j])
    #         for i in range(1,columnaY):
    #           # a = tablaLogica().va[i][xx]
    #           # matrizOp.append(a)
    #           matrizOp.append(tablaLogica().va[i][xx])
              
              
              
            

    # for i in range(len(matrizOp)):
    #    print("---->",matrizOp[i])


        


    

    

       
        
       


       
    




     #------------------------------manipulando operaciones
    print("La matriz es la siguiente:")
    for filaX in matriz:
        for valor in filaX:
            print("\t", valor, end=" ")
        print()
    

    



   
     
    

    





  

    

    