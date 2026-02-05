def sum(a, b):
  return a + b

def devide(a, b):
  if b == 0:
    raise ValueError("Denominator could not be zero")
  return a / b