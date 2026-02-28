import pandas as pd

# Load data - Replace 'revenue.csv' with your actual file path if using CSV.
# revenue_df = pd.read_csv('revenue.csv')

# 1. Identify missing values
missing_values = revenue_df.isnull().sum()
print("Missing values per column:\n", missing_values)

# 2. Handle missing data appropriately
# Option 1: Drop rows with missing 'customer_id' or 'date' (assumed essential fields)
revenue_df = revenue_df.dropna(subset=['customer_id', 'date'])

# Option 2: For optional fields such as 'customer_name', fill missing with 'Unknown'
revenue_df['customer_name'] = revenue_df['customer_name'].fillna('Unknown')

# For 'revenue', if missing, fill with 0 or another strategy (if business logic allows)
revenue_df['revenue'] = revenue_df['revenue'].fillna(0)

# 3. Convert date columns
# Standardize 'date' column to datetime, coerce errors to NaT (missing value)
revenue_df['date'] = pd.to_datetime(revenue_df['date'], errors='coerce')

# Drop rows where date conversion failed (optional, but ensures clean date column)
revenue_df = revenue_df.dropna(subset=['date'])

# 4. Remove duplicates
# Remove exact duplicate rows
revenue_df = revenue_df.drop_duplicates()

# Optionally, remove duplicates based on subset of key columns
# revenue_df = revenue_df.drop_duplicates(subset=['customer_id', 'date'])

# 5. Prepare the dataset for Power BI analysis
# Rename columns for Power BI best practices (e.g., spaces instead of underscores, Pascal Case)
revenue_df = revenue_df.rename(columns={
    'customer_id': 'Customer ID',
    'customer_name': 'Customer Name',
    'date': 'Date',
    'revenue': 'Revenue'
})

# Reset index for clean export
revenue_df = revenue_df.reset_index(drop=True)

# Export cleaned data for Power BI
# revenue_df.to_csv('revenue_cleaned.csv', index=False)

# Print preview of cleaned data
print(revenue_df.head())