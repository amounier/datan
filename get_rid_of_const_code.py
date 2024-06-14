import pandas as pd

# Lire le fichier CSV dans un DataFrame
df = pd.read_csv("output/RN_deputees_information.csv")

# Extraire la partie sans le code entre parenthèses
df["Constituency_no_code"] = df["Constituency"].apply(lambda x: x.split("(")[0].strip())

# Enregistrer le DataFrame modifié dans un nouveau fichier CSV
df.to_csv("output/RN_deputees_information.csv", index=False)