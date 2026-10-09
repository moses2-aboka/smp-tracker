step_count = [8800, 6500, 11000, 9200, 7300]
step_count.append(10500)
step_count.remove(6500)
step_count.sort(reverse=True)
print("Final list:", step_count)


high_days = 0
for s in step_count:
    if s >= 9000:
       high_days += 1
print("Days exceeding 9000 steps:", high_days)   