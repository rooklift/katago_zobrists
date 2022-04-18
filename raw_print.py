import sys

with open(sys.argv[1]) as infile:
	raw = infile.read()

tokens = raw.split(" ")

for i in range(len(tokens) // 16):
	b = tokens[i * 16 : i * 16 + 16]
	b.reverse()									# dump is little-endian
	print("0x" + "".join(b).lower() + "n")
