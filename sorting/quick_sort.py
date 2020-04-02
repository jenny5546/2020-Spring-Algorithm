"""
문병로 교수님 알고리즘 4강. 정렬
퀵 정렬을 파이썬으로 짜서 연습해보자!
"""
array = [0,5,31,3,4,2,1]

def swap(a,b):
    temp = a
    a = b
    b= temp

def partition(arr,l,r):
    pivot = arr[l]
    last = l
    for elem in range(l+1,r+1):
        if arr[elem]<pivot:
            last+=1
            temp =arr[last]
            arr[last]=arr[elem]
            arr[elem]=temp

    temp2 =arr[last]
    arr[last]=arr[l]
    arr[l]=temp2
    return last

def quickSort(arr, l,r):
    if l<r:
        pivot = partition(arr,l,r)
        quickSort(arr,l,pivot-1)
        quickSort(arr,pivot+1,r)

quickSort(array,0,len(array)-1)
print(array)