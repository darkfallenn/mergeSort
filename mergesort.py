# Divides the array into halves, until it reaches sequences of one (ex. [6] and [5])

def mergeSort(arr):
  mid = len(arr) // 2 
  
  if len(arr) < 2:
    return arr

  left = arr[:mid]
  right = arr[mid:]

  return merge(mergeSort(left), mergeSort(right))

# Sorts and conquers both halves.

def merge(left, right):
  arr = []

  while left and right:
    if left[0] < right[0]:
      arr.append(left.pop(0))
    else:
      arr.append(right.pop(0))

  return [*arr, *left, *right]

# Total time complexity: O(nLogn)
