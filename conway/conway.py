from .cell import Cell

class Game:
    def run(self, cell, neighbours_number):
        if neighbours_number == 1:
            if cell.status == True:
                cell.status = False
                return cell
        if (neighbours_number == 2) or (neighbours_number == 3):
            if cell.status == True:
                cell.status = True
                return cell
        if neighbours_number > 3:
            if cell.status == True:
                cell.status = False
                return cell
        if neighbours_number == 3:
            if cell.status == False:
                cell.status = True
                return cell

