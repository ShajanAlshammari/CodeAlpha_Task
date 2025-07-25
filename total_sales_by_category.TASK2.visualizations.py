import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset
df = pd.read_csv(r"C:\Users\saudi\Downloads\ecommerce_data.csv")

# Create folder if it doesn't exist
os.makedirs("visualizations", exist_ok=True)

# Group sales by product category
category_sales = df.groupby('Product Category')['Total'].sum().sort_values(ascending=False)

# Plot
plt.figure(figsize=(8, 5))
category_sales.plot(kind='bar', color='#FF8C00')
plt.title('Total Sales by Product Category', fontsize=14, fontweight='bold')
plt.xlabel('Product Category', fontsize=12)
plt.ylabel('Total Sales', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Save image
plt.savefig('visualizations/total_sales_by_category.png')
plt.show()
