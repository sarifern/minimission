#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    pass

if __name__ == '__main__':
    candles_count = int(input("Enter the kid's age:").strip())
    candles = list(map(int, input("Enter the candles height:").rstrip().split()))
    result = birthdayCakeCandles(candles)