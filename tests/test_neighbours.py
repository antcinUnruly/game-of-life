from conway.neighbours import Neighbours


class TestNeighbours():

    def test_neighbours(self):
        neighbours = Neighbours()

        neighbours.neighbour_right.status = False
        neighbours.neighbour_bottom_right = True
        neighbours.neighbour_bottom = False
        neighbours.neighbour_bottom_left = True
        neighbours.neighbour_left = False
        neighbours.neighbour_top_left = True
        neighbours.neighbour_top = False
        neighbours.neighbour_top_right = True

        assert (neighbours.get_neighbour_status(neighbours.neighbour_right) == False)
