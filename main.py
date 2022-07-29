import re
frase = 'funcion = ( a . ¬b + d) + ( ¬a + ¬b ) + [ a . b . p ] . [ a . c ] funcionulisesul'
 
funciones = re.findall(r'[a-zA-Z]{1,100}',frase) # para extraer nombre de funciones



compuerta = re.findall(r'[+|.]',frase) # para extraer nombre de funciones
negacion = re.findall(r'[¬]',frase) # para extraer nombre de funciones
entradaNegada = re.findall(r'¬[a-zA-Z]|',frase) # negacion y entrada
igual = re.findall(r'[=]',frase)
llave = re.findall(r'[(|)]',frase) # para extraer nombre de func

string_list = frase.split()
print("es te es ===== ",string_list)
for i in string_list:
    print("cote ",i)

entrada = re.findall(r'[a-zA-Z]',string_list[2]) # para extraer nombre de funciones

entrada2 = re.search(r'\(([^)]*)', frase).group(1)

res = []
for i in re.findall("\[(.*?)\]", frase):
    res.extend(i.replace(".", "").split())
    
print("holalllll",res)

print("frace : ",frase)
print("-------------------------")
print("funciones ",len(funciones),"=",funciones)
print("negacion ",len(negacion),"=",negacion)
print("compuerta ",len(compuerta),"=",compuerta)
print("igual ",len(igual),"=",igual)
print("llave",len(llave),"=",llave)
print("entrada ",len(entrada),"=",entrada)
print("entrada2 ",len(entrada2),"=",entrada2)
print("entrada negada : ",len(entradaNegada),"=",entradaNegada)


string = string_list[2]
characters = "(.¬+)?"

for x in range(len(characters)):
    string = string.replace(characters[x],"")

print(string)

for i in res :
    print(len(i))

