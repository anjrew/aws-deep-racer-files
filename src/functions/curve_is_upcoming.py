
from get_curvature_ahead import get_curvature_ahead


def curve_is_ahead(ahead_waypoints: list, distance_check: int, turn_degree_activation: int) -> bool:
    """
    Checks weather a tun is ahead on the track

    Parameters
    ----------
    - ahead_waypoints : list,
        An array of waypoints that are ahead of the agent 
    - distance_check : int,
        The distance(Amount of waypoints) to start checking the track for a turn
    - turn_degree_activation:int
        The angle degree at which a turn is recognized

    Returns:
        boolean: Weather a turn was detected or not
    """

    waypoint_to_check = ahead_waypoints[distance_check]
    waypoints_to_check = [
        ahead_waypoints[distance_check + 1], ahead_waypoints[distance_check + 2]]
    curvature = get_curvature_ahead(
        waypoint_to_check, waypoints_to_check)
    return curvature > turn_degree_activation
