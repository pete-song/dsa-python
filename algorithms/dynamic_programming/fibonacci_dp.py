# Memoized Approach
def fib_dp_memoized(n, mem=None):
  if mem is None:
    mem={}
  if n in mem:
    return mem[n]
  elif n == 0:
    return 0
  elif n == 1:
    return 1

  result = fib_dp_memoized(n-1, mem) + fib_dp_memoized(n-2, mem)
  mem[n] = result
  return result


# Bottom Up Approach
def fib_dp_bottom_up(n):
  if n <= 2:  # Base cases are already in fibnums, no need for 0 and 1
    return 1

  fibnums = [0,1,1]

  for i in range(3, n+1):
    fibnums.append(fibnums[i-1] + fibnums[i-2])

  return fibnums[n]

def test():
  # Memoized Approach
  print(fib_dp_memoized(5))
  print(fib_dp_memoized(6))
  print(fib_dp_memoized(7))

  # Bottom Up Approach
  print(fib_dp_bottom_up(5))
  print(fib_dp_bottom_up(6))
  print(fib_dp_bottom_up(7))

if __name__ == "__main__":
  test()
