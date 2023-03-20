# def f(n):
#     if (n > 1):
#         return n * f(n-1)
#     else:
#         return 1

def f(n):
    a = 1
    for i in range(1, n+1):
        a *= i
    return a

t = int(input())

for i in range(t):
    n,m = map(int, input().split())
    r = f(m) // (f(n) * f(m-n))
    print(r)
