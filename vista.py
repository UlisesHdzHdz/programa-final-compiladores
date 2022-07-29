from cProfile import label
from email.mime import image
from enum import auto
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#from typing_extensions import Self
from analizador import analizadorlexico
from sintactico import analizador_sintactico
from resultado import resultadoOut
#from analizador_L import analiza
import re
raiz = Tk()
a = analizadorlexico()
s = analizador_sintactico()
f = resultadoOut()

Label(text=" '  Analizador lexico ' ", fg="black",
      bg="blue", font=('Ravie', 16)).pack()
Label(text="Entrada de Datos ", fg="black",bg="blue", font=('Ravie', 16)).pack()



def datos():
    print(entrada.get())
    # se divide las palabras por cada espacio que encuentra
    palabras = re.split("\s", entrada.get())
    palabrasc2 = palabras[:]
    a.analizador(palabras)
    s.analizarSintaxis(palabrasc2)
    f.resultadoF(palabrasc2)


entrada = StringVar()

raiz.geometry('1050x500')
# color fondo
raiz.configure(bg='blue')
# titulo
raiz.title('Lenguajes y Automatas')
caja = Entry(raiz, textvariable=entrada)
caja.place(x=278, y=57, width="500", height="35")
ttk.Button(raiz, text='Busqueda', command=datos).place(
    x=800, y=57, width="100", height="35")


ttk.Button(raiz, text='Salir', command=quit).pack(side=BOTTOM)

raiz.mainloop()

# funcion = ( aA + aB * aC * aD ) :
# Funcion = ( AA * BB ) + ( ¬ AA * BB ) :
# Funcion = ( AA * BB * CC ) + ( ¬ AA * BB ) + ( CC * ¬ BB ) :
# Funcion = ( AA * BB * CC ) + ( ¬ AA * BB ) + ( CC * ¬ BB ) * ( DD + AA ) :
# Funcion = ( CC * BB ) + (  AA * SS ) + ( AA * ¬ BB ) * ( CC + AA ) :
# Funcion = ( AA * ¬ BB ) + ( ¬ AA * BB ) + ( ¬ CC * BB ) * ( ¬ DD + AA ) :
# Funcion = ( AA * BB ) + ( AA * BB ) + ( ¬ CC * BB ) * ( ¬ DD + ¬ AA ) :

