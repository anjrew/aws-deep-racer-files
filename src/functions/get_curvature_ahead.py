import math
from typing import Tuple


# Gets the average curvature in degrees of the road ahead based on the agents position and the given waypoints that are ahead of the agent.
# A minimum of two waypoints must be given
# The calculation will use the first and last waypoint in the waypoints array to make the calculation if more that two waypoints are given
def get_curvature_ahead(agent_pos: Tuple[int, int], ahead_waypoints: list):
    amount_of_waypoints = len(ahead_waypoints)
    if amount_of_waypoints < 2:
        raise Exception(
            f'''There must be at least 2 waypoints given to calculate curvature.
            Only {amount_of_waypoints} were given''')
    # The waypoint that helps give the direction of the agent
    # The waypoint that gives the direction of the road
    direction_waypoint = ahead_waypoints[0]

    return _get_angle(agent_pos, direction_waypoint, ahead_waypoints[1])


# Python code to find all three angles
# of a triangle given coordinate
# of all three vertices

# returns square of distance b/w two points
def _length_square(_x, _y):
    x_diff = _x[0] - _y[0]
    y_diff = _x[1] - _y[1]
    return x_diff * x_diff + y_diff * y_diff


def _get_angle(_a, _b, _c):
    # Square of lengths be a2, b2, c2
    a_2 = _length_square(_b, _c)
    b_2 = _length_square(_a, _c)
    c_2 = _length_square(_a, _b)

    # length of sides be a, b, c
    _b = math.sqrt(b_2)
    _c = math.sqrt(c_2)

    # From Cosine law
    alpha = math.acos((b_2 + c_2 - a_2) /
                      (2 * _b * _c))

    # Converting to degree
    alpha = alpha * 180 / math.pi

    return alpha
