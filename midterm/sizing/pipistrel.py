cruise_speed = 46.3  # m/s
cruise_power = 49.2e3  # W
battery_capacity = 24.8e3  # Wh
energy_density = 150  # Wh/kg
battery_weight = battery_capacity / energy_density
print(battery_weight)
mtow = 600
payload = 172
oew = mtow - battery_weight - payload
print(oew)
print(oew / mtow)
