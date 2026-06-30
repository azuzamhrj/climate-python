# ── EXERCISE 1: Variables ──────────────────────────────────────
paris = 44.3
berlin = 41.5
madrid = 43.1
london = 37.8
tubingen = 38.5

print("=== Peak Temperatures ===")
print("Paris:", paris, "°C")
print("Berlin:", berlin, "°C")
print("Madrid:", madrid, "°C")
print("London:", london, "°C")
print("Tübingen:", tubingen, "°C")


# ── EXERCISE 2: Lists and loops ────────────────────────────────
cities = ["Paris", "Berlin", "Madrid", "London", "Amsterdam"]
temps = [44.3, 41.5, 43.1, 37.8, 34.0]

print("\n=== Cities above 40°C ===")
for i in range(len(cities)):
    if temps[i] >= 40:
        print(cities[i], "EXTREME HEAT:", temps[i], "°C")
    else:
        print(cities[i], "hot but below 40°C:", temps[i], "°C")


# ── EXERCISE 3: Dictionary ─────────────────────────────────────
heatwave_data = {
    "Paris": {"temp": 44.3, "country": "France"},
    "Berlin": {"temp": 41.5, "country": "Germany"},
    "Madrid": {"temp": 43.1, "country": "Spain"},
    "London": {"temp": 37.8, "country": "UK"},
}

print("\n=== City Details ===")
for city, info in heatwave_data.items():
    print(city, "(", info["country"], "):", info["temp"], "°C")


# ── EXERCISE 4: Function ───────────────────────────────────────
june_averages = {
    "Paris": 24.5,
    "Berlin": 23.1,
    "Madrid": 31.2,
    "London": 21.3,
}

def heat_anomaly(city, peak_temp):
    baseline = june_averages[city]
    anomaly = peak_temp - baseline
    return round(anomaly, 1)

print("\n=== Heat Anomalies ===")
for city, info in heatwave_data.items():
    anomaly = heat_anomaly(city, info["temp"])
    print(city, ": +", anomaly, "°C above the June average")