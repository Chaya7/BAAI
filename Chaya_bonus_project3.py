#
# Chaya, 2025/10/24
# File: Chaya_bonus_project3.py
# Short description of the task
#

# 1. Input
import pandas as pd
df = pd.read_excel('customers.xlsx')

# 2. Process
vip = []
regular = []
new = []
total_vip_revenue = 0

for index, row in df.iterrows():
    name = row['Customer_Name']
    total = row['Total_Purchases']
    orders = row['Number_of_Orders']
    avg_order = round(total / orders, 2)
    if total > 10000:
        vip.append((name, total, orders, avg_order))
        total_vip_revenue += total
    elif total>= 5000:
        regular.append((name, total, orders, avg_order))
    else:
        new.append((name, total, orders, avg_order))


# 3. Output
print('CUSTOMER SEGMENTATION REPORT')
print('='*15)

print("VIP Customers:")
for name, total, orders, avg in vip:
    print(f"-{name} | Total: ${total:,.0f} | Orders: {orders} | Avg Order: ${avg:,.2f}")
          
print("\nRegular Customers:")
for name, total, orders, avg in regular:
    print(f"- {name} | Total: ${total:,.0f} | Orders: {orders} | Avg Order: ${avg:,.2f}")

print("\nNew Customers:")
for name, total, orders, avg in new:
    print(f"- {name} | Total: ${total:,.0f} | Orders: {orders} | Avg Order: ${avg:,.2f}")


print(f"\nTotal VIP Revenue: ${total_vip_revenue:,.0f}")