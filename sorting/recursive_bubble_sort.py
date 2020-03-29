"""
문병로 교수님 알고리즘 4강. 정렬
버블정렬을 파이썬으로 짜서 연습해보자!(recursive.ver)
"""

array = [0,5,31,3,4,2,1]

def sort(arr, n):
    # 기저사례
    if n==1:
        return -1
    else:
        for i in range(n-1):
            if arr[i]>arr[i+1]:
                arr[i], arr[i+1]= arr[i+1], arr[i]
            sort(arr,n-1)

sort(array,len(array))
print(array)