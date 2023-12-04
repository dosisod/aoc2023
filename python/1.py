from pathlib import Path

data = Path(__file__).with_suffix(".txt").read_text()

total = 0

for line in data.splitlines():
    nums = [c for c in line if c.isnumeric()]

    total += int(nums[0] + nums[-1])

print(total)

total = 0

for line in data.splitlines():
    # Replace spelled out version of numbers with their numeric versions. The
    # rules weren't very clear as to how you should handle words that overlap,
    # and this was the only way I could get it to work. Basically, if you have
    # a string like "oneight", it would get replaced with "o1eight", then with
    # "o1e8t". Since characters are ignored later and only the numbers matter,
    # the extra characters don't matter. Numbers like four and six don't start
    # or end with any of the same letters as the other numbers, so it is safe
    # to replace them without adding the start/end.
    line = (
        line.replace("one", "o1e")
            .replace("two", "t2o")
            .replace("three", "t3e")
            .replace("four", "4")
            .replace("five", "5e")
            .replace("six", "6")
            .replace("seven", "7n")
            .replace("eight", "e8t")
            .replace("nine", "n9e")
    )

    nums = [c for c in line if c.isnumeric()]

    total += int(nums[0] + nums[-1])

print(total)
