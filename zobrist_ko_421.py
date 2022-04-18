with open("katago_ko_421_memdump.txt") as infile:
	raw = infile.read()

tokens = raw.split(" ")


print("BASIC KO...")
printouts = 0
for i in range(421):
	b = tokens[i * 16 : i * 16 + 16]
	b.reverse()									# dump is little-endian
	print("0x" + "".join(b).lower() + "n, ", end="\n" if printouts % 3 == 2 else "")
	printouts += 1

