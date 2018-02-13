'''
https://codefights.com/arcade/intro/level-3/fzsCQGYbxaEcTr2bL

Created on 2018年2月5日
@author: rocky.wang
'''
def allLongestStrings(inputArray):
    m = max(len(s) for s in inputArray)
    r = [s for s in inputArray if len(s) == m]
    return r

inputArray = ["abad", "aa", "ad", "vcd", "abax"]

print(allLongestStrings(inputArray))

arr = [2, 3, 8, 4]
list1 = (i**2 for i in arr)

print(list1)

def my_allLongestStrings(inputArray):
    
    leng = []
    for item in inputArray:
        leng.append(len(item))
    
    maxLeng = max(leng)
    
    maxWords = []
    for item in inputArray:
        if len(item) == maxLeng:
            maxWords.append(item)
    
    return maxWords




