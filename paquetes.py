import pandas as pd
try:
  paquetes = pd.read_excel("paquetes.xlsx")
  paquetes.to_csv("paquetes.csv", index = False)
except:
  print("Hubo un error cargando la lista de paquetes")
else:
  print("La lista de paquetes se cargo correctamente")
  print(rows)
