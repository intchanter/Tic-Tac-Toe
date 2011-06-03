#!/usr/bin/env python

players = ('X', 'O')

wins = (
    # Horizontal
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    # Vertical
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    # Diagonal
    (0, 4, 8),
    (2, 4, 6),
)

class Board(object):
    def __init__(self):
        self.spaces = range(9)

    def __repr__(self):
        return '''
%s | %s | %s
--+---+--
%s | %s | %s
--+---+--
%s | %s | %s
        '''.strip() % tuple(self.spaces)

    def __unicode__(self):
        return unicode(self.__repr__())

    def isEmpty(self, index):
        raise NotImplementedError('Implement test for an empty square.')

    def move(self, index, player):
        raise NotImplementedError('Implement the ability for a player to move.')
    def isWon(self):
        raise NotImplementedError('Implement test for end of game.')