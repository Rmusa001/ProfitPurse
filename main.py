business_list = []

def calculate_profit():
    
    business_name = input("Business Name: ")
    product_name = input("Product/Service Name: ")
    product_status = "Available"

    while True:
        try:
            qty_sold = int(input("Quantity Sold: "))

            if qty_sold > 0:
                break
            else:
                print("Quantity must be greater than 0.")

        except ValueError:
            print("Please enter a whole number.")

    while True:
        try:
            selling_price = float(input("Selling Price: "))

            if selling_price > 0:
                break
            else:
                print("Selling price must be greater than 0.")

        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            cost_price = float(input("Cost Price: "))

            if cost_price > 0:
                break
            else:
                print("Cost price must be greater than 0.")

        except ValueError:
            print("Please enter a valid number.")
      
    while True:
        try:
            discount = float(input("Discount (%): "))
            if 0 <= discount <= 100:
                break
            else:
                print("Discount must be between 0 and 100.")        
        except ValueError:
            print("Please enter a valid number.")
                
        
    total_revenue = round(qty_sold * selling_price, 2)
    total_cost = round(qty_sold * cost_price, 2)
    discount_amount = round((total_revenue * discount) / 100, 2)
    revenue_after_discount = round(total_revenue - discount_amount, 2)

    profit = round(revenue_after_discount - total_cost, 2)

    if revenue_after_discount > 0:
        profit_margin = round((profit / revenue_after_discount) * 100, 2)
    else:
        profit_margin = 0

    if profit > 0:
        status = "Profit"
    elif profit == 0:
        status = "Break Even"
    else:
        status = "Loss"
    transaction = {
            "business_name": business_name,
            "product_name": product_name,
            "quantity": qty_sold,
            "profit": profit
    }
    business_list.append(transaction)

    print("=======================================")
    print("BIZ PROFIT")
    print("=======================================")

    print(
        f"Business Name: {business_name}\n"
        f"Product Name: {product_name}\n"
        f"Product Status: {product_status}\n"
        f"Quantity Sold: {qty_sold}\n"
        f"Total Revenue: ₦{total_revenue:,.2f}\n"
        f"Total Cost: ₦{total_cost:,.2f}\n"
        f"Discount Amount: ₦{discount_amount:,.2f}\n"
        f"Revenue After Discount: ₦{revenue_after_discount:,.2f}\n"
        f"Profit: ₦{profit:,.2f}\n"
        f"Profit Margin: {profit_margin}%\n"
        f"Status: {status}"
    )

calculate_profit()
print(business_list)
