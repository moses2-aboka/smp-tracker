fasting = "Autophagy Marathon"
cold_shower = True

if fasting == "Autophagy Marathon":
    print("Fasting: 48-HOUR FAST ACTIVE")
elif fasting == "OMAD" or fasting == "2MAD":
    print("Fasting: PROTOCOL ACTIVE-", fasting)
else:
    print("Fasting: No protocal today")

if cold_shower:
    print("Cold shower : DONE ")
else:
    print("Cold shower : SKIPPED") 

print()
peak_discipline_day = cold_shower == True and fasting == "Autophagy Marathon"
if peak_discipline_day:
    print("VERDICT : Peak discipline day.")                   