leap_year = int(input("Enter the year: "))
if leap_year % 4 == 0:
  if leap_year % 100 == 0:
    if leap_year % 400 == 0:
      print("it is leap year")
    else:
      print("it is not leap year")
  else:
    print("it is a leap year")
else:
  print("it is not leap year") 