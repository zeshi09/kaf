import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Подключение к базе данных
conn = sqlite3.connect('Locations_fin.db')

# Загрузка данных из таблицы
query = "SELECT District, Selsovet, Chrononym FROM locations"
df = pd.read_sql_query(query, conn)

conn.close()  # Закрываем соединение

# Группируем данные по District и Chrononym, считаем количество записей для каждой пары
district_chrononym = df.groupby(['District', 'Chrononym']).size().reset_index(name='Count')

# Построение графика
plt.figure(figsize=(12, 8))
sns.barplot(data=district_chrononym, x='District', y='Count', hue='Chrononym')
plt.title('Соотношение районов и хронологий', fontsize=16)
plt.xlabel('Район', fontsize=14)
plt.ylabel('Количество записей', fontsize=14)
plt.xticks(rotation=45)
plt.legend(title='Хронология', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('graph.png', bbox_inches='tight')

