age = int(input("Enter your age: "))
normal_ticket_price = 3
discount=50
if 6<=age<=60:
  if 6<=age<18:
    print(normal_ticket_price*discount/100)
  else:
    print(normal_ticket_price)
else:    
  print("It is free")

 