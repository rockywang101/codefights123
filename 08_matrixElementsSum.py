'''

https://codefights.com/arcade/intro/level-2/xskq4ZxLyqQMCLshr

Created on 2018年2月5日
@author: rocky.wang
'''

def matrixElementsSum(matrix):
    total = 0
    for w in range(len(matrix[0])): # width
        for h in range(len(matrix)): # height
            if matrix[h][w] == 0:
                break
            else:
                total += matrix[h][w]
    return total


matrix = [[0, 1, 1, 2], 
          [0, 5, 0, 0], 
          [2, 0, 3, 3]]

total = matrixElementsSum(matrix)
print("sum is %s" %(total))



'''
First version not good.
'''
def matrixElementsSumOld(matrix):
     
    noteArr = []
    for i in range(len(matrix[0])):
        noteArr.append("O")
     
    total = 0
    for arr in matrix:
        for i in range(len(arr)):
            if noteArr[i] == "X":
                pass
            else:
                if arr[i] == 0:
                    noteArr[i] = 'X'
                else:
                    total += arr[i]
               
    return total
