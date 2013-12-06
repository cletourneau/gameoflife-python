import unittest
from gameoflife.game_of_life import GameOfLife
from hamcrest import assert_that, is_
from nose.tools import istest


class GameOfLifeTest(unittest.TestCase):

    @istest
    def a_cell_without_neighbours_dies_of_underpopulation(self):
        evolution = self.evolve([
            (0, 0)
        ])

        assert_that((0, 0) not in evolution)

    @istest
    def a_cell_stays_alive_when_it_has_2_neighbours(self):
        evolution = self.evolve([
            (0, 0), (0, 1), (0, 2)
        ])

        assert_that((0, 1) in evolution)

    @istest
    def a_cell_stays_alive_when_it_has_3_neighbours(self):
        evolution = self.evolve([
            (0, 0), (0, 1), (0, 2),
                    (1, 1)
        ])

        assert_that((1, 1) in evolution)

    @istest
    def a_cell_with_more_than_3_neighbours_dies_of_overpopulation(self):
        evolution = self.evolve([
            (1, 0), (1, 1), (1, 2),
            (2, 0), (2, 1)
        ])

        assert_that((1, 1) not in evolution)

    @istest
    def a_cell_spawns_when_it_has_3_neighbours(self):
        evolution = self.evolve([
            (0, 0), (0, 1),
            (1, 0),
        ])

        assert_that((1, 1) in evolution)

    @istest
    def a_cell_does_not_spawn_outside_the_grid_limit(self):
        self.game = GameOfLife(3, 3)
        evolution = self.evolve([
            (0, 0), (0, 1), (0, 2)
        ])

        assert_that((-1, 1) not in evolution)

    @istest
    def a_cell_is_inside_the_grid(self):
        assert_that(self.game._inside_grid((2, 2)), is_(True))

    @istest
    def a_cell_up_the_grid_is_not_inside(self):
        assert_that(self.game._inside_grid((-1, 0)), is_(False))

    @istest
    def a_cell_down_the_grid_is_not_inside(self):
        assert_that(self.game._inside_grid((5, 0)), is_(False))

    @istest
    def a_cell_left_to_the_grid_is_not_inside(self):
        assert_that(self.game._inside_grid((0, -1)), is_(False))

    @istest
    def a_cell_right_to_the_grid_is_not_inside(self):
        assert_that(self.game._inside_grid((0, 5)), is_(False))

    def setUp(self):
        self.game = GameOfLife(5, 5)
        self.evolve = self.game.evolve
