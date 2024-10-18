list1 = [1,2,7,9,15]

def binarySearch(list1,key,start,end):
    mid = (start + end)//2


    if start > end:
        return -1

    mid = (start + end) // 2

    if list1[mid] == key:
            
            return mid
    
    elif list1[mid]< key:
        return binarySearch(list1,key, mid + 1,end)
    else:
        return binarySearch(list1,key,start, mid - 1)
       
list2 = [0,1,2,7,9,15]
key = 0
start = 0
end = len(list1) - 1

    

    
result = binarySearch(list2,key,start,end)

if result == -1:
    print("not found")
else:
    print("found")