"""
문병로 교수님 알고리즘 4강. 정렬
퀵 정렬을 파이썬으로 짜서 연습해보자!
"""
array = [0,5,31,3,4,2,1]

def partition(arr,l,r):
    pivot = arr[l]
    less = l
    for elem in range(l+1,r):
        if arr[elem]<pivot:
            less+=1
            temp =arr[less]
            arr[less]=arr[elem]
            arr[elem]=temp

    temp2 =arr[less]
    arr[less]=arr[l]
    arr[l]=temp2
    return less

def quickSort(arr, l,r):
    if l<r:
        pivot = partition(arr,l,r)
        quickSort(arr,l,pivot-1)
        quickSort(arr,pivot+1,r)

quickSort(array,0,len(array))
print(array)