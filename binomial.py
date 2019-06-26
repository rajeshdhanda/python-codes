import numpy as np 
import itertools
n = 4
temp = range(0, n)
possible_positons = itertools.permutations(temp)
# for i in possible_positons:
#     print i
array=[]
for term in possible_positons:
    board = np.zeros((n,n))
    for j in range(n):
        board[j,term[j]] = 1
    # print board, term, sum(sum(board))

    for i in range(n):
        for j in range(n):
            if board[i,j] == 1:
                for k in range(1,n):
                    if i-k < n and i-k >=0 and j-k < n and j-k >=0 and board[i-k,j-k] == 1:
                        board[i-k,j-k] = 0
                    if i+k < n and i+k >=0 and j-k < n and j-k >=0 and board[i+k,j-k] == 1:
                        board[i+k,j-k] = 0
    if sum(sum(board)) == 4:
        array.append(board)
        array=array[::-1]
for i in array:
    print(i)
