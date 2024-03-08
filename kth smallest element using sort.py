#K’th Smallest/Largest Element in Unsorted Array

#using sorting method


#Observe the time complexity and space complexity


def smallestele(arr,n,k):#for finding the smallest element
    arr.sort() #sort method takes time complexity of O(nlog n)
    return arr[k-1]
def largestele(arr,n,k):#for finding the largest element
    arr.sort()
    return arr[n-k]
arr=[x for x in map(int,input().split())]
n=len(arr)
k=int(input("enter the kth element to find the kth smallest and kth largest element"))
print(smallestele(arr,n,k),largestele(arr,n,k))

#time complexity O(nlog n)
#space complexity O(1)




# in this i missed 3-4 another different methods to solve