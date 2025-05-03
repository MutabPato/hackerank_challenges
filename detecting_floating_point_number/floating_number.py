# Enter your code here. Read input from STDIN. Print output to STDOUT
#! /usr/bin/env python3

import sys
import re

input = []

for line in sys.stdin:
    input.append(line.rstrip())

test_cases = input[1:]

for case in test_cases:
    match = re.findall("[+-]?[0-9]*\.[0-9]+", case)
    if case in match:
        print(True)
    else:
        print(False)