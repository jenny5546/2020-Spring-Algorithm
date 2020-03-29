"""
문병로 교수님 알고리즘 4강. 정렬
선택정렬을 파이썬으로 짜서 연습해보자!
"""

array = [0,5,31,3,4,2,1]

def sort(arr, n):

    for i in range(n-1,-1,-1): # n-1부터 0 까지 downcount 
        max = arr[i]
        max_pos = i
        for j in range(i): # 0 부터 i-1까지
            if max < arr[j]:
                max = arr[j]
                max_pos = j
        arr[max_pos],arr[i]= arr[i],arr[max_pos]  
           
    print(arr)

sort(array,len(array))

                
        

