A= [1,-2,1,3,-6,5,4,7,9,8]
B= [0]*10

def countingSort(A,B,n):
    c = [0] * 2 * n
    min = -1 * n
    for j in range(n):
        c[A[j]-min]+=1
    for i in range(1,2*n):
        c[i] = c[i]+c[i-1]
    
    for j in range(n-1, -1, -1):
        B[c[A[j]-min]-1] = A[j]
        c[A[j]-min]-=1
    
    print(B)




countingSort(A,B,10)