import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset
df = pd.read_csv(r"C:\Users\saudi\Downloads\ecommerce_data.csv")

# Create folder if not exists
os.makedirs("visualizations", exist_ok=True)

# Group sales by customer type
customer_type_sales = df.groupby('Customer Type')['Total'].sum()

# Pie chart
plt.figure(figsize=(5, 5))
customer_type_sales.plot(
    kind='pie',
    autopct='%1.1f%%',
    startangle=90,
    colors=sns.color_palette('Set2'),
    labels=customer_type_sales.index,
    wedgeprops={'edgecolor': 'black'}
)

# Title and formatting
plt.title('Sales by Customer Type', fontsize=14, fontweight='bold')
plt.ylabel('')
plt.tight_layout()

# Save figure
plt.savefig('visualizations/sales_by_customer_type.png')
plt.show()
