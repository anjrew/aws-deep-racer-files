# TODO this needs fixing
# Up samples the missing gaps in the waypoints to give evenly spaced waypoints
def up_sample(waypoints: list, k: int) -> list:
    _p = waypoints
    _n = len(_p)
    return [[i / k * _p[(j+1) % _n][0] + (1 - i / k) * _p[j][0],
             i / k * _p[(j+1) % _n][1] + (1 - i / k) * _p[j][1]] for j in range(_n) for i in range(k)]
