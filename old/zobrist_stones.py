import json, subprocess

WIDTH = 19
HEIGHT = 19

# -------------------------------------------------------------------------------------------------
# Dealing with the KataGo process...

exe_path = "C:\\Programs (self-installed)\\KataGo 1.11.0 OpenCL\\katago.exe"

args = [
	"analysis",
	"-config",
	"C:\\Programs (self-installed)\\KataGo 1.11.0 OpenCL\\analysis_example.cfg",
	"-model",
	"C:\\Users\\Owner\\Documents\\Misc\\KataGo\\kata1-b40c256-s11101799168-d2715431527.bin.gz",
	"-quit-without-waiting"]

p = subprocess.Popen(
	[exe_path] + args,
	stdin = subprocess.PIPE,
	stdout = subprocess.PIPE,
	stderr = subprocess.DEVNULL)

def send(o):
	s = json.dumps(o) + "\n"
	p.stdin.write(s.encode("utf8"))
	p.stdin.flush()

next_id = 0

def next_id_string():
	global next_id
	next_id += 1
	return "query_{}".format(next_id)

def send_query(stones, player):

	assert(type(stones) is list)
	assert(player in ["B", "W"])
	
	d = {
		"id": next_id_string(),
		"moves": [],
		"rules": "Chinese",
		"komi": 7.5,
		"boardXSize": WIDTH,
		"boardYSize": HEIGHT,
		"initialStones": stones,
		"initialPlayer": player,
		"maxVisits": 1,
	}

	send(d)

def receive_and_extract_hash():
	kata_output = p.stdout.readline().decode("utf8")
	d = json.loads(kata_output)
	return int(d["rootInfo"]["thisHash"], base=16)

# -------------------------------------------------------------------------------------------------
# Utility...

def xy_to_gtp(x, y):
	x_ascii = x + 65
	if x_ascii >= ord("I"):
		x_ascii += 1
	y = HEIGHT - y
	return chr(x_ascii) + str(y)

def nice_hex(i):
	s = hex(i)[2:]			# remove the 0x
	while len(s) < 32:
		s = "0" + s
	return "0x" + s + "n"	# restore the 0x, add JS bigint marker

# -------------------------------------------------------------------------------------------------

send_query([], "B")
empty_b_to_play = receive_and_extract_hash()

send_query([], "W")
empty_w_to_play = receive_and_extract_hash()

for stone_colour in ["B", "W"]:

	print()
	print("{} STONES...".format(stone_colour))

	done = 0

	for y in range(HEIGHT):
		for x in range(WIDTH):
			stones = [[stone_colour, xy_to_gtp(x, y)]]
			send_query(stones, "B")								# Always Black to play...
			h = receive_and_extract_hash() ^ empty_b_to_play	# XOR against the empty position to get what difference this stone made.
			print(nice_hex(h) + ", ", end="")
			done += 1
			if (done % 3 == 0):
				print()


print()
print("B TO PLAY, {}x{}".format(WIDTH, HEIGHT))
print(nice_hex(empty_b_to_play))

print("W TO PLAY, {}x{}".format(WIDTH, HEIGHT))
print(nice_hex(empty_w_to_play))
