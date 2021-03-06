Files:

* `katago_board_421_memdump.txt` - KataGo's zobrist array for stones.
* `katago_ko_421_memdump.txt` - KataGo's zobrist array for ko locations.
* `20_mystery_values.txt` - these turned out to be the width array.
* `24_mystery_values.txt` - these turned out to be the height array and the player array (4 players).

Scripts:

* `raw_print.py` - just prints usable values from any dump file.
* `zobrist_board_421.py` - prints usable stone values.
* `zobrist_ko_421.py` - prints usable ko values.

Notes:

* KataGo's hash arrays are initialised by `Board::initHash()` in [board.cpp](https://github.com/lightvector/KataGo/blob/master/cpp/game/board.cpp).
* `thisHash` is (ultimately) generated by `getSitHashWithSimpleKo()` in the same file.
* KataGo's zobrist arrays are length 421 due to padding.
* The correct index for (x, y) is `x + 1 + ((y + 1) * (width + 1))` - see `Location::getLoc()`.
* The stones array is laid out as a blank, followed by a Black value, followed by a White value, followed by a blank.
