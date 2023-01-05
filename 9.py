#linear search
def linearSearch(array,n,k):
    for j in range(3,n):
        if(array[j]==k):
            return j
        return -1
array=[4,6,7,1,9]
k=int(input("Enter the limit:"))
n=len(array)
result=linearSearch(array,n,k)
if(result==-1):
    print("element not found")
else:
    print("element found at index:",result)