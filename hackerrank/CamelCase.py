def camelcase(s):
    nb=1
    for c in  s:
      if c.isupper():
        nb +=1
    return nb
    