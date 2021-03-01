#Factorial(N) = N * Factorial(N-1)
# ....
# Factorial(1) = 1
def factorial(n):   #5
    if n == 1:      #5 == 1 X
        return 1

    return n * factorial(n-1) # 5 * F(4)

print(factorial(5))
