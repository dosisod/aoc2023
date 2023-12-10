from collections import defaultdict
from pathlib import Path

data = Path(__file__).with_suffix(".txt").read_text()

chunks = []
inside_chunk = False
symbols = []

for row, line in enumerate(data.splitlines()):
    for col, c in enumerate(line):
        if c.isdigit():
            if not inside_chunk:
                chunks.append([row, [col, col], c])
                inside_chunk = True

            else:
                chunks[-1][1][1] = col
                chunks[-1][2] += c

        elif c == ".":
            inside_chunk = False

        else:
            inside_chunk = False
            symbols.append((row, col, c))

total = 0

gear_ratios = defaultdict(list)

for row, [col_start, col_end], product_code in chunks:
    for sym_row, sym_col, sym in symbols:
        if (
            ((row - 1) <= sym_row <= (row + 1)) and
            ((col_start - 1) <= sym_col <= (col_end + 1))
        ):
            total += int(product_code)

            if sym == "*":
                gear_ratios[(sym_row, sym_col)].append(product_code)

            break

print(total)

total = 0

for ratios in gear_ratios.values():
    if len(ratios) != 2:
        continue

    total += int(ratios[0]) * int(ratios[1])

print(total)
