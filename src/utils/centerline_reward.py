def centerline_reward(params):
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    is_left_of_center = params['is_left_of_center']
    steering_angle = params['steering_angle']

    # Calculate 4 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.2 * track_width
    marker_3 = 0.3 * track_width
    marker_4 = 0.4 * track_width

    all_wheels_on_track = params['all_wheels_on_track']
    is_offtrack = params['is_offtrack']
    is_reversed = params['is_reversed']

    if is_offtrack or is_reversed:
        return 0
    elif not all_wheels_on_track:
        return 0.0001
    elif distance_from_center <= marker_1:
        return 5
    elif distance_from_center <= marker_2:
        return 3
    elif distance_from_center <= marker_3:
        return 2
    elif distance_from_center <= marker_4:
        return 1
    else:
        return 0.1
