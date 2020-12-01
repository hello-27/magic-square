#Imports
import numpy as np

#Functions
def check_square():
    sd = sum([magic_square[i,i] for i in range(0,n)])
    sr = sum([magic_square[i,] for i in range(0,n)])
    sc = sum([magic_square[:,i] for i in range(0,n)])
    su = sum([magic_square[n - 1 - i,i] for i in range(0,n)])
    
    return sd if sd == su and np.array_equal(sc, sr) and sd == sc[0] else 0

#Initialization
while True:
    n = int(input('dimension of magic square: '))
    if n%2 == 1:
        break
    else:
        print('please input odd number')
                
magic_square = np.zeros((n,n), dtype=int)        

x = n-1
y = int((n-1)/2)
magic_square[x, y] = 1

#Logic
for number in range(2,n*n+1):
    if x + 1 < n and y + 1 < n:
        if magic_square[x + 1, y + 1] == 0:
            magic_square[x + 1, y + 1] = number
        else:
            magic_square[x - 1, y] = number
    if x + 1 > n - 1 or y + 1 > n - 1:
        if x == n - 1 and y != n - 1:
            if magic_square[0, y + 1] == 0:
                magic_square[0, y + 1] = number
            else:
                magic_square[x - 1, y] = number
        if x != n - 1 and y == n - 1:
            if magic_square[x + 1, 0] == 0:
                magic_square[x + 1, 0] = number
            else:
                magic_square[x - 1, y] = number
        if x == n - 1 and y == n - 1:
            magic_square[x - 1, y] = number

    x = int(np.where(magic_square == number)[0])
    y = int(np.where(magic_square == number)[1])

#Result
print('\n')
print(magic_square)
print('\n')
print(r'sum of each row column and diagonal (n*(n*n + 1)/2): ' + str(int(n*(n*n + 1)/2)))
