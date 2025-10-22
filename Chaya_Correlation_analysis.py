#
# Chaya, 2025/10/22
# File: Chaya_Correlation_analysis.py
# Short description of the task
#

import pandas as pd

# 1. Input
df = pd.read_csv('simple_data.csv')

# 2. Process
print(df.isnull().sum())
print(df.isnull().sum().sum())

# # 3. Output
# print("Data loaded successfully!")
# print(f"Dataset shape:{df.shape}")