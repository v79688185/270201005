gpa = int(input("Enter the gpa:" ))
num_of_Lectures = int(input("Enter the number: "))
if gpa <= 2.0 :
  if num_of_Lectures < 47: 
    print("not enough number of lectures for gpa")
  else:
    print("not enough gpa")
else:
   gpa >= 2.0
   if num_of_Lectures < 47:
     print("not enough number of lectures")
   else:
     print("Graduated")
