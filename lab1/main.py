age = int(input("Enter your age: "))
normal_ticket_price = 3
discount=50
if age<6 and age>60:
  print("free")
else:
  if age>=6 and age<=18:
    discount_ticket_price=normal_ticket_price - normal_ticket_price*(1-(50/100))
    print(discount_ticket_price)
  else:
    print(normal_ticket_price)
    
    
 





  
  








    

  





