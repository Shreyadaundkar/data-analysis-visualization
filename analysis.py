import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file
df = pd.read_csv("data.csv")

# Display first few rows
print("Dataset Preview:")
print(df.head())

# Basic statistics
print("\nStatistical Summary:")
print(df.describe())

# Calculate average sales
average_sales = df['Sales'].mean()
print("\nAverage Sales:", average_sales)

# Bar Chart: Average Sales by Category
plt.figure(figsize=(6,4))
df.groupby('Category')['Sales'].mean().plot(kind='bar', color='skyblue')
plt.title("Average Sales by Category")
plt.ylabel("Sales")
plt.xlabel("Category")
plt.tight_layout()
plt.show()

# Scatter Plot: Advertising vs Sales
plt.figure(figsize=(6,4))
plt.scatter(df['Advertising'], df['Sales'], color='green')
plt.title("Advertising vs Sales")
plt.xlabel("Advertising Budget")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# Heatmap: Correlation Matrix
plt.figure(figsize=(6,4))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()
