weeek_steps = [7800, 8200, 9400, 6000, 10000, 12000, 5000]
for steps in weeek_steps:
    if steps >= 8000:
        print(steps, "Steps - Goal hit.")
    else:
        print(steps, "Steps - Below goal.")


print("Days tracked:", len(weeek_steps))            