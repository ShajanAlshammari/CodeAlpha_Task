# Import the pandas library for data handling
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style for better visual aesthetics
sns.set(style='whitegrid')

# Load the dataset from the specified path (make sure the file is in this exact location)
df = pd.read_csv(r"C:\Users\saudi\Downloads\ecommerce_data.csv")

# Question: Which product category generates the most revenue?
# Question: What is the most preferred payment method?
# Question: Does delivery speed affect customer satisfaction (rating)?

# Preview the first 5 rows of the dataset
print(df.head())

# Print dataset info: column names, types, and non-null counts
print(df.info())

# Generate statistical summaries for numeric columns
print(df.describe())

# Check for missing values in each column
print(df.isnull().sum())

# Group and sum sales by product category
category_sales = df.groupby('Product Category')['Total'].sum().sort_values(ascending=False)

# Plot a bar chart of total sales by product category
plt.figure(figsize=(8, 5))
category_sales.plot(kind='bar', color='orange', title='Total Sales by Product Category')
plt.ylabel("Total Sales")
plt.xlabel("Product Category")
plt.tight_layout()
plt.show()

# Count frequency of each payment method
plt.figure(figsize=(6, 4))
payment_counts = df['Payment Method'].value_counts()


# Convert it into a DataFrame (this is required for hue support)
payment_df = pd.DataFrame({
    'Payment Method': payment_counts.index,
    'Count': payment_counts.values
})

# Create the barplot using hue to avoid the deprecation warning
plt.figure(figsize=(6, 4))
sns.barplot(data=payment_df, x='Payment Method', y='Count', hue='Payment Method', palette='Set2', legend=False)
plt.title('Payment Method Distribution')
plt.xlabel('Payment Method')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# Hypothesis Test: Faster delivery leads to higher ratings

# Scatter plot showing relationship between delivery time and rating
plt.figure(figsize=(6, 4))
sns.scatterplot(x='Delivery Days', y='Rating', data=df)
plt.title('Delivery Days vs Rating')
plt.xlabel('Delivery Days')
plt.ylabel('Customer Rating')
plt.tight_layout()
plt.show()

# Sum total sales grouped by customer type
customer_type_sales = df.groupby('Customer Type')['Total'].sum()

# Plot pie chart of sales contribution by customer type
plt.figure(figsize=(5, 5))
customer_type_sales.plot(kind='pie', autopct='%1.1f%%', title='Sales by Customer Type')
plt.ylabel('')
plt.tight_layout()
plt.show()

# Group by product category and calculate total quantity and sales
summary = df.groupby('Product Category')[['Quantity', 'Total']].sum()

# Save the summary to a CSV file
summary.to_csv("sales_summary.csv")
print("\n✅ Sales summary has been saved as 'sales_summary.csv'")
