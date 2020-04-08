"""
문병로 교수님 알고리즘 4강. 정렬
Counting 정렬을 파이썬으로 짜서 연습해보자!

"""

array= [2,1,3,6,5,4,7,9,8]


def simpleCountingSort(arr, n):

    c = [0] * 10

    for j in range(n):
        c[arr[j]]+=1

    for idx in range(10):
        for i in range(c[idx]):
            print(idx, end='  ')
    print()

simpleCountingSort(array,9)

def fullCountingSort(arr,n):

    c = [0] * 10
    for j in range(n):
        c[arr[j]]+=1
        
    #######여기까지 동일#######
