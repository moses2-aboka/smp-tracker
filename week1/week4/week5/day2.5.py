commodity_response = {
    "status":"ok",
    "market":"Wakulima market, Nairobi",
    "date":"2026-08-13",
    "prices":[
        {"commodity":"Maize","unit":"90kg bag","price_kes":3200,"change_pct":-2.1,"available":True},
        {"commodity":"Beans(Dry)","unit":"90kg bag","price_kes":9800,"change_pct":4.5,"available":True},
        {"commodity":"Milk(Raw)","unit":"litre","price_kes":62,"change_pct":1.2,"available":True},
        {"commodity":"Tea leaf","unit":"kg","price_kes":28,"change_pct":-0.8,"available":False},
        {"commodity":"Wheat flour","unit":"50kg bag","price_kes":2900,"change_pct":0.0,"available":True},
    ]
}
market = commodity_response["market"]
date = commodity_response["date"]
clean = [
  {
    {"commodity": item["commodity"]},
    {"unit": item["unit"]},
    {"price_kes": item["price_kes"]}
  }
  for item in commodity_response if item["available"]
]
for item in clean :
 print(f"Market : {market}  | Date : {date}")
print("-"* 55)
print(f"{'Commodity':<15}{'Unit':<12}{'Price(KES)':>12}")
print("-"* 55)

for item in commodity_response["prices"]["available"]:
   if item == True:
    print(f"{item['commodity']:<15} {item['unit']:<12} {item['price_kes']:>12,}")               