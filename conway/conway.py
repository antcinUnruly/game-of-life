from .cell import Cell


class Game:
    def run(self, observed_square):
        for x in observed_square:
            print(x)


        # if cell.status == True:
        #     self.alive(cell, neighbours_number)
        #     return cell
        #
        # if cell.status == False:
        #     self.dead(cell, neighbours_number)
        #     return cell

    def alive(self, cell, neighbours_number):
        if neighbours_number == 1:
            cell.status = False
            return cell
        if (neighbours_number == 2) or (neighbours_number == 3):
            cell.status = True
            return cell
        if neighbours_number > 3:
            cell.status = False
            return cell

    def dead(self, cell, neighbours_number):
        if neighbours_number == 3:
            cell.status = True
            return cell
