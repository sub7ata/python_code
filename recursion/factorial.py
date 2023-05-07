def _factorial(n):
    if n <= 1:
        return 1
    else:
        return n * _factorial(n - 1)
        

if __name__ == '__main__':
    print(_factorial(6))
    