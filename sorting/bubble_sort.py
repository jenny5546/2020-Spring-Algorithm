"""
문병로 교수님 알고리즘 4강. 정렬
버블정렬을 파이썬으로 짜서 연습해보자!
"""

array = [0,5,31,3,4,2,1]

def sort(arr, n):
    for end in range(n-1,-1,-1): # n-1부터 0 까지 downcount 
        for i in range(end):
            if arr[i]>arr[i+1]:
                arr[i], arr[i+1]= arr[i+1], arr[i]
    print(arr)

sort(array,len(array))