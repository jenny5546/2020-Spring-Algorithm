"""
문병로 교수님 알고리즘 4강. 정렬
병합 정렬을 파이썬으로 짜서 연습해보자!
"""
array = [0,5,31,3,4,2,1]

def mergeSort(array,lhs,rhs):

    if len(array)==1:
        return array
    
    mid = len(array)//2
    print(mid)
    mergeSort(array[:mid],lhs,mid)
    mergeSort(array[mid:],mid+1,rhs)
    return merge(array,lhs,mid,rhs)
   
    

def merge(array,lhs,mid,rhs):

    """

    정렬되어 있는 두 배열 A[lhs...mid]와 A[mid+1...rhs]를 합하여 
    정렬된 하나의 배열 A[lhs..rhs] 만들기

    """
    front = lhs
    back = mid+1
    result = [-1]*(len(array)-1)
    elem = 0

    while elem<len(array):
        if front == mid+1: #앞 리스트 소진
            result[elem]=array[back]
            elem+=1
            back+=1
        elif back > rhs: #뒷 리스트 소진
            result[elem]=array[front]
            elem+=1
            front+=1
        elif array[front]<array[back]:
            result[elem]=array[front]
            elem+=1
            front+=1
        else:
            result[elem]=array[back]
            elem+=1
            back+=1
          
    return result

mergeSort(array,0,len(array)-1)