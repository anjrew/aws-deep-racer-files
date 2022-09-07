import math


def direction_reward(params):
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

    # Reward or Penalize based on the difference
    if direction_diff > 30:
        return 1e-3 / params['speed']
    elif direction_diff > 15:
        return 0.5 / params['speed']
    elif direction_diff > 7:
        return 1.2
    elif direction_diff > 3:
        return 5 * params['speed']
    else:
        return 10 * params['speed']
