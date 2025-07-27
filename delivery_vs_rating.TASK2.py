import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset
df = pd.read_csv(r"C:\Users\saudi\Downloads\ecommerce_data.csv")

# Create folder if not exists
os.makedirs("visualizations", exist_ok=True)

# Plotting the scatter plot
plt.figure(figsize=(6, 4))
sns.scatterplot(x='Delivery Days', y='Rating', data=df, color='teal', s=70, alpha=0.8)

# Titles and labels
plt.title('Delivery Days vs Customer Rating', fontsize=14, fontweight='bold')
plt.xlabel('Delivery Days')
plt.ylabel('Customer Rating')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

# Save the figure
plt.savefig('visualizations/delivery_vs_rating.png')
plt.show()
