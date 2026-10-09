def weekly_report(name,steps_list,goal = 10000):
    days_on_target = 0
    for s in steps_list:
        if s >= goal:
            days_on_target += 1
    avg = sum(steps_list) / len(steps_list)       
  
   

    print(f"----{name}'s week----")
    print(f"Days tracked : {len(steps_list)}")
    print(f"Days og goal : {days_on_target}")
    print(f"Average steps : {round(avg,0)}")
    print()



weekly_report("Moses",[11000,10500,99000,12100,13400,9200,15000])
weekly_report("Albert",[9900,13000,10400,8500,7200,14500,13200])    