junctions = [
    {
        "Junction ID": "J101",
        "Vehicle Count": 500,
        "Average Speed": 40,
        "Accident Count": 2,
        "Signal Delay": 30,
        "Pollution Index": 90,
        "Peak Hour Traffic": 600
    },
    {
        "Junction ID": "J102",
        "Vehicle Count": 700,
        "Average Speed": 35,
        "Accident Count": 5,
        "Signal Delay": 45,
        "Pollution Index": 120,
        "Peak Hour Traffic": 850
    },
    {
        "Junction ID": "J103",
        "Vehicle Count": 450,
        "Average Speed": 50,
        "Accident Count": 1,
        "Signal Delay": 20,
        "Pollution Index": 70,
        "Peak Hour Traffic": 500
    },
    {
        "Junction ID": "J104",
        "Vehicle Count": 900,
        "Average Speed": 30,
        "Accident Count": 6,
        "Signal Delay": 50,
        "Pollution Index": 140,
        "Peak Hour Traffic": 1000
    },
    {
        "Junction ID": "J105",
        "Vehicle Count": 650,
        "Average Speed": 45,
        "Accident Count": 3,
        "Signal Delay": 35,
        "Pollution Index": 100,
        "Peak Hour Traffic": 750
    }
]

# 1. Calculate Congestion Score
print("1. Congestion Score")
for j in junctions:
    congestion = (j["Vehicle Count"] * j["Signal Delay"]) / j["Average Speed"]
    j["Congestion Score"] = round(congestion, 2)
    print(j["Junction ID"], ":", j["Congestion Score"])

# 2. Rank Junctions
ranking = sorted(junctions, key=lambda x: x["Congestion Score"], reverse=True)

print("\n2. Junction Rankings")
for i, j in enumerate(ranking, 1):
    print(i, j["Junction ID"], "-", j["Congestion Score"])

# 3. Accident-Prone Areas
print("\n3. Accident-Prone Areas")
for j in junctions:
    if j["Accident Count"] >= 5:
        print(j["Junction ID"])

# 4. Heavily Polluted Junctions
print("\n4. Heavily Polluted Junctions")
for j in junctions:
    if j["Pollution Index"] > 100:
        print(j["Junction ID"])

# 5. City Average Congestion
average = sum(j["Congestion Score"] for j in junctions) / len(junctions)

print("\n5. City Average Congestion")
print(round(average, 2))

# 6. Busiest Junction
busiest = max(junctions, key=lambda x: x["Peak Hour Traffic"])

print("\n6. Busiest Junction")
print(busiest["Junction ID"], "-", busiest["Peak Hour Traffic"])

# 7. Generate Traffic Alerts
print("\n7. Traffic Alerts")

alerts = []

for j in junctions:
    if j["Congestion Score"] > 800:
        alert = f"{j['Junction ID']} : Heavy Traffic"
        alerts.append(alert)
        print(alert)

# 8. Save Alerts to File
with open("traffic_alerts.txt", "w") as file:
    file.write("Traffic Alerts\n\n")
    for alert in alerts:
        file.write(alert + "\n")

print("\n8. Alerts Saved Successfully")

# 9. Sort Junctions
sorted_junctions = sorted(junctions, key=lambda x: x["Junction ID"])

print("\n9. Sorted Junctions")
for j in sorted_junctions:
    print(j["Junction ID"])

# 10. Top 5 Congestion Points
print("\n10. Top 5 Congestion Points")
for j in ranking[:5]:
    print(j["Junction ID"], "-", j["Congestion Score"])

print("\nReading Alerts File\n")

with open("traffic_alerts.txt", "r") as file:
    print(file.read())