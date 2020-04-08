"""
문병로 교수님 알고리즘 4강. 정렬
Counting 정렬을 파이썬으로 짜서 연습해보자!

"""

array= [1,2,1,3,6,5,4,7,9,8]


def simpleCountingSort(arr, n):

    c = [0] * 10

    for j in range(n):
        c[arr[j]]+=1

    for idx in range(10):
        for i in range(c[idx]):
            print(idx, end='  ')
    print()

simpleCountingSort(array,10)

def fullCountingSort(arr,n):

    c = [0] * 10
    b = [0] * n
    for i in range(n):
        c[arr[i]]+=1   #array= [1,2,1,3,6,5,4,7,9,8]
                        # c[0]=0 c[1]=2, c[2]=1 ...c[9]=1
    
    #######여기까지 동일#######
    for i in range(1,10,1):
        c[i]= c[i]+c[i-1]  #c[0]=0, c[1]=2, c[2]=3 c[3]=4
    # 이 지점에서 c[r]: 값이 r 이하인 원소의 총수  

    for i in range(n-1,-1,-1):
        print(i)
        b[c[arr[i]]-1] = arr[i] #index -1 해주기 주의
        c[arr[i]]-=1

    return b

print(fullCountingSort(array,10))