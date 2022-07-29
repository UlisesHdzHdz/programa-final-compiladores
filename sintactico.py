
from tkinter import END
from tabla import tablaPredictiva
from tabla import noTerminales
from tabla import terminales
from tkinter import *
from tkinter import messagebox as MessageBox
import re

listaAuxiliar = []
aux = []
global auxX
global auxY
class analizador_sintactico:
    
  def analizarSintaxis(self, palabras):
  
    bandera = True
    apuntador = 0
    pila=["F"]
    while True:
        
          cima = pila.pop()
          numPalabras = len(palabras)
          
        
          resulExpresion = re.search("^[a-zA-Z][a-zA-Z]+$", palabras[apuntador])

          if resulExpresion:
              xx=1
          elif(palabras[apuntador] in terminales().t):
              xx=terminales().t.index(palabras[apuntador])

          if(cima in noTerminales().g): 
           yy=noTerminales().g.index(cima) 
           extraer = tablaPredictiva().t1[yy][xx]

           if(extraer == ""):
            if(pila):
                pila.pop()
            
         
           print("-> No terminales  (",cima,") --> ",extraer,"palabra",palabras[apuntador])
           print( "[y=",yy,"]",noTerminales().g[yy])
           print( "[x=",xx,"]",terminales().t[xx])
        
          
           separado_por_espacios = extraer.split(" ")
           print("Separado por espacios es:", separado_por_espacios)
           
           cantPro=len(separado_por_espacios)
           cantre=len(separado_por_espacios)
           for p in range(0,cantPro):
            cantre=cantre-1
            print(separado_por_espacios[cantre])
            pila.append(separado_por_espacios[cantre])
          else:
              print("terminales")
           
              if(cima == 'a..z'):
                              
                                print('es una expresion regular (a...z|A...Z)')
                                resulExpresion = re.search("^[a-zA-Z][a-zA-Z]+$", palabras[apuntador])
                                if resulExpresion:
                                    print('cumple la expresion')
                                    cima = palabras[apuntador]
                                else:
                                
                                    print('Error de sintaxis: ', palabras[apuntador])
                                    MessageBox.showerror("ERROR 1", "Error de sintaxis")
                                    bandera = False
                                    break
         
              

             
              if(cima == palabras[apuntador]):

                      print("-----------------------------------{")
                      print("este es la cima y el apuntador->",cima,"<-palabra apuntador ",palabras[apuntador])
                      print("palabras", palabras)
                      print("palabras", palabras[apuntador],"apuntador",apuntador)
                      print('Se extrae ', cima, ' de la pila'," palabras ",palabras[apuntador],"apuntador,",apuntador) #                     
                      apuntador =apuntador + 1
                      print('Contenido de Pila 1: ',pila)
                      print("-----------------------------------}")
                  
              else:
                      print('Error de sintaxis: ', palabras[apuntador])
                      MessageBox.showerror("ERROR 2", "Error de sintaxis")
                      bandera = False
                      break
              if(len(pila) == 0):  # ----
                      print('PILA VACIA')
                      print("APUNTADOR",apuntador,"numPalabras",numPalabras)
                      if(apuntador == numPalabras):
                       
                          print('ENTRADA VACIA')
                          MessageBox.showinfo("CADENA VALIDA", "ENTRADA VACIA Y PILA VACIA")
                          bandera = False
                          break
                      else:
                          print('ENTRADA CON DATOS')
                          MessageBox.showerror("CADENA NO VALIDA","ENTRADA CON DATOS")   
                          bandera = False
                          break  # ---
                        
                      if(apuntador == numPalabras):
                        print('ENTRADA VACIA')
                        MessageBox.showerror("ERROR 3", "Pila con datos, entrada vacia!")
                        print('Contenido de Pila 2: ', pila)
                        bandera = False
                        break # ---
                     
          if(bandera == False):
           break


          
        