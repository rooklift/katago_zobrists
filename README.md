Files:

* `katago_board_421_memdump.txt` - memdump of KataGo's zobrist array for stones.
* `katago_ko_421_memdump.txt` - memdump of KataGo's zobrist array for ko locations.
* `zobrist_board_421.py` - prints usable stone values.
* `zobrist_ko_421.py` - prints usable ko values.

Notes:

* KataGo's zobrist arrays are length 421 due to padding.
* The correct index for (x, y) is `x + 1 + ((y + 1) * (width + 1))` - see Location::getLoc().
* The stones array is laid out as 16 zeroes, followed by a Black value, followed by a White value, followed by 16 zeroes.
