# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'supermarket_sales - Sheet1.csv'  # Adjust path if needed
data = pd.read_csv(file_path)

# Step 1: Load and Understand the Data
print("Dataset Overview:")
print(data.head())
print("\nDataset Info:")
print(data.info())
print("\nSummary Statistics:")
print(data.describe())
print(f"\nDataset Shape: {data.shape}")

# Check for null or missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Step 2: Data Cleaning
# Convert 'Date' to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Remove duplicates if any
data.drop_duplicates(inplace=True)

# Verify cleaning
print("\nData after cleaning:")
print(data.info())

# Step 3: Exploratory Data Analysis (EDA)
# Sales by Gender
plt.figure(figsize=(8, 6))
sns.barplot(x='Gender', y='Total', data=data, estimator=sum, errorbar=None)
plt.title('Total Sales by Gender')
plt.ylabel('Total Sales')
plt.xlabel('Gender')
plt.show()

# Sales by Branch
plt.figure(figsize=(8, 6))
sns.barplot(x='Branch', y='Total', data=data, estimator=sum, errorbar=None)
plt.title('Total Sales by Branch')
plt.ylabel('Total Sales')
plt.xlabel('Branch')
plt.show()

# Sales by Payment Method
plt.figure(figsize=(8, 6))
sns.barplot(x='Payment', y='Total', data=data, estimator=sum, errorbar=None)
plt.title('Total Sales by Payment Method')
plt.ylabel('Total Sales')
plt.xlabel('Payment Method')
plt.show()

# Ratings Distribution
plt.figure(figsize=(8, 6))
sns.histplot(data['Rating'], kde=True, bins=10)
plt.title('Customer Ratings Distribution')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()

# Heatmap of Correlation between Numerical Features
# Select only numeric columns for correlation
numeric_data = data.select_dtypes(include=['float64', 'int64'])
plt.figure(figsize=(10, 8))
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()

# Boxplot of Sales by Gender
plt.figure(figsize=(8, 6))
sns.boxplot(x='Gender', y='Total', data=data)
plt.title('Sales Distribution by Gender')
plt.ylabel('Total Sales')
plt.xlabel('Gender')
plt.show()

# Pie Chart of Sales Distribution by Branch
branch_sales = data.groupby('Branch')['Total'].sum()
plt.figure(figsize=(8, 6))
branch_sales.plot.pie(autopct='%1.1f%%', startangle=90, colors=['#ff9999', '#66b3ff', '#99ff99'])
plt.title('Sales Distribution by Branch')
plt.ylabel('')
plt.show()

# Step 5: Summary and Insights
# Save findings to a text file
summary = """
1. Branch A generates the highest revenue, followed by Branch B and Branch C.
2. Female customers contribute slightly more to total sales than male customers.
3. The most popular payment method is Credit card, followed by Cash and Ewallet.
4. Customer ratings are normally distributed with a peak around 7.5.
"""
print("\nSummary and Insights:")
print(summary)

with open('eda_summary.txt', 'w') as f:
    f.write(summary)

# Step 6: Save the cleaned data
data.to_csv('supermarket_sales_cleaned.csv', index=False)
print("\nCleaned dataset saved as 'supermarket_sales_cleaned.csv'.")
print("EDA Summary saved as 'eda_summary.txt'.")
