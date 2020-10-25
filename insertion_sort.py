'''
input: [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
goal: sort the array in ascending order
algorithm: insertion sort
description:
  assume that the array left of the anchor is already sorted
  set the anchor to the front of the array
  move the anchor to the right and check the number
  go through the array left of the anchor and find the right place and insert
process:
  for all indices,
    1. go through the left array
    2. swap if the number to the left is larger
    3. repeat until no swap is needed
time complexity:
  O(n^2)
'''
input_arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

for i in range(len(input_arr) - 1):
  # anchor is at i
  j = i

  while input_arr[j] > input_arr[j + 1]:
    temp = input_arr[j]
    input_arr[j] = input_arr[j + 1]
    input_arr[j + 1] = temp
    j -= 1

print(input_arr)

  
