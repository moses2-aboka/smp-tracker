import io

weekly_data = """Monday:9400
Tuesday:10400
Wednesday:8800
Thursday:7400
Friday:6500
Saturday:11200
Sunday:9600
"""

goal = 8000
days_on_goal = 0

f = io.StringIO(weekly_data)
for line in f :
    line = line.strip()
    if ":" in line:
        day,steps_str = line.split(":",1)
        steps = int (steps_str.strip())
        status = "Goal hit" if steps >= goal  else "Below goal"
        print(f"{day}:{steps}steps - {status}")
        if steps >= goal:
            days_on_goal += 1
print(f"\nDays on goal : {days_on_goal}/7")            
