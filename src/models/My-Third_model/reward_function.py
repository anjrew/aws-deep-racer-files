import math
from functools import reduce


class PREVIOUS_PARAMS:
    prev_speed = None
    prev_steering_angle = None
    prev_steps = None
    prev_direction_diff = None
    prev_normalized_distance_from_route = None
    intermediate_progress = {}


def compose_params(params: dict, prev_params: dict):
    """Composes current and previous params into one object

    Args:
        params (dict): the current params of the step experience
        prev_params (dict): the params of the previous experience

    Returns:
        _type_: A dictionary containing current and previous params
    """

    return {**params, **prev_params}


def direction_reward(params: dict, weight=1):
    # Read input variables
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    steering_angle = params['steering_angle']
    heading = heading + steering_angle

    # Alter the array to make sure the first point is the one just behind the car
    # Then we can identify and target the 9th
    # Compare target point and current x-y coordinates to identify the direction
    waypoints = waypoints[closest_waypoints[0]:] + \
        waypoints[:closest_waypoints[0]]
    next_point = waypoints[9]
    prev_point = (params['x'], params['y'])

    # Now identify the direction that the car should be heading
    track_direction = math.atan2(
        next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    track_direction = math.degrees(track_direction)

    # Get the difference between the ideal and actual.
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    def calc_reward(x):
        return x * weight

    # Reward or Penalize based on the difference
    if direction_diff > 30:
        return calc_reward(0)
    elif direction_diff > 15:
        return calc_reward(0.25)
    elif direction_diff > 7:
        return calc_reward(0.5)
    elif direction_diff > 3:
        return calc_reward(0.75)
    else:
        return calc_reward(1)


def speed_reward(params: dict, weight=1):
    max_speed = 4
    return params.get('speed', 0) / max_speed * weight


def progress_reward(params: dict, weight=1):
    steps = params.get('steps', 0)
    max_progress = 100
    if steps <= 5:
        return 0  # ignore progress in the first 5 steps
    else:
        progress = params.get('progress', 0)
        return progress / max_progress / steps * weight


def reward_function(params: dict):
    """The reward function given the parameter state

    Args:
        params dict: The parameters that can be found here

    Returns:
        float: A reward value
    """

    # params = compose_params(params, PREVIOUS_PARAMS.__dict__)

    # Penalize if the car goes off track
    if not params['all_wheels_on_track']:
        return 1e-3

    # Start with reward at minimum value and then accumulate the different rewards together for the final reward
    reward = reduce(lambda a, b: a + b, [
        1e-3,  # Minimum reward
        direction_reward(params, 1),
        speed_reward(params, 2),
        progress_reward(params, 10)
    ])

    # Always return a float value
    return float(reward)
