#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    characters = list(s)
    character_count = Counter(characters)
    count_list = list(character_count.most_common())
    sorted_count_list = sorted(count_list, key=lambda x: (-x[1], x[0]))
    iterations = 0
    for a, b in sorted_count_list:
        print(a, b)
        if iterations >= 2:
            break
        iterations +=1