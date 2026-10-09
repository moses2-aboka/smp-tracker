import csv
import io

csv_data = """day,steps,skill
Monday,9200,welding
Tuesday,10500,tilling
Wednesday,11000,farming
Thursday,6500,plumbing
Friday,7800,copywriting
Saturday,9800,phonerepair
Sunday,6800,fishing"""

f = io.StringIO(csv_data)
reader = csv.DictReader(f)

valid_steps = []
for row in reader:
    steps = int(row["steps"])
    if steps >= 7000:
        valid_steps.append(steps)
        print(f"{row['day']} :{steps}steps ({row['skill']})")
    else:
        print(f"{row['day']} :{steps}steps-flagged as invalid")

avg = sum(valid_steps) / len(valid_steps)
print(f"\nAverage(valid_days) : {round(avg)} steps")            