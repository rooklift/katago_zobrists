Files:

* `katago_ko_memdump.txt` - The RAM state of KataGo for its ko zobrist hash array, starting at the top left (A19) hash and ending at the bottom right (T1) hash.
* `zobrist_ko.py` - script to print out usable values from the above.
* `zobrist_stones.py` - script to determine B and W stone zobrist hash values via analysis engine queries.

Notes:

* KataGo's hash arrays are initialised by `Board::initHash()` in [board.cpp](https://github.com/lightvector/KataGo/blob/master/cpp/game/board.cpp).
* `thisHash` is (ultimately) generated by `getSitHashWithSimpleKo()` in the same file.