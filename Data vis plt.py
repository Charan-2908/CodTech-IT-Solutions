import matplotlib.pyplot as plt
import numpy as np

# Sample data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values_bar_chart = np.random.randint(50, 100, size=len(categories))
values_pie_chart = np.random.randint(20, 60, size=len(categories))
values_line_graph = np.random.randint(30, 80, size=len(categories))

# Bar Chart
plt.figure(figsize=(12, 5))
plt.bar(categories, values_bar_chart, color='skyblue')
plt.title('Bar Chart Example')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

# Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(values_pie_chart, labels=categories, autopct='%1.1f%%', colors=[
        'lightcoral', 'lightgreen', 'lightskyblue', 'lightyellow'])
plt.title('Pie Chart Example')
plt.show()

# Line Graph
plt.figure(figsize=(8, 5))
plt.plot(categories, values_line_graph, marker='o',color='orange', label='Line Graph')
plt.title('Line Graph Example')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.legend()
plt.show()
