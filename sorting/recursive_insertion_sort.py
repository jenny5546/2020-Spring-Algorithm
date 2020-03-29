"""
문병로 교수님 알고리즘 4강. 정렬
삽입정렬을 파이썬으로 짜서 연습해보자!(recursive.ver)
"""

array = [0,5,31,3,4,2,1]

# Version 1, index를 parameter로 주기 

def sort1(arr, i, n):
    # 기저사례
    if i==n:
        return -1
    else:  
        while i!=0 and arr[i]<arr[i-1] :
            arr[i],arr[i-1]=arr[i-1],arr[i]
            i=i-1
        sort1(arr,i+1,n)
           

sort1(array,1,len(array))
print(array)

# Version 2, arr와 n만 parameter로 받기
def sort2(arr,n):
    if n==1:
        return -1
    else:
        i = len(arr)-(n-1)
        while i!=0 and arr[i]<arr[i-1] :
            arr[i],arr[i-1]=arr[i-1],arr[i]
            i=i-1
        sort2(arr,n-1)

sort2(array,len(array))
print(array)

                
        

