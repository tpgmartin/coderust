def move_zeros_to_left(arr):
  read_index = write_index = len(arr)-1

  while (write_index > -1):
    if (read_index > -1):
      read_value = arr[read_index]
      if(read_value != 0):
        arr[write_index] = read_value
        write_index -= 1
    else:
      arr[write_index] = 0
      write_index -= 1
    read_index -= 1
  
  return arr
