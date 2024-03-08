def occurance(arr,k):
    d={}
    for i in arr:
        d[i]=d.get(i,0)+1
    if k not in d:
        return 0
    return d[k]
arr=[int(x) for x in input().split()]
k=int(input())
print(occurance(arr,k))