import math


class PARAMS:
    prev_speed = None
    prev_steering_angle = None
    prev_steps = None
    prev_direction_diff = None
    prev_normalized_distance_from_route = None
    intermediate_progress = {}


# Gets the average curvature in degrees of the road ahead based on the agents position and the given waypoints that are ahead of the agent.
# A minimum of two waypoints must be given
# The calculation will use the first and last waypoint in the waypoints array to make the calculation if more that two waypoints are given


def _get_curvature_ahead(agent_pos, ahead_waypoints):
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

    term_1 = (b_2 + c_2 - a_2)
    term_2 = (2 * _b * _c)

    # From Cosine law
    alpha = math.acos(term_1 / term_2)
    # Converting to degree
    alpha = alpha * 180 / math.pi

    return alpha


def _curve_is_ahead(ahead_waypoints: list, distance_check: int, turn_degree_activation: int) -> bool:
    """
    Checks weather a tun is ahead on the track

    Parameters
    ----------
    - ahead_waypoints : list,
        An array of waypoints that are ahead of the agent 
    - distance_check : int,
        The distance(waypoints zero index) to start checking the track for a turn
    - turn_degree_activation:int
        The angle degree at which a turn is recognized

    Returns:
        boolean: Weather a turn was detected or not
    """

    waypoint_to_check = ahead_waypoints[distance_check]
    waypoints_to_check = [
        ahead_waypoints[distance_check + 1], ahead_waypoints[distance_check + 2]]
    curvature = _get_curvature_ahead(
        waypoint_to_check, waypoints_to_check)
    return curvature > turn_degree_activation


def reward_function(params):

    MINIMUM_SPEED = 2
    MINIMUM_REWARD = 1e-3

    # Read input parameters
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    steering_angle = params['steering_angle']
    track_width = params['track_width']
    # heading = params['heading']
    steps = params['steps']
    speed = params['speed']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    progress = params['progress']

    next_point_index = closest_waypoints[1]
    prev_point_index = closest_waypoints[0]
    # next_point = waypoints[next_point_index]
    # prev_point = waypoints[prev_point_index]
    ahead_waypoints = waypoints[next_point_index::
                                ] if next_point_index > prev_point_index else waypoints[::next_point_index]

    # Penalize if the car goes off track
    if not all_wheels_on_track:
        return 1e-3

    # - - - - -

    # Give a very low reward by default
    reward = 1e-3

    print('reward1', reward)

    # Give a high reward if no wheels go off the track and
    # the agent is somewhere in between the track borders
    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        reward += 1.0

    print('reward2', reward)

    # Reward weights
    speed_weight = 10
    drop_in_speed_punishment = 2

    # Initialize the reward based on current speed
    speed_reward = (speed * speed_weight) / 100

    print('speed_reward', speed_reward)

    reward += speed_reward

    turn_is_upcoming = _curve_is_ahead(ahead_waypoints, 4, 10)

    print('reward3', reward)

    # Calculate rewards based on previous state

    # Reinitialize previous parameters if it is a new episode
    if PARAMS.prev_steps is None or steps < PARAMS.prev_steps:
        PARAMS.prev_speed = None
        PARAMS.prev_steering_angle = None
        PARAMS.prev_direction_diff = None
        PARAMS.prev_normalized_distance_from_route = None

    # Check if the speed has dropped
    speed_has_dropped = False
    if PARAMS.prev_speed is not None:
        if PARAMS.prev_speed > speed:
            speed_has_dropped = True

    # Penalize slowing down without good reason on straight portions
    if speed_has_dropped and not turn_is_upcoming:
        drop_in_speed = PARAMS.prev_speed - speed
        # Remove value from the reward
        reward -= min(drop_in_speed / drop_in_speed_punishment, 1)

    print('reward4', reward)

    # Reward slowing down with good reason on approaching a bend
    if speed_has_dropped and turn_is_upcoming:
        drop_in_speed = PARAMS.prev_speed - speed
        # Give reward for slowing down for corners
        reward += 1

    print('reward5', reward)

    # Before returning reward, update the variables
    PARAMS.prev_speed = speed
    PARAMS.prev_steering_angle = steering_angle
    PARAMS.prev_steps = steps

    # Reward for making steady progress
    progress_reward = 10 * progress / steps
    if steps <= 5:
        progress_reward = 1  # ignore progress in the first 5 steps

    # Bonus that the agent gets for completing every 10 percent of track
    # Is exponential in the progress / steps.
    # exponent increases with an increase in fraction of lap completed
    intermediate_progress_bonus = 0
    progress_tenth_section = 10
    pi = int(progress//progress_tenth_section)
    if pi != 0 and PARAMS.intermediate_progress.get(pi) == 0:
        if pi == progress_tenth_section:  # 100% track completion
            intermediate_progress_bonus = progress_reward ** 3
        else:
            intermediate_progress_bonus = progress_reward ** 2
    PARAMS.intermediate_progress[pi] = intermediate_progress_bonus

    reward += intermediate_progress_bonus

    print('reward6', reward)

    # If going below the minimum speed remove some reward
    if speed < MINIMUM_SPEED:
        reward -= 1

    print('reward7', reward)

    # Always return a float value
    return max(float(reward), MINIMUM_REWARD)
