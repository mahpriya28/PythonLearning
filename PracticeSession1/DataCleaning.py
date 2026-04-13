import pandas as pd

df = pd.read_csv("employees.csv")
print(df.head())

print(df.info())       # check data types
print(df.isnull().sum())  # missing values
print(df.describe())   # numeric summary

# Convert to numeric (invalid becomes NaN)
df['age'] = pd.to_numeric(df['age'], errors='coerce')

# Fill missing with median
df['age'].fillna(df['age'].median(), inplace=True)

# Remove unrealistic ages
df = df[(df['age'] >= 18) & (df['age'] <= 65)]

# Remove symbols and commas
df['salary'] = df['salary'].astype(str).str.replace(r'[^\d.]', '', regex=True)

# Convert to numeric
df['salary'] = pd.to_numeric(df['salary'], errors='coerce')

# Fill missing with median
df['salary'].fillna(df['salary'].median(), inplace=True)

# Standardize text
df['country'] = df['country'].str.strip().str.lower()

# Replace variations
df['country'] = df['country'].replace({
    'india': 'India',
    'ind': 'India',
    'usa': 'USA',
    'us': 'USA'
})

df = df.drop_duplicates()
df = df.drop_duplicates(subset='email')
# Remove spaces
df['email'] = df['email'].str.strip()

# Basic validation
df = df[df['email'].str.contains(r'^[\w\.-]+@[\w\.-]+\.\w+$', na=False)]

# Reset index after deletions
df.reset_index(drop=True, inplace=True)

df.to_csv("cleaned_employees.csv", index=False)