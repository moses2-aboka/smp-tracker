logs = [
    {"name":"James Omondi","steps":9200,"protocol":"OMAD"},
    {"name":"Sandra Weru","steps":10500,"protocol":"2MAD"},
    {"name":"Patrick Njiru","steps":8100,"protocol":"OMAD"},
    {"name":"Grace Achieng","steps":11000,"protocol":"OMAD"},
    {"name":"Brian Kamau","steps":7400,"protocol":"2MAD"},
    {"name":"Kevin Mwangi","steps":10800,"protocol":"OMAD"},
]
goal_hitters = [
    r for r in logs
    if r["protocol"]=="2MAD" and r["steps"] >=8000
]
print("2MAD users who hit 8k steps:")
for r in goal_hitters:
    print(f"{r['name']} : {r['steps']}steps")
