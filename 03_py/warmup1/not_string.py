def not_string(str):
  if len(str) >= 3:
    if(str[:3] != "not"):
      return "not " + str
    else:
      return str
  return "not " + str

