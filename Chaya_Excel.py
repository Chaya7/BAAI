
# Chaya, 2025/10/08
# file: Chaya_excel.py
# Calculate sum of columm in Excel file
#

import pandas as pd

# 1. Input
df = pd.read_excel('Financial_Sample.xlsx')

# 2. Process
sum = df.select_dtypes(include='number').sum()
sums ['Name'] = 'total' 
df_with_total = pd.contat([df, pd.DataFrame(sums)]),ignore_index=True

# 3. Output
print(df_with_total)
df_with_total.to_excel('otput.xlsx', index=False)