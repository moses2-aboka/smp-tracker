print("====EXERCISE 1 DATAFRAMES====")
import pandas as pd
#Create a DataFrame from a dictionary and inspect it
data = {
    "name": ["Eric", "Moses", "Albert", "Aboka"],
    "score": [85, 72, 91, 68],
    "city": ["Nairobi", "Mombasa", "Nairobi", "Kisumu"]
}
df = pd.DataFrame(data)
print(df)
print("Shape  (rows, cols):", df.shape)
print("Columns:", list(df.columns))
print("Data types:", df.dtypes)
print(df.to_string())

print("\n====EXERCISE 2 FILTERING====")
#Filter to show only students from Nairobi with score above 80
result = df[(df['city'] == 'Nairobi') & (df['score'] > 80)]
print(result)

print("\n====EXERCISE 3 GROUPING====")
#Group by city and get the average score by city
grouped = df.groupby("city")["score"].mean().round(1)
print(grouped)


print("\n====EXERCISE 4 NUMPHY CHALLANGE====")
#Create an array of 10 random integers between 1 and 100
#Print the mean, max, min, and standard deviation
import numpy as np
data = np.array([48, 32, 24, 53, 67, 74, 18, 91, 88, 66])
print("Data array:", data)
print(f"Mean:  {np.mean(data):.2f}")
print(f"Max:  {np.max(data)}")
print(f"Min:  {np.min(data)}")
print(f"Std daev:  {np.std(data):.2f}")

print("\n==EX 5-TILLING CONTRACTOR JOB TRACKER==")
import pandas as pd
import numpy as np
#Tilling contactor job records
jobs = [
    {"client":"Kamau","location":"Kiambu","boxes_used":30,"price_per_box":1800},
    {"client":"Aboka","location":"Vihiga","boxes_used":48,"price_per_box":2100},
    {"client":"Odhiambo","location":"Kisumu","boxes_used":20,"price_per_box":1600},
    {"client":"Hope","location":"Mombasa","boxes_used":60,"price_per_box":2200},
    {"client":"Moses","location":"Luanda","boxes_used":50,"price_per_box":2400},
]
print("Job Summary:")
print("=" * 60)
total_boxes = 0
total_revenue = 0
for j in jobs:
    revenue = j["boxes_used"] * j["price_per_box"]
    print(f"{j['client']} ({j['location']}): {j['boxes_used']} boxes  | KES{revenue:,}")
    total_boxes += j["boxes_used"]
    total_revenue += revenue

avg_price = total_revenue / total_boxes
print(f"\nTotal boxes laid: {total_boxes}")
print(f"Total revenue: KES {total_revenue:,}")
print(f"Average price per box: KES {avg_price:.0f}")


print("\n==EX 6-FARMING-WEEKLY MILK YIELD ANALYSIS")
#Weekly milk yield per cow (litres)
herd_data = [
    {"cow": "hope", "yields": [72, 68, 74, 70]},
    {"cow": "Sakwa", "yields": [45, 42, 38, 40]},
    {"cow": "Basel", "yields": [88, 91, 85, 93]},
    {"cow": "Bella", "yields": [55, 58, 52, 50]},
    {"cow": "Lola", "yields": [78, 80, 76, 82]},
]
minimum_weekly = 60
top_cow = None
top_total = 0

print(f"{'Cow':<8} {'Total':>8} {'Avg/wk':>8} {'Status':>15}")
print("-" * 40)
for cow in herd_data:
    total = sum(cow["yields"])
    avg = total / len(cow["yields"])
    status = "OK" if avg >= minimum_weekly else "NEEDS MORE ATTENTION"
    print(f"{cow['cow']:<8} {total:>8} {avg:>8.1f} {status:>15}")
    if total > top_total:
        top_total = total
        top_cow = cow["cow"]
print(f"\nTop producer : {top_cow} ({top_total} litres for over 4 weeks)")        