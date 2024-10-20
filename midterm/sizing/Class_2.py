import numpy as np


# Initial parameters
S_w = 138.85431  # [ft^2]
W_fw = 0  # [lb]
A = 10  # [-]
rho_cruise = 0.0764743  # [lb/ft^3]
V_cruise = 182.2688889  # [ft/s]
q = 0.5 * rho_cruise * V_cruise**2  # [lb/ft^2]
lambda_ = 1.4  # [-]
sweep = -0.043633231  # [rad]
N = 2.5  # [-] load factor
N_z = 1.5 * N  # [-] ultimate load factor
W_dg = 2407.44504  # [lb]
tc = 0.18  # [-] t/c ratio

# Horizontal Tail
S_ht = 29.44194249  # [ft^2]
Lambda_ht = -0.043633231  # [rad]
lambda_ht = -0.043633231  # [rad]

# Vertical tail
H_t = 5  # [ft]
H_v = 10  # [ft]
Svt = 32.11760562  # [ft^2]
Lambda_vt = -0.043633231  # [rad]
lambda_vt = 0.45  # [-]

# Fuselage group
S_f = 356  # [ft^2]
L_t = 13.6  # [ft]
LD_ratio = 11  # [-]
W_press = 70.40800462  # [lb]
V_pr = 182.27  # [ft/s]
P_delta = 8  # [lb/ft^2] Pressure differential

# Landing gear
N_l = 1.5  # [-]
W_l = 2166.7  # [lb]
L_m = 40  # [in]
L_n = 30  # [in]

# Engine group
W_en = 22.7  # [lb] engine weight
N_en = 2  # [-] number engines

# Flight control group
L = 22.637796  # [ft] Fuselage structural length
B_w = 37.401576  # [ft] Wingspan

# Hydraulic group
K_h = 0.05  # [-]
M = 0.165528298  # [-] Max design mach number

# Electrical group
W_fuelsystem = 120.37  # [lb] Fuel system weight
W_avionics = 1082.190746  # [lb] Weight of avionics

# Avionics group
W_uav = 800  # [lb] Uninstalled avionics weight

# Air conditioning anti-icing group
N_p = 4  # [-] number of personnel onboard (crew+passenger)
W_avionics = W_avionics  # [lb]
M = M  # Max design mach number (see Hydraulic group)

# Formulas


def wing_weight(S_w, W_fw, A, q, lambda_, sweep, N_z, W_dg, tc):
    """
    Calculates the weight of the wing.

    Parameters:
        S_w (float): Wing area [ft^2].
        W_fw (float): Fuel weight [lb].
        A (float): Aspect ratio.
        q (float): Dynamic pressure [lb/ft^2].
        lambda_ (float): Taper ratio.
        sweep (float): Wing sweep angle [rad].
        N_z (float): Load factor.
        W_dg (float): Design gross weight [lb].
        tc (float): Thickness-to-chord ratio.

    Returns:
        float: Weight of the wing [lb].
    """
    cos_sweep = np.cos(sweep)
    return 0.036 * S_w**0.758 * W_fw**0.0035 * (A / cos_sweep**2)**0.6 * q**0.006 * N_z**0.04 * W_dg**0.49 * (100 * tc)**-0.3


def horizontal_tail_weight(N_z, W_dg, q, S_ht, Lambda_ht):
    """
    Calculates the weight of the horizontal tail.

    Parameters:
        N_z (float): Load factor.
        W_dg (float): Design gross weight [lb].
        q (float): Dynamic pressure [lb/ft^2].
        S_ht (float): Horizontal tail area [ft^2].
        Lambda_ht (float): Horizontal tail sweep angle [rad].

    Returns:
        float: Weight of the horizontal tail [lb].
    """
    cos_Lambda_ht = np.cos(Lambda_ht)
    return 0.016 * (N_z * W_dg)**0.414 * q**0.168 * S_ht**0.896 * (A / cos_Lambda_ht**2)**0.043 * (1 / cos_Lambda_ht)**-0.02


def vertical_tail_weight(N_z, W_dg, q, Svt, Lambda_vt, H_v, tc):
    """
    Calculates the weight of the vertical tail.

    Parameters:
        N_z (float): Load factor.
        W_dg (float): Design gross weight [lb].
        q (float): Dynamic pressure [lb/ft^2].
        Svt (float): Vertical tail area [ft^2].
        Lambda_vt (float): Vertical tail sweep angle [rad].
        H_v (float): Vertical tail height [ft].
        tc (float): Thickness-to-chord ratio.

    Returns:
        float: Weight of the vertical tail [lb].
    """
    cos_Lambda_vt = np.cos(Lambda_vt)
    return 0.073 * (1 + 0.2 * H_v) * (N_z * W_dg)**0.376 * q**0.122 * Svt**0.873 * (A / cos_Lambda_vt**2)**0.039 * (100 * tc)**-0.49 * (1 / cos_Lambda_vt)**0.357


def fuselage_weight(N_z, W_dg, L_t, LD_ratio, q, W_press):
    """
    Calculates the weight of the fuselage.

    Parameters:
        N_z (float): Load factor.
        W_dg (float): Design gross weight [lb].
        L_t (float): Fuselage length [ft].
        LD_ratio (float): Lift-to-drag ratio.
        q (float): Dynamic pressure [lb/ft^2].
        W_press (float): Pressurization weight [lb].

    Returns:
        float: Weight of the fuselage [lb].
    """
    return 0.052 * (N_z * W_dg)**0.177 * L_t**0.51 * (L / LD_ratio)**-0.072 * q**0.241 + W_press


def main_landing_gear_weight(N_l, W_l, L_m):
    """
    Calculates the weight of the main landing gear.

    Parameters:
        N_l (float): Number of landing gears.
        W_l (float): Landing gear weight [lb].
        L_m (float): Main landing gear length [in].

    Returns:
        float: Weight of the main landing gear [lb].
    """
    return 0.095 * (N_l * W_l)**0.768 * (L_m / 12)**0.409


def nose_landing_gear_weight(N_l, W_l, L_n):
    """
    Calculates the weight of the nose landing gear.

    Parameters:
        N_l (float): Number of landing gears.
        W_l (float): Landing gear weight [lb].
        L_n (float): Nose landing gear length [in].

    Returns:
        float: Weight of the nose landing gear [lb].
    """
    return 0.125 * (N_l * W_l)**0.566 * (L_n / 12)**0.845


def installed_engine_weight(W_en, N_en):
    """
    Calculates the weight of the installed engine.

    Parameters:
        W_en (float): Engine weight [lb].
        N_en (float): Number of engines.

    Returns:
        float: Weight of the installed engine [lb].
    """
    return 2.575 * (W_en * N_en)**0.922


def fuel_system_weight(V_t, Vi, N_t, N_en):
    """
    Calculates the weight of the fuel system.

    Parameters:
        V_t (float): Total fuel volume [ft^3].
        Vi (float): Fuel volume index.
        N_t (float): Number of tanks.
        N_en (float): Number of engines.

    Returns:
        float: Weight of the fuel system [lb].
    """
    return 2.49 * (V_t + Vi / V_t)**0.242 * (N_t * N_en)**0.157


def flight_controls_weight(L, B_w, N_z, W_dg):
    """
    Calculates the weight of the flight controls.

    Parameters:
        L (float): Fuselage structural length [ft].
        B_w (float): Wingspan [ft].
        N_z (float): Load factor.
        W_dg (float): Design gross weight [lb].

    Returns:
        float: Weight of the flight controls [lb].
    """
    return 0.053 * L**1.536 * B_w**0.371 * (N_z * W_dg)**0.80


def hydraulics_weight(W_dg):
    """
    Calculates the weight of the hydraulics.

    Parameters:
        W_dg (float): Design gross weight [lb].

    Returns:
        float: Weight of the hydraulics [lb].
    """
    return 0.01 * W_dg**0.8 * M**0.5


def electrical_weight(W_fuelsystem, W_avionics):
    """
    Calculates the weight of the electrical system.

    Parameters:
        W_fuelsystem (float): Fuel system weight [lb].
        W_avionics (float): Weight of avionics [lb].

    Returns:
        float: Weight of the electrical system [lb].
    """
    return 12.57 * (W_fuelsystem + W_avionics)**0.51


def avionics_weight(W_uav):
    """
    Calculates the weight of the avionics.

    Parameters:
        W_uav (float): Uninstalled avionics weight [lb].

    Returns:
        float: Weight of the avionics [lb].
    """
    return 2.117 * W_uav**0.933


def air_conditioning_and_anti_ice_weight(W_dg, N_p, W_avionics):
    """
    Calculates the weight of the air conditioning and anti-ice systems.

    Parameters:
        W_dg (float): Design gross weight [lb].
        N_p (float): Number of personnel onboard.
        W_avionics (float): Weight of avionics [lb].

    Returns:
        float: Weight of the air conditioning and anti-ice systems [lb].
    """
    return 0.265 * W_dg**0.52 * N_p**0.68 * W_avionics**0.17 * M**0.08


def furnishings_weight(W_dg):
    """
    Calculates the weight of the furnishings.

    Parameters:
        W_dg (float): Design gross weight [lb].

    Returns:
        float: Weight of the furnishings [lb].
    """
    return 0.0582 * W_dg - 65

# Calculations
wing_w = wing_weight(S_w, W_fw, A, q, lambda_, sweep, N_z, W_dg, tc)
horizontal_tail_w = horizontal_tail_weight(N_z, W_dg, q, S_ht, Lambda_ht)
vertical_tail_w = vertical_tail_weight(N_z, W_dg, q, Svt, Lambda_vt, H_v, tc)
fuselage_w = fuselage_weight(N_z, W_dg, L_t, LD_ratio, q, W_press)
main_landing_gear_w = main_landing_gear_weight(N_l, W_l, L_m)
nose_landing_gear_w = nose_landing_gear_weight(N_l, W_l, L_n)
installed_engine_w = installed_engine_weight(W_en, N_en)
fuel_system_w = fuel_system_weight(V_pr, V_cruise, N_l, N_en)
flight_controls_w = flight_controls_weight(L, B_w, N_z, W_dg)
hydraulics_w = hydraulics_weight(W_dg)
electrical_w = electrical_weight(W_fuelsystem, W_avionics)
avionics_w = avionics_weight(W_uav)
air_conditioning_and_anti_ice_w = air_conditioning_and_anti_ice_weight(W_dg, N_p, W_avionics)
furnishings_w = furnishings_weight(W_dg)

# Print results
print(f"Wing weight: {wing_w:.2f} lb")
print(f"Horizontal tail weight: {horizontal_tail_w:.2f} lb")
print(f"Vertical tail weight: {vertical_tail_w:.2f} lb")
print(f"Fuselage weight: {fuselage_w:.2f} lb")
print(f"Main landing gear weight: {main_landing_gear_w:.2f} lb")
print(f"Nose landing gear weight: {nose_landing_gear_w:.2f} lb")
print(f"Installed engine weight: {installed_engine_w:.2f} lb")
print(f"Fuel system weight: {fuel_system_w:.2f} lb")
print(f"Flight controls weight: {flight_controls_w:.2f} lb")
print(f"Hydraulics weight: {hydraulics_w:.2f} lb")
print(f"Electrical weight: {electrical_w:.2f} lb")
print(f"Avionics weight: {avionics_w:.2f} lb")
print(f"Air conditioning and anti-ice weight: {air_conditioning_and_anti_ice_w:.2f} lb")
print(f"Furnishings weight: {furnishings_w:.2f} lb")
