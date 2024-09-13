def sum67(nums):
  seen6 = False
  sum = 0
  for i in nums:
    if(i == 6):
      seen6 = True
    if(not seen6):
      sum += i
    elif(i == 7):
      seen6 = False
  return sum

