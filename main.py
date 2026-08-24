def calculate_profit():
    
    business_name = input('Business Name:')
    
    product_name = input('Product Name:').strip()
    product = ["Beads", "Earring", "Neck Chain", "Perfume Oil"]
    if product_name in product:
        product_status = "Available"
    else:
        product_status = "it's not available"
        print("it's not available")
        return
    qty_sold= int(input('Quantity Sold:'))
    selling_price= float(input('Selling Price:'))
    cost_price= float(input('Cost Price:'))
    discount = float(input("Discount:"))
    
    total_revenue = round(qty_sold * selling_price, 2)
    total_cost = round(qty_sold * cost_price, 2)
    discount_amount = round((total_revenue * discount) / 100, 2)
    revenue_after_discount = round(total_revenue - discount_amount, 2)
    profit = round (revenue_after_discount - total_cost, 2)  
    profit_margin = (profit / revenue_after_discount) * 100
    if revenue_after_discount > 0:
        profit_margin = "Profit Margin"
    else:
        profit_margin = ""
    
    if profit > 0:
        status = "Profit"
    elif profit == 0:
        status = "Break Even"
    else:
        status = "Loss"
        
    print("=======================================")
    print("BIZ PROFIT")
    print("=======================================")
    print (f"Business Name: {business_name}\nProduct Name: {product_name}\nProduct Status: {product_status}\nQuantity Sold: {qty_sold}\nTotal Revenue: ₦{total_revenue}\nTotal Cost: ₦{total_cost}\nDiscount Amount: ₦{discount_amount}\nRevenue After Discount: ₦{revenue_after_discount}\nProfit: ₦{profit}\nProfit Margin: {profit_margin}%\nStatus: {status}")

calculate_profit()


