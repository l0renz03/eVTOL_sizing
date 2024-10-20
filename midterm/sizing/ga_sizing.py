import numpy as np

range = 50  # km
cruise_speed = 200  # km/h
cruise_speed_mps = cruise_speed * 1000 / 3600  # m/s
cruise_endurance = range / cruise_speed * 3600  # s
loiter_endurance = 10 * 60  # s
stall_speed = 25  # m/s
takeoff_speed = 1.21 * stall_speed  # m/s
loiter_speed = cruise_speed_mps  # m/s
energy_density = 235  # Wh/kg
sys_eff = 0.9
prop_eff = 0.8
L_D = 15
g = 9.81  # m/s^2
Vv = 500 * 0.3048 / 60  # m/s (500 ft/min as specified in Uber report)
h = 1500 * 0.3048  # m (1500 ft as specified in Uber report)
m = 1500  # kg
payload = 420  # kg
oew_ratio = 0.55
m_step = 0  # kg
loiter_bmf = (loiter_endurance / 3600 * loiter_speed * g) / (3.6 * energy_density * sys_eff * prop_eff * L_D)
cruise_bmf = (range * g) / (3.6 * energy_density * sys_eff * prop_eff * L_D)
total_bmf = loiter_bmf + cruise_bmf
rpm = 2000  # RPM


def get_take_off_power(cruise_mass):
    """
    Calculate takeoff power with propeller efficiency applied
    :param cruise_mass: Cruise mass in kg
    :return: Takeoff power in W
    """
    mass_with_lifting_factor = 1.8
    tol = 500  # m
    t = 25  # s
    v_dot = 2 * tol / t ** 2
    thrust = mass_with_lifting_factor * v_dot * cruise_mass
    return thrust * takeoff_speed / prop_eff


def get_cruise_power(cruise_mass):
    """
    Calculate cruise power with propeller efficiency applied
    :param cruise_mass: Cruise mass in kg
    :return: Cruise power in W
    """
    return (cruise_mass * g) / L_D * cruise_speed_mps / prop_eff


def get_propeller_diameter(cruise_mass):
    """
    Calculate propeller diameter for cruise and takeoff
    :param cruise_mass: Cruise mass in kg
    :return: Propeller diameter in m
    """
    rho_cruise = 1.121  # kg/m^3 (density of air at 3000 ft)
    thrust_cruise = get_cruise_power(cruise_mass) / cruise_speed_mps
    thrust_takeoff = get_take_off_power(cruise_mass) / takeoff_speed
    cruise_area = thrust_cruise ** 3 / (2 * rho_cruise * (get_cruise_power(cruise_mass) * prop_eff) ** 2)
    takeoff_area = thrust_takeoff ** 3 / (2 * rho_cruise * (get_take_off_power(cruise_mass) * prop_eff) ** 2)
    area = max(cruise_area, takeoff_area)
    return (4 * area / np.pi) ** 0.5


def get_spl_at_distance(distance, engine_power, propeller_diameter, rpm, prop_number, blades_number):
    """
    Calculate sound pressure level at a given distance
    :param distance: Distance from the source in m
    :param engine_power: Engine power in W
    :param propeller_diameter: Propeller diameter in m
    :param rpm: Rotations per minute
    :param prop_number: Number of propellers
    :param blades_number: Number of blades per propeller
    :return: Sound pressure level in dB
    """
    # propeller_diameter = 75 * 0.0254
    M_t = np.pi * propeller_diameter * rpm / (60 * 340.3)
    return (83.4 + 15.3 * np.log10(engine_power) - 20 * np.log10(propeller_diameter) + 38.5 * M_t -
            3 * (blades_number - 2) + 10 * np.log10(prop_number) - 20 * np.log10(distance))


P_climb = None
while abs(m - m_step) > 0.01 * m:
    m_step = m
    P_climb = 0.85 * get_take_off_power(m)  # Assuming maximum continuous power is 85% of takeoff power
    climb_bmf = (P_climb / 1000 * h) / (3.6 * Vv * energy_density * sys_eff * L_D * 0.866 * m)
    total_bmf = loiter_bmf + cruise_bmf + climb_bmf
    m = payload / (1 - total_bmf - oew_ratio)
    oew_ratio = (m - payload - total_bmf * m) / m

print(f"Takeoff weight: {m:.2f} kg")
print(f"Empty weight: {oew_ratio * m:.2f} kg")
print(f"Battery weight: {total_bmf * m:.2f} kg")
print(f"OEW ratio: {oew_ratio:.2f}")
print(f"Takeoff power: {get_take_off_power(m):.2f} W")
print(f"Climb power: {P_climb:.2f} W")
print(f"Cruise power: {get_cruise_power(m):.2f} W")
print(f"Propeller diameter: {get_propeller_diameter(m):.2f} m")
print(f"Energy used total: {total_bmf * m * energy_density:.2f} Wh")
print(f"Energy used for cruise: {cruise_bmf * m * energy_density:.2f} Wh")
print(f"Energy used for cruise: {cruise_bmf * m * energy_density * 3600 / 1e6:.2f} MJ")
print(f"Energy used for mission: {total_bmf * m * energy_density * 3600 / 1e6:.2f} MJ")
print(f"Energy used for loiter: {loiter_bmf * m * energy_density:.2f} Wh")
print(f"Energy used for climb: {climb_bmf * m * energy_density:.2f} Wh")
sound_pressure_level = get_spl_at_distance(100, get_take_off_power(m), get_propeller_diameter(m), rpm, 1, 3)
print(f"Sound pressure level at 100 m: {sound_pressure_level:.2f} dB")

energy_10k = m * g / L_D * 100 / 3.6 / prop_eff * 10 / 100 * 3600
print(f"Energy used for 10 km: {energy_10k / 1e6 + loiter_bmf * m * energy_density * 3600 / 1e6:.2f} MJ")