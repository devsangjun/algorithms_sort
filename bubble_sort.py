'''
input: [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
goal: sort the array in ascending order
algorithm: bubble sort
description:
  compare with the number to the right and 
  send the smaller number to the front
process:
  1. bubble sort from the first index to the anchor
  2. move the anchor to the left
time complexity:
  total operations: n * (n + 1) / 2
  slowest sorting algorithm (too many swaps)
  O(n^2)
'''
input_arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

for i in range(len(input_arr) - 1, 0, -1):
  anchor = i
  for j in range(anchor):
    num_1 = input_arr[j]
    num_2 = input_arr[j + 1]
    if num_2 < num_1:
      input_arr[j] = num_2
      input_arr[j + 1] = num_1

print(input_arr)