"""
문병로 교수님 알고리즘 4강. 정렬
삽입정렬을 파이썬으로 짜서 연습해보자!
"""

array = [0,5,31,3,4,2,1]

def sort(arr, n):

    for i in range(1,n): # 1부터 n-1까지

        while i!=0 and arr[i]<arr[i-1] :
            arr[i],arr[i-1]=arr[i-1],arr[i]
            i=i-1
           
    print(arr)

sort(array,len(array))

                
        

