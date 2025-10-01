MEMO = {}
def fibonacci(n: int) -> int:
    if n in MEMO:
        print("hit memo")
        return MEMO[n]
    
    if n <= 1:
        print("base case", n)
        return n
    
    print("computing", n)
    MEMO[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return MEMO[n]

print(fibonacci(10)) # 55
print(fibonacci(5)) # 5 (0, 1, 1, 2, 3, 5)

def fib(n):
    MEM = [0, 1]
    for i in range(2, n + 1):
        MEM.append(MEM[i - 1] + MEM[i - 2])
    return MEM[n]
print(fib(10)) # 55
