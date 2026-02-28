import pandas as pd
import os

# Load your file (adjust the path if needed)
input_file = 'case_study_original.xlsx'

# Read the relevant sheets
df_revenues = pd.read_excel(input_file, sheet_name='Revenues')
df_rrw = pd.read_excel(input_file, sheet_name='Recurring Revenue Waterfall')
df_category = pd.read_excel(input_file, sheet_name='Category')
df_customer = pd.read_excel(input_file, sheet_name='Customer')

# ---------------------
# ---- Revenues Tab ----
# 1. Identify and print missing values
print("Revenues missing values:\n", df_revenues.isnull().sum())
# 2. Drop rows where Company, Customer, or Date are missing
df_revenues = df_revenues.dropna(subset=['Company', 'Customer', 'Date'])
# 3. Fill missing revenue with 0
df_revenues['Value EUR'] = df_revenues['Value EUR'].fillna(0)
# 4. Convert Date
df_revenues['Date'] = pd.to_datetime(df_revenues['Date'], errors='coerce')
df_revenues = df_revenues.dropna(subset=['Date'])
# 5. Remove duplicates
df_revenues = df_revenues.drop_duplicates()

# --------------------------------
# ---- Recurring Revenue Waterfall Tab ----
print("Recurring Revenue Waterfall missing values:\n", df_rrw.isnull().sum())
df_rrw = df_rrw.dropna(subset=['Company', 'Customer', 'Date'])
df_rrw['Value EUR'] = df_rrw['Value EUR'].fillna(0)
df_rrw['Category'] = df_rrw['Category'].fillna('Unknown')
df_rrw['Date'] = pd.to_datetime(df_rrw['Date'], errors='coerce')
df_rrw = df_rrw.dropna(subset=['Date'])
df_rrw = df_rrw.drop_duplicates()

# -----------------
# ---- Category Tab ----
print("Category missing values:\n", df_category.isnull().sum())
df_category = df_category.fillna({
    'Category': 'Unknown',
    'Category Subgroup': 'Unknown',
    'Category Group': 'Unknown'
})
numeric_columns = ['Gross Increase', 'Net Increase']
for col in numeric_columns:
    df_category[col] = pd.to_numeric(df_category[col], errors='coerce').fillna(0)
df_category = df_category.drop_duplicates()

# -----------------
# ---- Customer Tab ----
print("Customer missing values:\n", df_customer.isnull().sum())
df_customer = df_customer.dropna(subset=['Customer', 'Country ID'])
df_customer = df_customer.drop_duplicates()

# -----------------
# Create processed folder if it doesn't exist
os.makedirs('processed', exist_ok=True)

# Write cleaned file
output_file = os.path.join('processed', 'case_study_original.xlsx')
with pd.ExcelWriter(output_file) as writer:
    df_revenues.to_excel(writer, sheet_name='Revenues', index=False)
    df_rrw.to_excel(writer, sheet_name='Recurring Revenue Waterfall', index=False)
    df_category.to_excel(writer, sheet_name='Category', index=False)
    df_customer.to_excel(writer, sheet_name='Customer', index=False)

print(f"Cleaned file saved to: {output_file}")