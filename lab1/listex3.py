n=int(input("How many student: "))
examlist=[]
for i in range(n):
  midterm1=int(input("Enter the first midterm: "))
  midterm2=int(input("Enter the first midterm2: "))
  final = int(input("Enter the final exam: "))
  examlist.append([midterm1,midterm2,final])
print(examlist)

averagegrades=[]

for j in examlist:
  averagegrades.append(j[0]*0.3+j[1]*0.3+j[2]*0.4)
print(averagegrades)