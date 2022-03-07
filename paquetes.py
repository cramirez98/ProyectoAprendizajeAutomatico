from google.colab import auth
from google.colab import output
auth.authenticate_user()

import gspread
from google.auth import default
creds, _ = default()
gc = gspread.authorize(creds)
worksheet = gc.open('paquetes').sheet1

# get_all_values gives a list of rows.
rows = worksheet.get_all_values()

import pandas as pd
paquetes = pd.DataFrame.from_records(rows)
try:
  paquetes.to_csv("paquetes.csv", index = False)
except:
  print("Hubo un error cargando la lista de paquetes")
else:
  print("La lista de paquetes se cargo correctamente")
  print(rows)
