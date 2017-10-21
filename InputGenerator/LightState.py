from enum import Enum
from Direction import Direction

class LightState(Enum):
    North = [Direction.N_left, Direction.N_straight, Direction.N_right]
    East = [Direction.E_left, Direction.E_straight, Direction.E_right]
    South = [Direction.S_left, Direction.S_straight, Direction.S_right]
    West = [Direction.W_left, Direction.W_straight, Direction.W_right]
    North_South_Turn = [Direction.N_left, Direction.S_left, Direction.E_right, Direction.W_right]
    East_West_Turn = [Direction.E_left, Direction.W_left, Direction.N_right, Direction.S_right]
    North_South_Straight = [Direction.N_straight, Direction.N_right, Direction.S_straight, Direction.S_right]
    East_West_Straight = [Direction.E_straight, Direction.E_right, Direction.W_straight, Direction.W_right]