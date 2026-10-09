def assess_day(steps):
    return steps >= 10000 and steps is not None

def assess_day(steps, goal=10000):
    return steps >= goal