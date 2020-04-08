"""
문병로 교수님 알고리즘 4강. 정렬
Bucket 정렬을 파이썬으로 짜서 연습해보자!

"""
import math 
x = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]

def bucketSort(arr,n):

    bucket = []
    for i in range(10): 
        bucket.append([]) #[[],[],[],[],[],[],[],[],[]]

    for i in arr:
        index = int(10*i)
        bucket[index].append(i)
    result = []

    for b in bucket:
        result.extend(insertionSort(b,len(b)))
    print(result)

def insertionSort(arr, n): #insertion sort
    for i in range(1,n): # 1부터 n-1까지
        while i!=0 and arr[i]<arr[i-1] :
            arr[i],arr[i-1]=arr[i-1],arr[i]
            i=i-1
    return arr

bucketSort(x,len(x))