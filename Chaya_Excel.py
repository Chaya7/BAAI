
# Chaya, 2025/10/08
# file: Chaya_excel.py
# Calculate sum of columm in Excel file
#

import pandas as pd

# 1. Input
df = pd.read_excel('Financial_Sample.xlsx')

# 2. Process
sum = df.select_dtypes(include='number').sum()

# 3. Output
print(f'Sum {sum}')