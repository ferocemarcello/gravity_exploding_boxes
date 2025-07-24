# gravity_exploding_boxes

You are running a gravity simulation involving falling boxes and exploding obstacles. The scenario is represented by a rectangular matrix of characters board. Each cell of the matrix board contains one of three characters: '-', which means that the cell is empty; '', which means that the cell contains an obstacle; '#', which means that the cell contains a box. The boxes all fall down simultaneously as far as possible, until they hit an obstacle, another grounded box, or the bottom of the board. If a box hits an obstacle, the box explodes, destroying itself and any other boxes within eight cells surrounding the obstacle. The obstacle stays at its place. it does not get destroyed. All the explosions happen simultaneously as well. Given board, your task is to return the state of the board after all boxes have fallen.

Example:

board = [

['#', '-', '#', '#', ''],

['#', '-', '-', '#', '#'],

['-', '#', '-', '#', '-'],

['-', '-', '#', '-', '#'],

['#', '', '-', '-', '-'],

['-', '-', '', '#', '-']

]

solution(board) =

[

['-', '-', '-', '-', ''],

['-', '-', '-', '-', '-'],

['-', '-', '-', '-', '-'],

['-', '-', '-', '-', '-'],

['-', '', '-', '-', '#'],

['#', '-', '*', '-', '#']

]

I also have for you a step by step matrix. I mean all the states that the matrix has, from 0(input), to 5(solution):

0:

[

['#', '-', '#', '#', ''],

['#', '-', '-', '#', '#'],

['-', '#', '-', '#', '-'],

['-', '-', '#', '-', '#'],

['#', '', '-', '-', '-'],

['-', '-', '*', '#', '-']

]

1:

[

['-', '-', '-', '-', ''],

['#', '-', '#', '#', '-'],

['#', '-', '-', '#', '#'],

['-', '#', '-', '#', '-'],

['-', '', '#', '-', '#'],

['#', '-', '*', '#', '-']

]

2:

[

['-', '-', '-', '-', ''],

['-', '-', '#', '-', '-'],

['#', '-', '#', '#', '-'],

['-', '-', '-', '#', '#'],

['-', '', '-', '-', '-'],

['-', '-', '*', '-', '#']

]

3:

[

['-', '-', '-', '-', ''],

['-', '-', '-', '-', '-'],

['-', '-', '#', '-', '-'],

['#', '-', '#', '#', '-'],

['-', '', '-', '#', '#'],

['-', '-', '*', '-', '#']

]

4:

[

['-', '-', '-', '-', ''],

['-', '-', '-', '-', '-'],

['-', '-', '-', '-', '-'],

['-', '-', '#', '-', '-'],

['#', '', '#', '#', '#'],

['-', '-', '*', '#', '#']

]

5:

[

['-', '-', '-', '-', ''],

['-', '-', '-', '-', '-'],

['-', '-', '-', '-', '-'],

['-', '-', '-', '-', '-'],

['-', '', '-', '-', '#'],

['#', '-', '*', '-', '#']

]
