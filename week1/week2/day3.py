my_log = {
    "steps": 9000,
    "water_glasses": 7,
    "fasting_protocol": "OMAD",
    "cold_shower": True,
    "sleep_hours": 8.5
}

print("My Profile :")
for key, value in my_log.items ():
    print(key, ":", value)

print()

if my_log["steps"] >= 8000 :
    print("Steps target Hit.")

else: 
    print("Steps target not Hit.")        
