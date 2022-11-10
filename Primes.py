

primes = []
for number in range(2,1000):
  factors = []
  for prime in primes:
    if number % prime == 0:
      factors.append(prime)
  if not factors:
    primes.append(number)
print(primes)