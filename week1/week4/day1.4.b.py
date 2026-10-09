import io
farm_log = """Pen A, 240, 12
Pen B, 185, 10
Pen C, 310, 15
Pen D, 92, 8
Pen E, 275, 13
"""
total_eggs = 0
total_feed = 0
low_pens = []

f = io.StringIO(farm_log)
for line in f :
    line = line.strip()
    if line:
        pen,eggs,feed = line.split(",")
        eggs = int(eggs)
        feed = int(feed)
        efficiency = eggs / feed
        status = "Good" if eggs >=200  else "Low yield"
        print(f"{pen}:{eggs} | {feed}kg | {efficiency : .1f}eggs/kg [{status}]")
        total_eggs += eggs
        total_feed += feed
        if eggs < 200:
            low_pens.append(pen)

print(f"\nTotal eggs : {total_eggs}")
print(f"Total feeds used : {total_feed}kg")
print(f"Pens needing attension : {','.join(low_pens)}")            