def calculate_profit():
    
    business_name = input('Business Name:')
    
    product_name = input('Product Name:')
    #product = ["Beads", "Earring", "Neck Chain", "Perfume Oil"]
    qty_sold= int(input('Quantity Sold:'))
    selling_price= float(input('Selling Price:'))
    cost_price= float(input('Cost Price:'))
    
    total_revenue = qty_sold * selling_price
    total_cost = qty_sold * cost_price
    profit = total_revenue - total_cost
    
    if profit > 0:
        status = "Profit"
    elif profit == 0:
        status = "Break Even"
    else:
        status = "Loss"
        
    print("=======================================")
    print("BIZ PROFIT")
    print("=======================================")
    print (f"Business Name: {business_name}\nProduct Name: {product_name}\nQuantity Sold: {qty_sold}\nTotal Revenue: {total_revenue}\nTotal Cost: {total_cost}\nProfit: {profit}\nStatus: {status}")

calculate_profit()


