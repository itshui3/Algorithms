#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
    if(n < 2):
        return 1
    threes = n // 3
    permutations = 0
    for i in range(0, threes + 1):
        permutations += 1
        permutations += ((n - (i * 3)) // 2)

    return permutations


print(eating_cookies(3))
if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')