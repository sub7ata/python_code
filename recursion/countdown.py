from sys import getrecursionlimit, setrecursionlimit
print(getrecursionlimit())
setrecursionlimit(2000)

def count_down(n):
    if n == 0:
        print('Done')
    else:
        print(n)
        count_down(n-1)
   
     
if __name__ == '__main__':
    count_down(1200)
    