# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(l, h):
  #write your code here
  mid = (l + h)//2
  left = l
  pivot = arr[mid]
  arr[h], arr[mid] = arr[mid], arr[h]
  for i in range(l,h):
    if arr[i] < pivot:
      arr[left], arr[i] = arr[i], arr[left]
      left += 1
  arr[left], arr[h] = arr[h], arr[left]
  return left


def quickSortIterative( l, h):
  #write your code here
  stack = [(l, h)]

  while stack:
    cur_low, cur_high = stack.pop()
    item = partition(cur_low, cur_high)

    if item>cur_low:
      stack.append((cur_low,item-1))
    
    if item < cur_high:
      stack.append((item+1, cur_high))
    
arr = [10, 80, 30, 90, 40, 50, 70]

print("before: ", arr)
quickSortIterative(0, len(arr)-1)
print("after: ", arr)

