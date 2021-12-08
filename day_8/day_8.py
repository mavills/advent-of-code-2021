with open("input.txt", "r") as file:
    lines = file.readlines()

print("Day 8")
print("Part 1")

processed = []
for line in lines:
    p = line.replace(" | ", " ")
    processed.append(p.strip())

codes = []
for line in processed:
    words = line.split(" ")
    words = ["".join(sorted(word)) for word in words]
    codes.append(words)

_1478 = 0
for code in codes:
    for digit in code[-4:]:
        if len(digit) in [2, 3, 4, 7]:
            _1478 += 1

print("number of 1's, 4's, 7's and 8's (answer):", _1478)  # 452

print("")
print("Part 2")

numbers = []

for code in codes:
    decoded = []
    one = [d for d in code if len(d) == 2][0]
    four = [d for d in code if len(d) == 4][0]
    seven = [d for d in code if len(d) == 3][0]
    eight = [d for d in code if len(d) == 7][0]
    b_one = sum([2 ** (ord(d) - ord('a')) for d in list(one)])
    b_four = sum([2 ** (ord(d) - ord('a')) for d in list(four)])
    b_seven = sum([2 ** (ord(d) - ord('a')) for d in list(seven)])
    b_eight = sum([2 ** (ord(d) - ord('a')) for d in list(eight)])
    for i, digit in enumerate(code[:10]):
        binary = sum([2 ** (ord(d) - ord('a')) for d in list(digit)])
        if len(digit) == 2:
            decoded.append(1)
            continue
        if len(digit) == 3:
            decoded.append(7)
            continue
        if len(digit) == 7:
            decoded.append(8)
            continue
        if len(digit) == 4:
            decoded.append(4)
            continue
        if b_four & binary == b_four:
            decoded.append(9)
            continue
        if len(digit) == 6 and (b_one & binary) == b_one:
            decoded.append(0)
            continue
        if len(digit) == 6 and (b_one & binary) != b_one:
            decoded.append(6)
            continue
        if len(digit) == 5 and (b_one & binary) == b_one:
            decoded.append(3)
            continue
        if len(digit) == 5 and bin(b_four & binary).count("1") == 3:
            decoded.append(5)
            continue
        if len(digit) == 5 and bin(b_four & binary).count("1") == 2:
            decoded.append(2)
            continue
        print("Something went wrong!")
    decoded = {code[i]: decoded[i] for i in range(10)}
    numbers.append(1000 * decoded[code[10]] + 100 * decoded[code[11]]
                   + 10 * decoded[code[12]] + decoded[code[13]])

print("Sum of all displays (answer):", sum(numbers))
