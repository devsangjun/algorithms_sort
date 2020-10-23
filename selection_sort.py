'''
input: [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
goal: sort the array in ascending order
algorithm: selection sort
description:
  moving the smallest number to the front
process:
  1. set the anchor to the first index
  2. go through the array
  3. find the smallest
  4. swap(num at the anchor, smallest)
  5. move the anchor to the right
'''
input_arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

for i in range(len(input_arr)):
  anchor = i
  smallest = input_arr[anchor]
  for j in range(anchor, len(input_arr)):
    if input_arr[j] < smallest:
      smallest = input_arr[j]
      input_arr[j] = input_arr[anchor]
      input_arr[anchor] = smallest
  anchor += 1
print(input_arr)