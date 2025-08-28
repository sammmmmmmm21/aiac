#code-1
with open("example.txt", "w") as f:
    f.write("Hello, world!")
#code-2
with open("data1.txt", "w") as f1, open("data2.txt", "w") as f2:
    f1.write("First file content\n")
    f2.write("Second file content\n")

print("Files written successfully")
#code-3
with open("input.txt", "r") as data, open("output.txt", "w") as output:
    for line in data:
        output.write(line.upper())

print("Processing done")
#code-4
squares = []

with open("numbers.txt", "r") as f:
    nums = f.readlines()

for n in nums:
    n = n.strip()
    if n.isdigit():
        squares.append(int(n) * int(n))

with open("squares.txt", "w") as f2:
    for sq in squares:
        f2.write(str(sq) + "\n")

print("Squares written")
