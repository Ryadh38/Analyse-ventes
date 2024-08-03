import sqlite3
import pandas as pd 
import matplotlib as mtp
import matplotlib.pyplot as plt

#Chemin vers le fichier csv :
csv_file_path = 'donnes.csv'

# Connection avec la base de données:
conn = sqlite3.connect ('data.db')
c= conn.cursor()

# Requête SQL pour extraire les ventes totales par produit
query_total_sales = '''
SELECT product, SUM(sales) as total_sales
FROM sales
GROUP BY product
'''

# Exécution de la requête
df_total_sales = pd.read_sql_query(query_total_sales, conn)
print("Ventes totales par produit:")
print(df_total_sales)



query_daily_sales= ''' 
SELECT date, SUM (sales) as total_sales 
FROM sales 
GROUP BY date
'''
df_daily_sales = pd.read_sql_query(query_daily_sales, conn)
print ("ventes totales par jour:")
print(df_daily_sales)

#state ventes total par produit :
print("/n Descriptif des ventes totales par produit :")
print(df_total_sales.describe())

#le top produit :
max_sales_product = df_total_sales.loc[df_total_sales['total_sales'].idxmax()]
print(f"Le top produit: {max_sales_product['product']} avec {max_sales_product['total_sales']} ventes")
#Ventes cummulée par dates :
df_daily_sales['cumulative_sales'] = df_daily_sales['total_sales'].cumsum()
print(df_daily_sales)

#Visualisation :
df_total_sales.plot(kind='bar', x='product', y='total_sales', title='Ventes Totales par Produit', legend=False)
df_daily_sales.plot(kind='line', x='date', y='total_sales', title='Ventes Quotidiennes Totales')
df_daily_sales.plot(kind='line', x='date', y='cumulative_sales', title='Ventes Cumulées par Date')

plt.show()
conn.close()








