def front3(str):
  if(len(str) < 3):
    front = str
  else:
    front = str[:3]
  return front + front + front

