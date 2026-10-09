print("----EXERCISE 1: HTTP REQUESTS----")

import urllib.request, json
#Fetch public API and print the response.
url = "https://httpbin.org/json"
with urllib.request.urlopen(url) as response:
    data = json.loads(response.read())
print(json.dumps(data, indent = 2)) 

print("----EXERCISE 2: PARSING JSON----")
import json
#Parse this nested JSON and print the author and tittle.
response = '{"book":{"tittle":"Clean code","author":"Robert Martin","year":2008}}'
data = json.loads(response)
book = data["book"]
print(f"Tittle : {book['tittle']}")
print(f"Author : {book['author']}")

print("\n----EXERCISE 3: HEADERS AND AUTHENTICATION----")
import urllib.request, json
#Make a request with a custom header.
req = urllib.request.Request(
    "https://httpbin.org/headers",
    headers = {"X-Custom-Header":"AmerixMasterclass"}
)
with urllib.request.urlopen(req) as r:
    data = json.loads(r.read())
    print(data["headers"])

print("\n----EXERCISE 4: CHALLANGE----")
import urllib.request,json
#Fetch a joke from a public API and print it.
url = "https://official-joke-api.appspot.com/random_joke"
try:
    with urllib.request.urlopen(url, timeout=5) as r:
        joke = json.loads(r.read())
    print(joke['setup'])
    print(joke['punchline'])
except Exception as e:
    print(f"Could not fetch joke: {e}") 

print("\n----EXERCISE 5: WELDING JOB QUOTE----")
import json
#Simulated response from a steel supplier.
response_text = '''
{
    "supplier":"Nairobi Steel Ltd",
    "date":"2026-07-27",
    "prices":{
        "mild_steel_sheet":6000,
        "angle_iron":3200,
        "square_tube":4200
    },
    "currency": "KES",
    "unit":"per metre"
}
'''

data = json.loads(response_text)

print(f"Supplier: {data['supplier']}")
print(f"Date: {data['date']}")
print(f"\nSteel prices ({data['currency']} {data['unit']}):")
for item, price in data["prices"].items():
    print(f"  {item.replace('_','').title()}:KES {price:,}")

#One steel door frame: 3 pieces of angle iron (2m each) + 1 mild steel sheet
angle_cost = data["prices"]["angle_iron"] * 2 * 3
sheet_cost = data["prices"]["mild_steel_sheet"]
frame_cost = angle_cost + sheet_cost

print(f"\nDoor frame quote:")
print(f" Angle iron (3 x 2m): KES {angle_cost:,}")
print(f" Mild steel sheet: KES {sheet_cost:,}")
print(f" Total: KES {frame_cost:,}")

print("\n---EXERCISE 6: FARM CROP MARKET PRICE CHECKER---")

import json

#Simulated crop market API response.
response_text = '''
{
    "market":"Wakulima farm Market, Kisumu",
    "date":"2026-09-02,
    "prices_per_bag_kes": {
        "maize":3800,
        "beans":9200,
        "wheat":5500,
        "sorghum":3200
    },
    "bag_weight_kg": 90
}
'''
#Farmer's current stock in bags
stock = {"maize":12, "beans":5, "wheat":8, "sorghum":20}
data = json.loads(response_text)

print(f"Market: {data['market']}")
print(f"Date:  {data['date']}\n")
print("Crop Valuation:")
print("-" * 40)

total_value = 0
for crop, bags in stock.items():
    price = data["prices_per_bag_kes"][crop]
    value = bags * price
    print(f"{crop.title()}: {bags} bags x KES {price:,} = KES {value:,}")
    total_value += value

print(f"\nTotal current stock value: KES {total_value:,}")
