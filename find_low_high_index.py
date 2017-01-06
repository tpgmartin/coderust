def find_low_index(arr, key):
  low = 0
  high = len(arr)-1
  mid = high/2
  
  
  while (low <= high):
    mid_el = arr[mid]
    if (mid_el < key):
      low = mid+1
    elif (mid_el >= key):
      high = mid-1
    mid = (low+high)/2
  
  if (arr[low] == key):
    return low
  else:
    return -1

def find_high_index(arr, key):
  low = 0
  high = len(arr)-1
  mid = high/2
  
  
  while (low <= high):
    mid_el = arr[mid]
    if (mid_el <= key):
      low = mid+1
    elif (mid_el > key):
      high = mid-1
    mid = (low+high)/2
  
  if (arr[high] == key):
    return high
  else:
    return -1
