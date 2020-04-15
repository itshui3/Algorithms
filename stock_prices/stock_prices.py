#!/usr/bin/python

import argparse

def find_max_profit(prices):
    max = 0
    min = prices[0]

    for i in prices:

        if((i - min) > (max - min)):
            max = i - min

        if(i < min):
            min = i

    return max

import random
myNums = []
for i in range(0, 10):
    myNums.append(random.randint(0, 20))

print(find_max_profit(myNums))


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))