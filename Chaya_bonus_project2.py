#
# Chaya, 2025/10/23
# File: Chaya_bonus_project2.py
# Short description of the task
#

# 1. Input

import pandas as pd
df = pd.read_excel('inventory.xlsx')

# 2. Process

print("INVENTORY REORDER REPORT")
print("="*25) 
# arrange the space
print("Products Needing Reorder:\n")

total_reorder_cost = 0
good_stock = []

# name the row
for idx, row in df.iterrows():
    product = row['Product_Name']
    current = row['Current_Stock']
    minimum = row['Minimum_stock']
    unit_price = row['Unit_Price']
    
    # provide the conditions - whether order or not
    if current < minimum:
        reorder_qty = (minimum - current)+10
        reorder_cost = reorder_qty*unit_price
        total_reorder_cost += reorder_cost
        print(f"{product}:Reorder {reorder_qty} units | Cost: ${reorder_cost:,}")
    else:
        good_stock.append(product)

print(f"\n Total Reorder Cost: ${total_reorder_cost:,}")
print("Products in Good Stock: "+",".join(good_stock))


# 3. Output