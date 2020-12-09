password = "emr365"
p1 = input("Enter your password: ")
while True:
  p1 = input("It is wrong, Enter your password: ")
  if p1 == password:
    print("welcome")
    break