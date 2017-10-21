from enum import Enum

class Direction(Enum):
    __order__ = "N_left N_straight N_right E_left E_straight E_right S_left S_straight S_right W_left W_straight W_right"
    N_left = 0
    N_straight = 1
    N_right = 2
    E_left = 3
    E_straight = 4
    E_right = 5
    S_left = 6
    S_straight = 7
    S_right = 8
    W_left = 9
    W_straight = 10
    W_right = 11