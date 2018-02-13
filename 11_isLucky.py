'''
給一組票券號碼，若前半與後半總合相同，則為幸運

https://codefights.com/arcade/intro/level-3/3AdBC97QNuhF6RwsQ

Created on 2018年2月12日
@author: rocky.wang
'''

def isLucky(n: int):
    
    s = str(n)

    pivot = len(s) // 2

    left, right = s[:pivot], s[pivot:] 

    return sum(map(int, left)) == sum(map(int, right))


# def isLucky(n):
#     
#     n = str(n)
#     half = int(len(n) / 2)
# 
#     n1 = n[0: half]
#     list1 = [int(x) for x in n1]
#     
#     n2 = n[half:]
#     list2 = [int(x) for x in n2]
# 
#     return sum(list1) == sum(list2)

if __name__ == '__main__':
    
    n = 12344321
    r = isLucky(n)
    print(r)
