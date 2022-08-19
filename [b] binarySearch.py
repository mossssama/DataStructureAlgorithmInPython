def binarySearch(arr,val):
    start=0;    end=len(arr); 
    while start<=end:
        mid=(start+end)//2;
        if val>arr[mid]:
            start=mid+1;
        elif  val<arr[mid]:
            end=mid-1;
        else:
            return mid
    return -1


sortedArr=[2,4,6,8,10,12,14]
print(sortedArr)
print(binarySearch(sortedArr,10))



