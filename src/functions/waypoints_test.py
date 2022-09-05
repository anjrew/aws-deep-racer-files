from waypoints import up_sample


ORIGINAL = [(0, 0), (0, 2), (0, 4), (0, 10)]
UP_SAMPLED = up_sample(ORIGINAL, 5)

print('\nThe original waypoints are', ORIGINAL, len(ORIGINAL))
print('\nThe new up sampled waypoints are', UP_SAMPLED, len(UP_SAMPLED))
