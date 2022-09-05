from curve_is_upcoming import curve_is_ahead


TEST_A = dict({
    'distance_check': 5,
    'waypoints': [
        (1, 0),
        (1, 1),
        (1, 2),
        (1, 3),
        (1, 4),
        (2, 5),
        (3, 6),
        (4, 6)],
    'turn_degree_activation': 10
})

TEST_A_RESULT = curve_is_ahead(TEST_A.get('waypoints'), TEST_A.get(
    'distance_check'), TEST_A.get('turn_degree_activation'))

print('The result form test A was', TEST_A_RESULT)


TEST_B = dict({
    'distance_check': 5,
    'waypoints': [
        (1, 0),
        (1, 1),
        (1, 2),
        (1, 3),
        (1, 4),
        (1, 5),
        (1, 6),
        (1, 7)],
    'turn_degree_activation': 10
})

TEST_B_RESULT = curve_is_ahead(TEST_B.get('waypoints'), TEST_B.get(
    'distance_check'), TEST_B.get('turn_degree_activation'))

print('The result form test B was', TEST_B_RESULT)

TEST_C = dict({
    'distance_check': 5,
    'waypoints': [
        (1, 0),
        (1, 1),
        (1, 2),
        (1, 3),
        (1, 4),
        (2, 5),
        (3, 6),
        (4, 6)],
    'turn_degree_activation': 20
})

TEST_C_RESULT = curve_is_ahead(TEST_C.get('waypoints'), TEST_C.get(
    'distance_check'), TEST_C.get('turn_degree_activation'))

print('The result form test C was', TEST_C_RESULT)
