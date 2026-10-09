import json

week_report = {
    "name": "Moses",
    "steps":[10500, 8400, 9800, 7800, 11000],
    "protocols":["2MAD", "OMAD", "2MAD", "OMAD", "Autophagy Marathon"]
}

json_str = json.dumps(week_report, indent = 2)
print("JSON output :")
print(json_str)


loaded = json.loads(json_str)
avg = sum(loaded["steps"]) / len(loaded["steps"])
print(f"\nAverage steps for{loaded['name']}: {round(avg)}")