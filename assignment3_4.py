def mergesort(sorted_list, value):
    merged_list = []
    
   
    start = 0
    end = len(sorted_list) - 1

    while start < end and sorted_list[start] < value:
        merged_list.append(sorted_list[start])
        start = start + 1
        
  
    merged_list.append(value)
    
    while start < end:
        merged_list.append(sorted_list[start])
        start = start + 1
    
    return merged_list


list1 = [1, 34, 56, 78, 89]
val = 100
print(mergesort(list1, val)) 
  
