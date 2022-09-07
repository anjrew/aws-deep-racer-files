

def progress_reward(params: dict):
    steps = params.get('steps', 0)
    if steps <= 5:
        return 1  # ignore progress in the first 5 steps
    else:
        progress = params.get('progress', 0)
        return 10 * progress / steps
