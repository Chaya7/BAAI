products = [
    {"name": "Laptop", "price": 1200, "category": "Electronics"},
    {"name": "Shirt", "price": 45, "category": "Clothing"},
    {"name": "Phone", "price": 800, "category": "Electronics"},
    {"name": "Shoes", "price": 120, "category": "Clothing"},
    {"name": "Tablet", "price": 350, "category": "Electronics"},
    {"name": "Jacket", "price": 95, "category": "Clothing"},
    {"name": "Book", "price": 25, "category": "Books"},
    {"name": "Headphones", "price": 150, "category": "Electronics"}
]

print("=== PRODUCT DISCOUNT CALCULATOR ===\n")

total_original = 0
total_discount = 0
total_final = 0
total_products = len(products)

for product in products:
    name = product["name"]
    price = product["price"]
    category = product["category"]

    # Determine discount based on category and price
    if category == "Electronics":
        if price >= 1000:
            discount = 20
        elif price >= 500:
            discount = 15
        else:
            discount = 10
    elif category == "Clothing":
        if price >= 100:
            discount = 25
        else:
            discount = 15
    elif category == "Books":
        discount = 10


    final_price = price * (1 - discount / 100)

    # Update totals
    total_original += price
    total_discount += price * discount / 100
    total_final += final_price

    # Output product details
print(f"Product: {name}")
print(f"   Category: {category}")
print(f"   Original Price: ${price:.2f}")
print(f"   Discount: {discount}%")
print(f"   Final Price: ${final_price:.2f}\n")

# Output summary
print("=== SUMMARY ===")
print(f"Total Products: {total_products}")
print(f"Total Original Price: ${total_original:.2f}")
print(f"Total Discount: ${total_discount:.2f}")
print(f"Total Final Price: ${total_final:.2f}")