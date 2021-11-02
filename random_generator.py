from random import randint

# @ToDo...
# create 2d array with all 0s
# generate random values which will be 2d array indexes
# add the Mines to the array instead of the 0s
# get the array index and put +1 near the boxes
# make the user play


class Cell():
    def __init__(self):
        self.mine = False
        self.flagged = False
        self.opened = False
        self.value = 0

    def get_value(self):
        if(self.opened == True):
            return ""
        elif(self.flagged == True):
            return "F"


MAX_MINES = 5


class random_gen:
    def __init__(self):
        # if the value is False, the cell was not opened, if the value is 1 the cell was opened, if the cell is M, it has a mine,
        # if the value is True, it was flagged
        self.grid_size = 8
        self.array = [[Cell() for i in range(self.grid_size)]
                      for i in range(self.grid_size)]
        self.numberMines = 0
        self.start()

    # fills the array with numbers and mines
    def start(self):
        self.random_numb()

    # created random numbers which will be the indexes where the mines will be
    def random_numb(self):
        for i in range(MAX_MINES):
            x = randint(0, (self.grid_size - 1))
            y = randint(0, (self.grid_size - 1))
            if(self.array[x][y].mine != True):
                self.array[x][y].mine = True
                self.numberMines = self.numberMines + 1
            self.add_value(x, y)

    # adds 1 to a value close to the mine
    def add_value(self, x, y):
        # same line as given indexed
        if(y-1 >= 0 and self.array[x][y-1].mine == False):
            self.array[x][y-1].value = self.array[x][y-1].value + 1
        if(y+1 < 8 and self.array[x][y+1].mine == False):
            self.array[x][y+1].value = self.array[x][y+1].value + 1

        # line under given indexed
        if(x+1 < 8):
            if(y-1 >= 0 and self.array[x+1][y].mine == False):
                self.array[x+1][y].value = self.array[x+1][y].value + 1
            if(y+1 < 8 and self.array[x+1][y+1].mine == False):
                self.array[x+1][y+1].value = self.array[x+1][y+1].value + 1
            if(y >= 0 and self.array[x+1][y-1].mine == False):
                self.array[x+1][y-1].value = self.array[x+1][y-1].value + 1

        # line up given indexed
        if(x-1 >= 0):
            if(y-1 >= 0 and self.array[x-1][y-1].mine == False):
                self.array[x-1][y-1].value = self.array[x-1][y-1].value + 1
            if(y+1 < 8 and self.array[x-1][y+1].mine == False):
                self.array[x-1][y+1].value = self.array[x-1][y+1].value + 1
            if(y >= 0 and self.array[x-1][y].mine == False):
                self.array[x-1][y].value = self.array[x-1][y].value + 1

    def get_array(self):
        return self.array

    def print_value(self, cell):
        if(cell.opened == True):
            print("|", cell.value, end="  ")
        elif(cell.flagged == True):
            print("|", "F", end="  ")
        else:
            print("|", "*", end="  ")
