week_log = [
    {"day":"Monday","steps":9000,"protocol":"OMAD"},
    {"day":"Teusday","steps":10400,"protocol":"2MAD"},
    {"day":"Wednesday","steps":12000,"protocol":"OMAD"},
    {"day":"Thursday","steps":85000,"protocol":"OMAD"},
    {"day":"Friday","steps":10000,"protocol":"2MAD"},
]
total = 0
for log in week_log :
    print(log["day"], "-", log["steps"], "steps -", log["protocol"])
    total += log["steps"]

average = total / len(week_log)    

print()
print("Average step count:", average) 