def factorial(n, a=1):
    if n == 0:
        return a
    return factorial(n-1, n * a)
    
if __name__ == '__main__':
    print(factorial(6))