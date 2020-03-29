"""
문병로 교수님 알고리즘 4강. 정렬
선택정렬을 파이썬으로 짜서 연습해보자!(recursive.ver)
"""

array = [0,5,31,3,4,2,1]


def sort(arr,n):
    # 기저사례
    if n==1:
        return -1
    else:
        max = arr[n-1]
        max_pos = n-1

        for i in range(n-1): # n-1부터 0 까지 downcount 
            if max<arr[i]:
                max_pos = i
                max = arr[i]  

        arr[max_pos],arr[n-1]= arr[n-1],arr[max_pos]
        sort(arr,n-1)
        
sort(array,len(array))
print(array)
