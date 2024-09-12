def array_front9(nums):
  for i in range(min(len(nums), 3)):
    if(nums[i] == 9):
      return True
  return False

