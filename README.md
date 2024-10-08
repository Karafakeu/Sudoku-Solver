# Sudoku-Solver

## Main functionality
The main functionality is to solve sudoku boards somehow presented to it. This solver can be found in the file solver.py, and is based on MRV algorithmic behaviour. This is further described in the Algorithms section. The board can either be presented from the player, as described in User input, or by the random generation of the computer itself, as described in Random field. 

The choice is made by the user, as described in User input.

The main solver part is also used to validate if a sudoku board has a solution or not during the random generation.

## Random field
The program is also able to (not currently, will be able to) generate random, solveable sudoku fields for different usage, as described in the User input section. The algorithm itself is described in the Algorithms section.

## User input
In the beginning, the user is asked to choose from the following options:
* i - input your own field
* r - let the program generate a random field and you will fill it out
* rs - let the program generate a random field, which it will immediately fill out

When option "i" is picked, the user will be asked to input a sudoku field in the following format:

```
This has not yet been implemented!
```

When option "r" is picked, the user is presented with a randomly generated, solveable field, and is asked to input their moves (in other words numbers) in the following format:

```
This has not yet been implemented!
```

When option "rs" is picked, the user can simply sit back and watch the program do it's magic.

## Algorithms
### Solver
The solving algorithm is a simple MRV solving algorithm, which goes through possible moves for each field on the board, finds the one with the lowest possibilities, and recursively tries that particular move, either finding a solution or not.
### Generation
The random generation of a sudoku field is not yet implemented, will be coming in future versions!