import pandas as pd

df_liga = pd.read_csv("vinicius_data_Liga.csv")
df_uefa = pd.read_csv("vinicius_data_uefa.csv")

uefa_frequency_goals = df_uefa["GOALS"].value_counts(normalize=True)


uefa_frequency_assist = df_uefa["ASSIST"].value_counts(normalize=True)


uefa_goals = df_uefa["GOALS"].sum()
uefa_goals_freuency = round(uefa_goals/19,3)
print(f"La probabilité pour que vinicius marque 1 ou 2 buts est de {uefa_goals_freuency*100}%")
print("")
print(f"La probabilité pour que Vinicius ne marque pas ou ne fasse aucun assist est de 63.1%")
print("")
print(f"La probabilité pour que vinicius marque 1 but ou qu'il fasse 1 assist est de 31.5%")
print("")
print(f"La probabilité pour que vinicius marque 2 buts ou qu'il fasse 2 assists est de 5.2%%")


liga_frequency_domicile = df_liga["BUTS_DOMICILE"].value_counts(normalize=True)
liga_frequency_exterieur = df_liga["BUTS_EXTERIEUR"].value_counts(normalize=True)
liga_frequency_assist = df_liga["ASSIST"].value_counts(normalize=True)
print(liga_frequency_assist)
print(liga_frequency_exterieur)
print(liga_frequency_domicile)

domicile = df_liga["BUTS_DOMICILE"].sum()
exterieur = df_liga["BUTS_EXTERIEUR"].sum()
total = domicile + exterieur
print("")
print(f"Le nombre de buts total (dom+ext) est de {total}")
print("")
print("-------EXTERIEUR--LIGA-------")
print("")
print(f"La probabilité pour que Vinicius ne marque pas à l'exterieur est de 81.3%")
print("")
print(f"La probabilité pour que vinicius marque 1 but à l'exterieur est de 13.5%")
print("")
print(f"La probabilité pour que vinicius marque 2 buts à l'exterieur est de 1.6%")
print("")
print(f"La probabilité pour que vinicius marque 3 buts à l'exterieur est de 1.6%")
print("")
print("---------DOMICILE---LIGA------")
print("")
print(f"La probabilité pour que Vinicius ne marque pas à domicile est de 81.3%")
print("")
print(f"La probabilité pour que vinicius marque 1 but à domicile est de 15.2%")
print("")
print(f"La probabilité pour que vinicius marque 2 buts à domicile est de 1.6%")
print("")

print("--------ASSIST-------LIGA------")
print(f"La probabilité pour que Vinicius ne fasse aucun assist  est de 83.0%")
print("")
print(f"La probabilité pour que vinicius fasse 1 assist  est de 22.0%")
print("")
print(f"La probabilité pour que vinicius fasse 2 assists  est de 3.3%")
print("")
print("")
print(f"Probabilité de but à domicile(liga): 53.8%")
print(f"Probabilité de but à l'exterieur(liga): 46.1%")
print("")
print("")
print(f"Nbre de buts à domicile (liga): {domicile}")
print(f"Nbre de buts à l'exterieur (liga): {exterieur}")
print(f"Nbre de buts total (liga): {total}")

total2 = total + df_uefa["GOALS"].sum()
frequences_all_match_goals = round((total2 / 78)*100,3)
print(f"la probabilité pour que Vinicius marque est de {frequences_all_match_goals}%")



