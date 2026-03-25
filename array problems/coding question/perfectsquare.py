def perfectsq(n):
    s=int(n**0.5)
    if s*s==n:
        return "perfect square"
    else:
        return "not perfect square"
n=int(input("enter the number:"))
print(perfectsq(n))
