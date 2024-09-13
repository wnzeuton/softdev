def last2(str):
  count = 0
  last = str[len(str) - 2: len(str)]
  for i in range(len(str)):
    if(str[i:i+2] == last):
      count += 1
    i += 1
  return max(count - 1, 0)

