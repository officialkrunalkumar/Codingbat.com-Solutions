'''
Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.


max_end3([1, 2, 3]) → [3, 3, 3]
max_end3([11, 5, 9]) → [11, 11, 11]
max_end3([2, 11, 3]) → [3, 3, 3]
'''
def max_end3(nums):
  maxi = max(nums[0], nums[len(nums)-1])
  amaxi = []
  for i in range(0, len(nums)):
    amaxi.append(maxi)
  return amaxi
