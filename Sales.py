# Define a list to store monthly sales
monthly_sales = []

# Function to enter monthly sales data
def enter_monthly_sales():
    for month in range(1, 13):
        sales = float(input(f"Enter sales for month {month}: $"))
        monthly_sales.append(sales)

# Function to calculate the annual sales average
def calculate_annual_average():
    total_sales = sum(monthly_sales)
    annual_average = total_sales / len(monthly_sales)
    return annual_average

# Program execution
print("Enter monthly sales data:")
enter_monthly_sales()

annual_average_sales = calculate_annual_average()
print(f"Annual Average Sales: ${annual_average_sales:.2f}")