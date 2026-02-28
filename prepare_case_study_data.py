import pandas as pd

# Load the dataset from Excel
# Adjust the path as needed if your file or sheet names differ
df = pd.read_excel("data/raw/case_study_original.xlsx")

# 1. Identify missing values
# Show the count of missing values in each column
print("Missing values per column:\n", df.isnull().sum())

# 2. Handle missing data appropriately

# If customer_id or date is missing, we can't analyze those rows, so drop them
df = df.dropna(subset=['customer_id', 'date'])

# For customer_name, fill missing names with "Unknown"
df['customer_name'] = df['customer_name'].fillna("Unknown")

# For revenue, fill missing with 0 (or, depending on business logic, you may choose to drop or impute another way)
df['revenue'] = df['revenue'].fillna(0)

# 3. Convert date columns

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# After conversion, there may be invalid (NaT) dates, drop those
df = df.dropna(subset=['date'])

# 4. Remove duplicates

# Remove exact duplicate rows
df = df.drop_duplicates()

# Alternatively, if duplicate is defined by customer_id, date, keep last and drop others
# df = df.drop_duplicates(subset=['customer_id', 'date'], keep='last')

# 5. Prepare the dataset for Power BI analysis

# Optionally: standardize column names (remove spaces, make lowercase)
df.columns = [col.strip().lower() for col in df.columns]

# Optionally: sort data (e.g., by customer and date)
df = df.sort_values(['customer_id', 'date'])

# Save cleaned data as CSV for Power BI import
df.to_csv("data/processed/case_study_prepared.csv", index=False)

# Print the prepared DataFrame head as a quick check
print(df.head())

# -------------------------
# Summary of steps:
# - Loaded data from Excel
# - Identified missing values
# - Handled missing data (dropped critical NAs, set sensible defaults)
# - Converted date columns to datetime
# - Removed duplicate rows
# - Standardized columns for Power BI
# - Saved processed data for further analysis
