from random_generator import random_gen
from inputClass import userInput


class mainClass():
    def __init__(self):
        self.random = random_gen()
        self.input = userInput()
        self.res_array = self.random.get_array()
        self.remaining_lives = (
            self.random.grid_size * self.random.grid_size) - self.random.numberMines

    def print(self):
        for x in range(self.random.grid_size+1):
            if(x == 0):
                print(end="    ")
            else:
                print(x, end="    ")
        print()

        for x in range(self.random.grid_size):
            print(x+1, end=" ")
            for y in range(self.random.grid_size):
                self.random.print_value(self.res_array[x][y])
            print()

    def user_input(self, row, column, command):
        print(self.res_array[row][column].mine, 'see this\n\n')
        res = True
        if(self.res_array[row][column].opened == True):
            print("You cannot open this cell!")
        elif(command == "O"):
            if(self.res_array[row][column].mine == True):
                print('Ops! You have lost')
                res = False
            else:
                self.res_array[row][column] = self.input.open_cell(
                    self.res_array[row][column])
                self.remaining_lives = self.remaining_lives - 1
        elif(command == "F"):
            self.res_array[row][column].flagged = self.input.flag_cell(
                self.res_array[row][column])
        return res
        # if(command == "F"):

        # if(self.res_array[column][row] == "F" and command == "F"):
        #     self.res_array[column][row] = 0
        # if()
        # if(self.res_array[column][row] != "1"):
        #     self.input.get_input(self.res_array[column][row])
        # else:
        #     print("You have already opened this cell")


mainObj = mainClass()
print("---Start game---")
loop = True

while(loop and mainObj.remaining_lives > 0):
    mainObj.print()
    row = int(input('row: '))
    column = int(input('column: '))
    print('Command: ')
    command = input()
    loop = mainObj.user_input(row-1, column-1, command)
