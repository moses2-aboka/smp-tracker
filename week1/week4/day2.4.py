daily_logs = [
    {"day":"Monday", "steps":"9200"},
    {"day":"Tuesday", "steps":"not recorded"},
    {"day":"Wednesday","steps":"10500"},
    {"day":"Thursday", "steps":None},
    {"day":"Friday", "steps":"8800"},
]

valid_steps =[]
for log in daily_logs :
    try:
        steps = int(log["steps"])
        valid_steps.append(steps)
        print(f"{log['day']} : {steps}steps")
    except (ValueError, TypeError):
        print(f"{log['day']} : Invaliv data. Skipped.")

if valid_steps :
    avg = sum(valid_steps)/ len(valid_steps)
    print(f"\nAverage from valid days :{round(avg)}steps")            
