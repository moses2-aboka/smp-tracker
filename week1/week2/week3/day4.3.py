pupils = [
    {"name":"Moses","steps":[11000,10500,12000,13100,12400,8000,9500]},
    {"name":"Hope","steps":[9000,8500,10200,7500,11000,9400,12100]},
    {"name":"Andy","steps":[15000,12300,1400,7600,11000,85000,10600]},
    {"name":"Aston","steps":[9800,10200,13400,12100,10600,9400,11000]},
]

all_steps = [s for p in pupils for s in p["steps"]]
high_steps = [s for s in all_steps if s > 10000]
print("Steps above 10000:", high_steps)


#2. names with average steps above 9000
high_avg_names = [p["name"] for p in pupils if sum(p["steps"]) / len(p["steps"]) > 9000]
print("High average performed:", high_avg_names)
