from get_curvature_ahead import get_curvature_ahead

A = (3, 6)
B = (3, 4)
C = (5, 2)


DEGREES_CURVE = get_curvature_ahead(A, [B, C])
print('The curvature is', DEGREES_CURVE)
