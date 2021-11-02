from abc import ABC, abstractmethod


class userInput(ABC):
    # def __init__(self, row, col, command):
    #     self.row = row
    #     self.col = col
    #     self.command = command

    # @abstractmethod
    # def read(self):
    #     return {
    #         self.row,
    #         self.col,
    #         self.command
    #     }

    def flag_cell(self, cell):
        return not cell.flagged

    def open_cell(self, cell):
        if(cell.flagged == True):
            print('You cannot open a flagged cell')
            return cell
        else:
            cell.opened = True
            return cell
