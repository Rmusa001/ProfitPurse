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
    
    total_revenue = qty_sold * selling_price
    total_cost = qty_sold * cost_price
    discount_amount = total_revenue * discount / 100
    revenue_after_discount = total_revenue - discount
    profit = total_revenue - revenue_after_discount
    
    if profit > 0:
        status = "Profit"
    elif profit == 0:
        status = "Break Even"
    else:
        status = "Loss"
        
    print("=======================================")
    print("BIZ PROFIT")
    print("=======================================")
    print (f"Business Name: {business_name}\nProduct Name: {product_name}\nProduct Status: {product_status}\nQuantity Sold: {qty_sold}\nTotal Revenue: {total_revenue}\nTotal Cost: {total_cost}\nProfit: {profit}\nStatus: {status}")

calculate_profit()


