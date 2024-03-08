def occurance(arr,k):
    m={}
    for i in arr:
        if i in m:
            m[i]+=1
        else:
            m[i]=1
    if k not in m:
        return 0
    return m[i]
arr=[int(x) for x in input().split()]
k=int(input())
print(occurance(arr,k))