import plotly.express as px
import pandas as pd
import sqlite3

# Извлечение данных из базы данных
conn = sqlite3.connect('Locations_fin.db')
df = pd.read_sql('SELECT District, Chrononym FROM locations ORDER BY Chrononym ASC', conn)

# Агрегация данных по району и хронологии
district_chrononym = df.groupby(['District', 'Chrononym']).size().reset_index(name='Count')

# Сортировка хронимов по алфавиту для оси X
chrononym_order = sorted(district_chrononym['Chrononym'].unique())

# Создание интерактивного графика
fig = px.bar(district_chrononym, x='District', y='Count', color='Chrononym', 
             title='Соотношение районов и хрононимов',
             labels={'District': 'Район', 'Count': 'Количество записей', 'Chrononym': 'Хрононим'},
             category_orders={'Chrononym': chrononym_order})  # Указание порядка для Chrononym

fig.write_html("interactive_graph.html")
# круговой
fig = px.pie(district_chrononym, names='Chrononym', values='Count', 
             title='Доли хронимов в записях',
             labels={'Chrononym': 'Хрононим', 'Count': 'Количество записей'})

fig.write_html("interactive_pie_chart.html")

fig = px.bar(district_chrononym, x='District', y='Count', color='Chrononym', 
             title='Соотношение районов и хрононимов (ленточный график)',
             labels={'District': 'Район', 'Count': 'Количество записей', 'Chrononym': 'Хрононим'},
             category_orders={'Chrononym': chrononym_order}, 
             barmode='stack')  # Ленточное отображение

fig.write_html("interactive_stacked_bar_chart.html")

fig = px.scatter(district_chrononym, x='District', y='Count', color='Chrononym', 
                 title='Распределение хронимов по районам',
                 labels={'District': 'Район', 'Count': 'Количество записей', 'Chrononym': 'Хрононим'},
                 size='Count',  # Размер точек соответствует количеству записей
                 category_orders={'Chrononym': chrononym_order})

fig.write_html("interactive_scatter_plot.html")

heatmap_data = district_chrononym.pivot(index='District', columns='Chrononym', values='Count').fillna(0)

fig = px.imshow(heatmap_data, 
                title='Тепловая карта районов и хронимов',
                labels={'x': 'Хрононим', 'y': 'Район', 'color': 'Количество записей'},
                x=chrononym_order,  # Сортировка хронимов
                color_continuous_scale='Viridis')  # Цветовая шкала

fig.write_html("interactive_heatmap.html")

