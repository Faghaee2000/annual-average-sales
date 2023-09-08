# Define a dictionary to store sales data for products
sales_data = {
    "Product 1": 500,
    "Product 2": 800,
    "Product 3": 600,
    "Product 4": 1200,
    "Product 5": 1000
}

# Find the best-selling product
best_selling_product = max(sales_data, key=sales_data.get)

# Display the best-selling product
print(f"Best-Selling Product: {best_selling_product}")




