print("====EXERCICE 1 : File Writing====")

import tempfile, os
path = tempfile.mktemp(suffix='.txt')
with open (path, 'w') as f :

    f.write("Name : Moses\nCity : Nairobi\n")
with open(path) as f:
    print(f.read())


print("====EXERCISE 2 : Error Handling====")

def safe_dividing(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except ValueError as c:
        return f"Invalid input : {c}"

print (safe_dividing(10, 2))
print(safe_dividing(10, 0)) 


print("====EXERCISE 3 :JSON ====")

import json
data = {"name":"Moses","age":29,"city":"Kakamega"}
json_text = json.dumps(data, indent=2)
print(json_text)
parsed = json.loads(json_text)
print(f"Name: {parsed['name']}")

print("\n====EXERCISE 4 : CHALLANGE====")

import json, tempfile
students = [
    {"name":"Moses","score":85},
    {"name":"Hope","score":68},
    {"name":"Albert","score":92}
]
path = tempfile.mktemp(suffix='.json')
with open(path, 'w') as f :
    json.dump(students, f)
with open(path) as f :
    loaded = json.load(f)
    for s in loaded:
        if s ['score'] > 70 :
            print(f"{s['name']} : {s['score']}")


print("===EXERCISE 5: CAPENTRY WORKSHOP===")
import io

workshop_log ="""Monday,5,15
Tuesday,4,16
Wednesday,11,33
Thursday,8,24
Friday,12,36
"""
total_chairs = 0
total_timber = 0
days = 0

f = io.StringIO(workshop_log)
for line in f:
    line = line.strip()
    if line :
        day,chairs,timber = line.split(",")
        chairs = int(chairs)
        timber = int(timber)
        print(f"{day}:{chairs}chairs |{timber}m timber")
        total_chairs += chairs
        total_timber += timber
        days += 1
print(f"\nTotal chairs made :{total_chairs}")
print(f"\nTotal timber used : {total_timber}m")
print(f"Average chairs per day : {total_chairs // days}")        


print("===EXERCISE 6: DAIRY COW MILK LOG===")
import io

milk_log = """Estevao,6.8,7.4
Messi,8.5,9.2
Ronaldo,4.2,4.7
Palmer,7.5,8.2
Caisedo,9.4,10.2
"""
total_herd = 0
low_producers = []

f = io.StringIO(milk_log)
for line in f:
    line = line.strip()
    if line:
        name,morning,evening = line.split(",")
        daily = float(morning) + float(evening)
        status = "OK" if daily >= 12 else "LOW"
        print(f"{name}: {daily:.1f}litres [{status}]")
        total_herd += daily
        if daily <12 :
            low_producers.append(name)

print(f"\nHerd total : {total_herd:1f}litres")
print(f"Low producers : {','.join(low_producers) if low_producers else 'None'}")            