from datetime import timedelta
from datetime import datetime
import numpy as np
import pandas as pd

#Función de suma
def getSum(n):  
  if n == 11:
      return n
  if n == 22:
      return n
  if n == 33:
      return n
  if n == 44:
      return n                
  sum = 0
  for digit in str(n):
      sum += int(digit)        
  return sum  

#cabeceras del frame
headers_F = ["Fechas"]
headers_N = ["Numerología"]

#fechas de inicio
inicio = datetime(1,1,1)
fin    = datetime(2022,10,10)

#array de todas las fechas según las fechas inicio y fin
##
##
##
lista_fechas_array = [(inicio + timedelta(days=d)).strftime("%Y%m%d") for d in range((fin - inicio).days + 1)] 
##
##
##
#interacción con el array
xs = [int(x) for x in lista_fechas_array]
dfecha = pd.DataFrame(xs)
dfecha.columns = headers_F
dfecha.head()

#construcción del frame de fechas
lista_p = list(dfecha['Fechas'])
dfecha.head()

#interacción con la lista
lista_p2 = [getSum(x) for x in lista_p]
lista_p3 =[getSum(x) for x in lista_p2]
lista_t = [getSum(x) for x in lista_p3]

#construcción del frame Numerologia
df_Num = pd.DataFrame(lista_t)
df_Num.columns = headers_N
df_Num.head()

#concateno el frame de la fecha y el frame del Num
Numerologia=pd.concat([dfecha,df_Num], axis=1)
Numerologia.head()

#RESULTADO DEFINITIVO
print("Mao",Numerologia[Numerologia['Fechas'] == 19761027])
print("Solange", Numerologia[Numerologia['Fechas'] == 19680914])
print("Carmen Luisa", Numerologia[Numerologia['Fechas'] == 19830113])
print("Ender", Numerologia[Numerologia['Fechas'] == 19910911])
print("Adrian", Numerologia[Numerologia['Fechas'] == 19821017])
print("Madeleine", Numerologia[Numerologia['Fechas'] == 19881104])
