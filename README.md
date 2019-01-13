# CSE_Fest_AI_Contest

All read write operations are done in player_x.py. Contestants may not need to change those codes. They can only modify the select_move(grid) function.

The grid is al 8*8 2d list. Each entry describe the cube in that position. Entry of "No" indicates empty cube. Otherwise the first letter of the entry describes color of the atom(s) in the cube ('R'/'G') the second letter describes number of the atoms. So if a cube has three red atoms it will be described as 'R3'.

The contestants may write hueristics or methods of their choice in the select_move function. The function will return the x, y values of the cube they want to make the next move in. 


