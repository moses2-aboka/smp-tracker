daily_steps = [8200, 5100, 113000, 6800, 9400, 4200, 10100]
target = 8000
minimum = 5000
total = 0
valid_days = 0


for steps in daily_steps:
    print(f"Checking: {steps} steps")
    if steps >= target:
        print(f"Target hit on this day: {steps} steps.")
        continue


for steps in daily_steps:
    if steps < minimum:
        print(f"Skipping {steps} (below minimum)")
    total += steps
    valid_days += 1
print(f"Valid days: {valid_days}")
print(f"Total steps (valid day): {total}")
print(f"Average: {total // valid_days}")


while steps < 8000:
    print("Steps", steps, "done.")