#!/usr/bin/python

# ID: FIB
# TITLE: Rabbits and Recurrency Relations

def fibonacci(n, k):
  if n == 1:
    return 1
  if n < 1:
    return 0
  else:
    return ((fibonacci(n - 2, k) * k) + fibonacci(n - 1, k))

print fibonacci(29, 5)
