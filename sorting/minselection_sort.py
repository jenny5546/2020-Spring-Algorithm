"""
문병로 교수님 알고리즘 4강. 정렬
선택정렬을 파이썬으로 짜서 연습해보자! (min ver.)
"""

array = [0,5,31,3,4,2,1]

def sort(arr, n):

    for i in range(1,n): # 1부터 N-1까지 
        min = arr[i]
        min_pos = i
        for j in range(i,n): # 0 부터 i-1까지
            if min > arr[j]:
                min = arr[j]
                min_pos = j
        arr[min_pos],arr[i]= arr[i],arr[min_pos]  
           
    print(arr)

sort(array,len(array))

                
        

