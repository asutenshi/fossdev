def sum(a, b):
  if not (isinstance(a, int) or isinstance(b, int)):
    raise ValueError("Summing could be with integers")
  return a + b

def devide(a, b):
  if b == 0:
    raise ValueError("Denominator could not be zero")
  return a / b