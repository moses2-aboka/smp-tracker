steps = 7500 
sleep_hours = 6 
water_glasses = 5 
cold_shower = False
pages_read = 15

if steps >= 10000:
    print("Excellent. Steps above 10000")
elif steps >= 7500:
    print("Good. Steps above 75000")
else:
    print("Needs more work otherwise")

if sleep_hours >= 7:
    print("Good. Sleep above 7 hours")
elif sleep_hours < 7:
    print("Low. Sleep below 7 hours")  

if water_glasses > 8:
    print("Good. Water glasses above 8")
elif water_glasses < 8:
    print("Low. Water glasses below 8")

if cold_shower:
    print("Cold shower. Skipped") 

if pages_read >= 10:
    print("Good . More than 10 pages read") 

print("I need to walk more steps, sleep more hours, drink more water and to take cold shower often, for good Health . ")                            