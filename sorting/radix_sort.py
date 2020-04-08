"""
문병로 교수님 알고리즘 4강. 정렬
Radix 정렬을 파이썬으로 짜서 연습해보자!

"""
arr= [123,456,232,121,878,456,123,666,555,323,879]

def stableSort(arr, n): #insertion sort
    for i in range(1,n): # 1부터 n-1까지
        while i!=0 and arr[i]<arr[i-1] :
            arr[i],arr[i-1]=arr[i-1],arr[i]
            i=i-1

def radixSort(arr,d):
    save = arr
    for j in range(d,-1,-1):
        temp = [x%10 for x in arr]




radixSort(arr,3)
print(arr)