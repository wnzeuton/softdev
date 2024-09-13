def sum13(nums):
  sum = 0
  seen13 = False
  for i in nums:
    if(i != 13 and not seen13):
      sum += i
    else:
      seen13 = True
    if(seen13 and i != 13):
      seen13 = False
  return sum

