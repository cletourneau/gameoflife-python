class GameOfLife(object):

    def __init__(self, grid_lines, grid_columns):
        self.grid_lines = grid_lines
        self.grid_columns = grid_columns

    def evolve(self, grid):
        self.grid = grid
        spawning_cells = filter(self._should_spawn, self._dead_neighbours())
        living_cells = filter(self._should_live, self.grid)

        return spawning_cells + living_cells

    def _live_neighbours_of(self, cell):
        return filter(self._is_alive, self._neighbours_of(cell))

    def _dead_neighbours_of(self, cell):
        return filter(self._is_dead, self._neighbours_of(cell))

    def _neighbours_of(self, cell):
        l, c = cell
        return [(l + line_offset, c + column_offset)
                for line_offset, column_offset in NEIGHBOURS_OFFSETS]

    def _is_alive(self, cell):
        return cell in self.grid

    def _is_dead(self, cell):
        return cell not in self.grid

    def _dead_neighbours(self):
        dead_neighbours = []
        for cell in self.grid:
            dead_neighbours.extend(self._dead_neighbours_of(cell))
        return filter(self._inside_grid, self._distinct_of(dead_neighbours))

    def _inside_grid(self, cell):
        line, column = cell
        return (0 <= line < self.grid_lines) and (0 <= column < self.grid_columns)

    def _should_spawn(self, cell):
        return self._count_of(self._live_neighbours_of(cell))

    def _should_live(self, cell):
        return self._count_of(self._live_neighbours_of(cell)) in (2, 3)

    def _count_of(self, l):
        return len(l)

    def _distinct_of(self, l):
        return set(l)


NEIGHBOURS_OFFSETS = [
    (-1, -1), (-1, +0), (-1, +1),
    (+0, -1),           (+0, +1),
    (+1, -1), (+1, +0), (+1, +1)
]
