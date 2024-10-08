def getCurrentMoves(field, x, y):
    currentMoves = [1, 2, 3, 4, 5, 6, 7, 8, 9] # create a list to pop from

    # select all possible moves
    for z in range(len(field[x])):
        if field[x][z] != 0 and field[x][z] in currentMoves:
            currentMoves.pop(currentMoves.index(field[x][z]))
    for z in range(len(field)):
        if field[z][y] != 0 and field[z][y] in currentMoves:
            currentMoves.pop(currentMoves.index(field[z][y]))
    for a in range(0 if x in range(0, 3) else 3 if x in range(3, 6) else 6, 3 if x in range(0, 3) else 6 if x in range(3, 6) else 9):
        for b in range(0 if y in range(0, 3) else 3 if y in range(3, 6) else 6, 3 if y in range(0, 3) else 6 if y in range(3, 6) else 9):
            if field[a][b] != 0 and field[a][b] in currentMoves:
                currentMoves.pop(currentMoves.index(field[a][b]))
    
    return currentMoves

def solve(field, depth=0):
    moves = {}
    for x in range(len(field)):
        for y in range(len(field[x])):
            if field[x][y] == 0: # empty space
                currentMoves = getCurrentMoves(field, x, y)
                # mrv implementation - save all possible move combinations
                if len(currentMoves) < 1:
                    return None
                moves[(x, y)] = currentMoves
        
    if len(moves) == 0:  # No more moves
        return field if not any(0 in row for row in field) else None
    
    # Select the cell with the fewest possible moves (MRV)
    mrvCell = min(moves.items(), key=lambda x: len(x[1]))[0]
    x, y = mrvCell
    for move in moves[mrvCell]:
        field[x][y] = move
        temp = solve(field, depth + 1)
        if temp:
            return temp
        field[x][y] = 0  # Backtrack if the move doesn't work

    return None
    
def validate(field):
    result = solve(field)
    if result == None:
        return False

    return True