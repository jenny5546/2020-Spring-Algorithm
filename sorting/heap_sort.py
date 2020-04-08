"""
문병로 교수님 알고리즘 4강. 정렬
힙 정렬을 파이썬으로 짜서 연습해보자!

"""

array = [3,11,14,10,9,7,4,13,5,8,16,13,2,25,12,3,5]

def heapSort(arr,n):
    buildHeap(arr,n)
    for size in range(n-1,0,-1):
        temp=arr[0]
        arr[0]=arr[size]
        arr[size]=temp
        heapify(arr,0,size)


def buildHeap(arr,n):
    for i in range(n//2,-1,-1):
        heapify(arr,i,n)

def heapify(arr,i,n):
    left = 2*i+1
    right = 2*i+2
    if right <= n-1: # two children
        if arr[left] < arr[right]:
            smaller = left
        else:
            smaller= right
    elif left <= n-1: # one children
        smaller= left
    else: 
        return 

    if (arr[smaller]<arr[i]):
        temp=arr[i]
        arr[i]=arr[smaller]
        arr[smaller]=temp
        heapify(arr,smaller,n)
    print(arr)


heapSort(array,17)
for i in reversed(array):
    print(i, end='  ')
print()
