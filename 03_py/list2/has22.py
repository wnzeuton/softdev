def has22(nums):
  seen2 = False
  for i in nums:
    if(seen2 and i == 2):
      return True
    if(i == 2):
      seen2 = True
    else:
      seen2 = False
  return False

