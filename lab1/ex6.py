book_price = 24.95
#cost of this book we used discount percentage
wholesale_cost_book = book_price * (60/100)
copy_cost = 3
additional_copy_cost = 0.75
# we used 59 because they spend 3 for first copy and they have to spend 0.75 for additional copies and we have 60 copies so 59 copies are additional
wholesale_cost = wholesale_cost_book + copy_cost + additional_copy_cost * 59
print(wholesale_cost)



