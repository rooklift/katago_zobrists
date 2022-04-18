with open("katago_board_421_memdump.txt") as infile:
	raw = infile.read()

tokens = raw.split(" ")


print("BLACK STONES...")
printouts = 0
for i in range(421):
	b = tokens[i * 64 + 16 : i * 64 + 32]
	b.reverse()									# dump is little-endian
	print("0x" + "".join(b).lower() + "n, ", end="\n" if printouts % 3 == 2 else "")
	printouts += 1


print("\n\nWHITE STONES...")
printouts = 0
for i in range(421):
	b = tokens[i * 64 + 32 : i * 64 + 48]
	b.reverse()
	print("0x" + "".join(b).lower() + "n, ", end="\n" if printouts % 3 == 2 else "")
	printouts += 1
