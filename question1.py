import decimal

def div(a,b,n):
    return round(a/b, n)

a = int(input("Enter a value of divident : "))
b = int(input("Enter a value of Divisor : "))
n = int(input("How many number require after decimal : "))

print(div(a,b,n))
