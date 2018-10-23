import sys # print("Debug messages...", file=sys.stderr)
import math

root = {}
count = 0

n = int(input())

for _ in range(n):
    print("root", root, file=sys.stderr)
    current = root
    phone_number = input()
    for number in phone_number:
        if number not in current:
            current[number] = {}
            count += 1
            print("current", current, file=sys.stderr)
            print("root", root, file=sys.stderr)
        current = current[number]
            
print(count)
