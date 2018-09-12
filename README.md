#Project 2A

Write a Python 3 program that takes two states, a *start* state and a *goal* state, of a 9-puzzle and determines:

1. Whether the goal state is reachable from the start state. An algorithm is described at [How to check if an instance of 15 puzzle is solvable?](https://www.geeksforgeeks.org/check-instance-15-puzzle-solvable/)
2. Displays the state of a puzzle as a grid&mdash;for example:
   ```
     1  2  3
     4  5  6
     7  8  
    ```
    or
    ```
    123
    456
    78
    ```
3. Computes a heuristic function `h()` between two states.

The two states are provided on the
command line using strings of digits
1 through 8 to indicate a tile and
a space to denote the absent tile.
For example, the board shown above
is entered on a command line as
`"12345678 "`.

Implement a state as a class:
```
class State:
    """A state of a 9-puzzle board"""
    
    def __init__(self, board_str):
 
```
