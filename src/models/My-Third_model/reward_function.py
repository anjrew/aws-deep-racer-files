import math


class PARAMS:
    prev_speed = None
    prev_steering_angle = None
    prev_steps = None
    prev_direction_diff = None
    prev_normalized_distance_from_route = None


def reward_function(params):
    '''
    Agent to stay inside the two borders of the track
    '''

    # Read input parameters
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    steering_angle = params['steering_angle']
    track_width = params['track_width']
    heading = params['heading']
    steps = params['steps']
    speed = params['speed']

    # Penalize if the car goes off track
    if not all_wheels_on_track:
        return 1e-3

    # - - - - -

    # Give a very low reward by default
    reward = 1e-3

    # Give a high reward if no wheels go off the track and
    # the agent is somewhere in between the track borders
    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        reward = 1.0

    # Reward weights
    speed_weight = 1

    # Initialize the reward based on current speed
    max_speed_reward = 10 * 10
    min_speed_reward = 3.33 * 3.33
    abs_speed_reward = params['speed'] * params['speed']
    speed_reward = (abs_speed_reward - min_speed_reward) / \
        (max_speed_reward - min_speed_reward) * speed_weight

    reward += speed_reward

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
        speed_maintain_bonus = min(speed / PARAMS.prev_speed, 1)

    # Before returning reward, update the variables
    PARAMS.prev_speed = speed
    PARAMS.prev_steering_angle = steering_angle
    PARAMS.prev_steps = steps

    # Assign rewards based on previous state
    reward += speed_maintain_bonus

    # Always return a float value
    return float(reward)
