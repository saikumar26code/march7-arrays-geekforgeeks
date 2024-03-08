#Count number of occurrences (or frequency) in a sorted array

#using linear search

def occurance(arr,n,x):
    res=0 #counting the number of occurances
    for i in arr:
        if i==x:#comparing the every element in the array with the x
            res+=1
    return res
arr=[int(x) for x in input().split()]
n=len(arr)
x=int(input())
print(occurance(arr,n,x))

#time complexity O(n)
#space complexity O(1)