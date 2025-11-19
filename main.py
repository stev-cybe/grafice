import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Creează un program Python care generează un set de date simplu
# Generarea unui set de date simplu
data = {
    'X': np.arange(1, 11),
    'Y': np.random.randint(1, 100, 10)
}
df = pd.DataFrame(data)

# creează un grafic pe baza datelor și salvează rezultatele în fișiere.
plt.figure(figsize=(10, 6))
plt.plot(df['X'], df['Y'], marker='o', linestyle='-', color='b')
plt.title('Grafic simplu al datelor generate')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.savefig('simple_plot.png')
plt.show()

# Creează un DataFrame cu vânzări lunare pentru 6 luni.
# Coloane: "Luna" și "Vânzări".
sales_data = {
    'Luna': ['Ianuarie', 'Februarie', 'Martie', 'Aprilie', 'Mai', 'Iunie'],
    'Vânzări': [1500, 1800, 2200, 1700, 2500, 3000]
}
sales_df = pd.DataFrame(sales_data)
print(sales_df)
# Salvează DataFrame-ul într-un fișier CSV.
sales_df.to_csv('monthly_sales.csv', index=False)


# Creează un grafic de tip linie care afișează evoluția vânzărilor.
plt.figure(figsize=(10, 6))
plt.plot(sales_df['Luna'], sales_df['Vânzări'], marker='s', linestyle='-', color='g')
plt.title('Evoluția Vânzărilor Lunare')
plt.xlabel('Luna')
plt.ylabel('Vânzări')
plt.grid(True)
plt.savefig('monthly_sales_plot.png')
plt.show()


# Adaugă valori numerice deasupra fiecărui punct din grafic.
plt.figure(figsize=(10, 6))
plt.plot(sales_df['Luna'], sales_df['Vânzări'], marker='s', linestyle='-', color='g')
for i, value in enumerate(sales_df['Vânzări']):
    plt.text(sales_df['Luna'][i], value + 50, str(value), ha='center', va='bottom')
plt.title('Evoluția Vânzărilor Lunare cu Valori')
plt.xlabel('Luna')
plt.ylabel('Vânzări')
plt.grid(True)
plt.savefig('monthly_sales_plot_with_values.png')
plt.show()