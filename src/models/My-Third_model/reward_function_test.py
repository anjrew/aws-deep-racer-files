from reward_function import reward_function


tests = [
    {
        'description': 'First Round',
        'params': dict({
            'distance_from_center': 2,
            'all_wheels_on_track': True,
            'steering_angle': 2,
            'track_width': 20,
            'steps': 30,
            'speed': 4.0,
            'waypoints': [(0 if x < 20 else x // 2, x) for x in range(100)],
            'closest_waypoints': [30, 31],
            'progress': 10,
        })
    },
    {
        'description': 'Second Round',
        'params': dict({
            'distance_from_center': 2,
            'all_wheels_on_track': True,
            'steering_angle': 2,
            'track_width': 20,
            'steps': 40,
            'speed': 4.0,
            'waypoints': [(0, x) for x in range(100)],
            'closest_waypoints': [60, 61],
            'progress': 30,
        }),
    },

    {
        'description': 'Curve Should be here and th model did not slow down so should be punished',
        'params': dict({
            'distance_from_center': 2,
            'all_wheels_on_track': True,
            'steering_angle': 2,
            'track_width': 20,
            'steps': 50,
            'speed': 4.0,
            'waypoints': [
                (1, 0),
                (1, 1),
                (1, 2),
                (1, 3),
                (1, 4),
                (2, 5),
                (3, 6),
                (4, 6)
            ],
            'closest_waypoints': [0, 1],
            'progress': 50,
        }),
    },


    {
        'description': 'This should be rewarded because it slowed down for the turn',
        'params': dict({
            'distance_from_center': 2,
            'all_wheels_on_track': True,
            'steering_angle': 2,
            'track_width': 20,
            'steps': 50,
            'speed': 3.0,
            'waypoints': [
                (1, 0),
                (1, 1),
                (1, 2),
                (1, 3),
                (1, 4),
                (2, 5),
                (3, 6),
                (4, 6)
            ],
            'closest_waypoints': [0, 1],
            'progress': 60,
        }),
    },

    {
        'description': 'This should be rewarded because it slowed down for the turn again',
        'params': dict({
            'distance_from_center': 2,
            'all_wheels_on_track': True,
            'steering_angle': 2,
            'track_width': 20,
            'steps': 60,
            'speed': 2.0,
            'waypoints': [
                (1, 0),
                (1, 1),
                (1, 2),
                (1, 3),
                (1, 4),
                (2, 5),
                (3, 6),
                (4, 6)
            ],
            'closest_waypoints': [0, 1],
            'progress': 70,
        }),
    },

    {
        'description': 'This should be rewarded because it slowed down for the turn again',
        'params': dict({
            'distance_from_center': 2,
            'all_wheels_on_track': True,
            'steering_angle': 2,
            'track_width': 20,
            'steps': 70,
            'speed': 2.0,
            'waypoints': [(0 if x < 20 else x // 2, x) for x in range(100)],
            'closest_waypoints': [0, 1],
            'progress': 80,
        }),
    },

]

# for test, i in tests:
for i, test in enumerate(tests):
    result = reward_function(test.get('params'))

    print(test.get('description'))
    print(f'The Reward for test {i} is', result, '\n')
