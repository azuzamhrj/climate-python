
# ════════════════════════════════════════
# SESSION 1: Basic Python
# ════════════════════════════════════════
#June 30
# ... session 1 code ...
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


# ── EXERCISE 2: Lists and loops
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



# ════════════════════════════════════════
# SESSION 2: Pandas
# ════════════════════════════════════════
  #July 1 

    # ── EXERCISE 1: Create a DataFrame ────────────────────────────
# A DataFrame is like a spreadsheet table — rows and columns
# Here we build one from our heatwave data manually
import pandas as pd
data = {
    "city": ["Paris", "Berlin", "Madrid", "London", "Amsterdam"],
    "country": ["France", "Germany", "Spain", "UK", "Netherlands"],
    "peak_2026": [44.3, 41.5, 43.1, 37.8, 34.0],
    "june_average": [24.5, 23.1, 31.2, 21.3, 22.0],
}
df = pd.DataFrame(data) 
print("=== Our DataFrame ===") 
print(df) 
#here the data block helps other things such as cities countries become column headers
#here df is just data frame short and pd.DataFrame is panda installations that takes the dictonary into proper table form
#=== is not needed just for decorative purposes 
#print df --column headers would be ones on the left and row headers on the right automatically


# ── EXERCISE 2: Add a new column ───────────────────────────────
# You can do math across whole columns at once — no loop needed

df["anomaly"] = df["peak_2026"] - df["june_average"]
print("\n=== With Anomaly Column ===")
print(df)
#"\n===" asks for a line break purely visual can be done without

# ── EXERCISE 3: Filter rows 
# Like asking "show me only the rows where anomaly is above 15"
extreme = df[df["anomaly"] >= 15]
print("\n=== Cities with anomaly above 15°C ===")
print(extreme)

#here we are creating a new variable extreme without changing the anomaly df,extreme will have only those values >=15

# ── EXERCISE 4: Sort and rank 
# Sort by anomaly, biggest first

ranked = df.sort_values("anomaly", ascending=False)
print("\n=== Cities ranked by heat anomaly ===")
print(ranked[["city", "peak_2026", "anomaly"]])

#sort_values is a function we are calling this in df df.sort_values (where- in the anomaly column, ascending = Fase will start biggest value first, if true smallest would be first)
#here print(ranked [["cities", "peak_2026", "anomaly"]]) we are choosing to only show three columns and no june average temp. 

# ── EXERCISE 5: Save to CSV 
# Export your results as a real file you can open in Excel

ranked.to_csv("heatwave_results.csv", index=False)
print("\n✓ Saved to heatwave_results.csv")
#.to_csv saves the ranked column to excel sheet index=False means "don't include that row number column in the file