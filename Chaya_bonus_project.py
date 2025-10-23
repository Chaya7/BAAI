#
# Chaya, 2025/10/23
# File: Chaya_bonus_project.py
# Short description of the task
#

import pandas as pd
df = pd.read_excel('sales_data.xlsx')

total_bonus = 0
# use loop to go through each employee
for index, row in df.iterrows():
    name = row['Employee_name']
    sales = row['monthly_sales']
    target = row['Sales_Target']

    # check whether they met the target and the bonus
    # met target = bonus 10%
    if sales >= target:
        status = "Target Met"
        bonus = int(sales*0.10)

    # not met target = bonus 5%
    else:
        status = "Target Not Met"
        bonus = int(sales*0.05)
    print(f"{name}| {status} | Sales:${sales:,} | Bonus:${bonus:,}")

    # accumulate total bonus
    total_bonus += bonus

print(f"\nTotal Bonuses to Pay: ${total_bonus:,}")
