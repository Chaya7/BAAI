#
# Chaya, 2025/10/22
# File: Chaya_Correlation_analysis.py
# Short description of the task
#

import pandas as pd
import numpy as np
from scipy import stats

# 1. Input
df = pd.read_csv('Correlation_Analysis_Data.csv')

df.info()


# correlation, pvalue = stats.pearsonr(df['Marketing_Spend'], df['Sales_Revenue'])

# 2. Process
# print(df.isnull().sum())
# print(df.isnull().sum().sum())
correlation_matrix=df.iloc[:,1:6]. corr()

print(correlation_matrix)

# # 3. Output
# print("Data loaded successfully!")
# print(f"Dataset shape:{df.shape}")
# print(f'Correlation:{correlation:.2f}')
# print(f'Pvalue:{pvalue}')