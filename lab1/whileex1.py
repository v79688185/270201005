id_password = "abc123"
password = (input("Enter the password: "))
while id_password != password:
  password = (input("Wrong password.Enter the password: "))
  if password == "help":
    print("a")
print("Welcome")    