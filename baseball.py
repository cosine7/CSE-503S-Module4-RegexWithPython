import os
import sys
import re

if len(sys.argv) < 2:
    sys.exit(f"Usage: {sys.argv[0]} filename")

filename = sys.argv[1]

if not os.path.exists(filename):
    sys.exit(f"Error: File '{sys.argv[1]}' not found")

record_regex = re.compile(r"([A-z]+ [A-z]+) batted ([0-9]+) times with ([0-9]+) hits and [0-9]+ runs")
records = dict()

with open(filename) as f:
    for line in f:
        match = record_regex.match(line)
        if match is None:
            continue
        name = match.group(1)
        at_bat = int(match.group(2))
        hit = int(match.group(3))
        if name in records:
            records[name][0] += at_bat
            records[name][1] += hit
        else:
            records[name] = [at_bat, hit]

for name, values in records.items():
    records[name] = values[1] / values[0]

for record in sorted(records.items(), key=lambda x: x[1], reverse=True):
    num = "{:.3f}".format(float(record[1]))
    print(f"{record[0]}: {num}")
