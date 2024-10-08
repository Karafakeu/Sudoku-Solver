import solver
import random
import copy

first = True

def main():
    global first

    choice = input("Do you want to create a random sudoku and let the computer solve it immediately (rs), create a random sudoku and you solve it yourself (r), or input a sudoku and let the computer solve it (i)? ")

    while choice not in ["rs", "r", "i"]:
        choice = input("Please, pick one of the options above. ")

    if choice == "rs": # random and solve
        valid = False
        while not valid:
            field = randomField()
            printField(field)
            tempField = copy.deepcopy(field)
            valid = solver.validate(tempField)
            print(valid)

        print("Randomly generated field, starting computer solve:")
        printField(field)
        print()

        field = solver.solve(field)

        if field == None:
            print("This sudoku could not be solved, please try again later"); exit()
        
        print("This is the solved field:")
        printField(field)

        input("Press any button to restart... ")
        main()
        
    elif choice == "r": # random
        valid = False
        while not valid:
            field = randomField()
            valid = solver.validate(field)

        print("Randomly generated field:")
        printField(field)

    elif choice == "i": # input
        field = input("Please input your sudoku: \n")

        # make the field a 2d array, eventually input this from the player. 
        field = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0]]

        first, start(first)

        print("Solving for this field:")
        printField(field)
        print()

        field = solver.solve(field)

        if field == None:
            print("This sudoku could not be solved, please try again later"); exit()
        
        print("This is the solved field:")
        printField(field)

        input("Press any button to restart... ")
        main()
    
def printField(field):
    for x in range(len(field)):
        row = ""

        for y in range(len(field[x])):
            if y % 3 == 0 and y != 0:
                row += "|"

            row += str(field[x][y])

        if x % 3 == 0 and x != 0:
            print("---+---+---")
        print(row)
        

def start(first=False):
    if first:
        pass
    return False

def randomField():
    field = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    return field

if __name__ == "__main__":
    main()