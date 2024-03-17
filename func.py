def calculate_discount(price,discount_percent):
  if discount_percent>=0.2:
    new_price=price-(discount_percent*price)
    print(new_price)
  else:
    print(price)

  
calculate_discount(float(input("enter price")),float(input("enter discount in decimal")))
