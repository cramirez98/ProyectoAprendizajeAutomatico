import pandas as pd
try:
  paquetes = pd.read_excel("ProyectoAprendizajeAutomatico/util/paquetes.xlsx")
  paquetes.to_csv("paquetes.csv", index = False)
except Exception as e:
  print(e)
else:
  print("La lista de paquetes se cargo correctamente")
