import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset
df = pd.read_csv(r"C:\Users\saudi\Downloads\ecommerce_data.csv")

# Ensure folder exists
os.makedirs("visualizations", exist_ok=True)

# Count the number of times each payment method was used
payment_counts = df['Payment Method'].value_counts()

# Convert counts to DataFrame to use hue and avoid warning
payment_df = pd.DataFrame({
    'Payment Method': payment_counts.index,
    'Count': payment_counts.values
})

# Plotting
plt.figure(figsize=(6, 4))
sns.barplot(data=payment_df, x='Payment Method', y='Count', hue='Payment Method', palette='Set2', legend=False)
plt.title('Payment Method Distribution', fontsize=14, fontweight='bold')
plt.xlabel('Payment Method')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()

# Save figure
plt.savefig('visualizations/payment_method_distribution.png')
plt.show()
