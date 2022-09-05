from get_curvature_ahead import get_curvature_ahead

RIGHT_TURN = dict({
    'A': (3, 6),
    'B': (3, 4),
    'C': (5, 2)
})

RIGHT_TURN_DEGREES_CURVE = get_curvature_ahead(
    RIGHT_TURN.get('A'), [RIGHT_TURN.get('B'), RIGHT_TURN.get('C')])
if RIGHT_TURN_DEGREES_CURVE != 26.56505117707799:
    raise Exception(
        'RIGHT_TURN_DEGREES_CURVE test failed with incorrect value of', RIGHT_TURN_DEGREES_CURVE)

print('The curvature for a left turn is', RIGHT_TURN_DEGREES_CURVE)


LEFT_TURN = dict({
    'A': (0, 0),
    'B': (0, 2),
    'C': (2, 2)
})

LEFT_TURN_DEGREES_CURVE = get_curvature_ahead(
    LEFT_TURN.get('A'), [LEFT_TURN.get('B'), LEFT_TURN.get('C')])
if LEFT_TURN_DEGREES_CURVE != 45.00000000000001:
    raise Exception(
        'LEFT_TURN_DEGREES_CURVE test failed with incorrect value of', LEFT_TURN_DEGREES_CURVE)

print('The curvature for a left turn is', LEFT_TURN_DEGREES_CURVE)
