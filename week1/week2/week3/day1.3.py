def day_report(steps,water,protocol):
    print("----DAILY REPORT----")
    print(f"Steps : {steps}")
    print(f"Water : {water}glasses")
    print(f"Protocol : {protocol}")
    print()
   

def hit_goal(steps):
    return steps >= 8000

day_report(9500, 7, "OMAD")
day_report(7500, 8, "2MAD")
day_report(10200, 6, "OMAD")

print("Goal hit(7500)?", hit_goal(7500))
print("Goal hit(10200)?", hit_goal(10200))