import random
import math

def generate_week():
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    total = 0
    goal_day = 0

    for day in days :
        steps = random.randint(6000,12000)
        total += steps
        if steps >= 8000 :
            goal_day += 1
        print(f"{day}:{steps} steps")


    avg = math.floor(total / 7)
    print(f"\nAverage steps : {avg}")
    print(f"Days on goal : {goal_day} / 7")  


generate_week()          