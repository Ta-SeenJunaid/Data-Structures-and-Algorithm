

def lis(arr):
    
    n=len(arr)
    
    lis=[1]*n
    
    for i in range(1,n):
        for j in range(0,i):
            if arr[i]>arr[j] and lis[i]<lis[j]+1:
                lis[i]=lis[j]+1
                
    maximum = 0
    
    for i in range(n):
        maximum=max(maximum,lis[i])
        
    return maximum




arr=[]
n=int(input("Enter size of the list:\n"))
     
for i in range(0,n):
    print("Enter "+str(i)+"th number to append: ")
    temp=int(input())
    arr.append(temp)
        


print("the length of lis is ",lis(arr))
