def centered_average(nums):
  size = len(nums)
  sum = 0
  for i in nums:
    sum += i
  sum -= max(nums)
  sum -= min(nums)
  
  return sum / (size - 2)
  

