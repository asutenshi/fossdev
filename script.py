def sum(a, b):
    if not (isinstance(a, int) or isinstance(b, int)):
        raise ValueError("Summing could be with integers")
    return a + b


def devide(a, b):
    if b == 0:
      raise ValueError("Denominator could not be zero")
    if isinstance(a, str) or isinstance(b, str):
      raise ValueError("Args could not be strings")
    if isinstance(a, list) or isinstance(b, list):
      raise ValueError("Could not devide lists")
    return a / b