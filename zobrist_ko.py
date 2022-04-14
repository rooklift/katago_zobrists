# This extracts the ko zobrists from the relevant memory dump.

# Note that there seems to be some padding for some reason, i.e. the dump has 379 hashes.
# So we ignore positions 19, 38, etc, etc...

with open("katago_ko_memdump.txt") as infile:
	raw = infile.read()

tokens = raw.split(" ")

printouts = 0

for i in range(379):

	b = tokens[i * 16 : i * 16 + 16]
	b.reverse()								# dump is little-endian

	if i % 20 != 19:
		print("0x" + "".join(b) + "n,", end="")
		printouts += 1
		if printouts % 3 == 0:
			print()

