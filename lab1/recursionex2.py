def Hailstone(n):
    if n == 1:
        print(n)  
    elif n % 2 == 1:
        print(n)
        return Hailstone(3*n+1)     
    elif n % 2 == 0:
        print(n)
        return Hailstone(n//2)
Hailstone(5)  