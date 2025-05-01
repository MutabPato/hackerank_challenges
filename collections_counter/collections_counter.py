# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from collections import Counter

input = []
for line in sys.stdin:
    input.append(line.rstrip())
number_of_shoes = input[0]
sizes = input[1].split(" ")
size_counter = Counter(sizes)
number_of_customers = input[2]
orders = []
for elem in input[3:]:
    order = elem.split()
    orders.append({order[0]: int(order[1])})

earnings = 0

for order in orders:
    size = list(order.keys())[0]
    price = list(order.values())[0]
    if size_counter[size] >= 1:
        earnings += price
        size_counter[size] -= 1
print(earnings)