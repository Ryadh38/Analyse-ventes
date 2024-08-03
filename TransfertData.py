import sqlite3
import pandas as pd 

#Chemin vers le fichier csv :
csv_file_path = 'donnes.csv'

# Connection avec la base de données:
conn = sqlite3.connect ('data.db')
c= conn.cursor()

#Lecture des données dufichier csv :
df = pd.read_csv(csv_file_path)

#transfert des donées dans SQL:
df.to_sql('sales', conn, if_exists='replace', index=False)

# verification 
result = c.execute('SELECT * FROM sales LIMIT 5').fetchall()
print(result)
#fermuture :
conn.close()

