import numpy as np
import math
#Parameters
rho = 1.225 #density kg/m^3
P_max = 107000 #Maximum power W
P_max_lv = 320000 #W
V = 200/3.6 #m/s
V_lv = 30 #m/s
T = P_max / V #Thrust N
T_lv = P_max_lv / V_lv #Thrust N
eta_prop = 0.8 #propeller efficiency
FM = 0.7
N = 2#amount of rotors cruise vehicle
N_lv = 5 #Amount of rotors lifting vehicle
m = 1 #order of the harmonic
B = 5 #blade number
B_lv = 5 #blade number
P_h = 0.00134102 * P_max #horsepower
P_h_lv = 0.00134102 * P_max #horsepower
T_lb = 0.2248 * T #Thrust lb
T_lb_lv = 0.2248 * T_lv #Thrust lb
S =  328 * 12 #Distance from propeller hub to observer ft
S_lv = 328 * 5   #ft
M_t = 0.6 #tip mach number
M_t_lv = 0.6
tetha = np.pi / 2  #angle of forward propeller axis to observer
x = 0.8 * M_t * m * B * np.sin(tetha) #argument of Bessel function
x_lv = 0.8 * M_t_lv * m * B_lv * np.sin(tetha) #argument of Bessel function

#Calculation for cruise vehicle
A = ((T ** 3 / 2 / rho / (P_max * eta_prop) ** 2 ) * 10.7639) / N #Propeller disk area ft^2
R = (A / np.pi) ** 0.5 #Propeller radius ft
    #Bessel function
J_mb = 0
for k in range(0, 10, 1):
    J_mb = J_mb + (-1) ** k / (math.factorial(k) * math.factorial(k + B)) * (x / 2) ** (2 * k * B)
p_m = (169.3 * m * B * R * M_t / S / A * (0.76 * P_h / (M_t) ** 2 - T_lb * np.cos(tetha)) * J_mb) * N
p_pascal = p_m * 0.1 #Pressure in pascal
SPL = 10 * np.log(p_pascal/0.000020) #in dB
print("The cruise vehicle produces",SPL,"dB at a distance of",S * 0.3048,"m")

#Calculation for lifting vehicle
A_lv = ((T_lv ** 3 / 2 / rho / (P_max_lv * FM) ** 2 ) * 10.7639) / N #Propeller disk area ft^2
R_lv = (A_lv / np.pi) ** 0.5 #Propeller radius ft
J_mb_lv = 0
for i in range(0, 10, 1):
    J_mb_lv = J_mb_lv + (-1) ** i / (math.factorial(i) * math.factorial(i + B_lv)) * (x_lv / 2) ** (2 * i * B_lv)
p_mlv = (169.3 * m * B_lv * R_lv * M_t_lv / S_lv / A_lv * (0.76 * P_h_lv / (M_t) ** 2 - T_lb_lv * np.cos(tetha)) * J_mb_lv) * N_lv
p_pascal_lv = p_mlv * 0.1 #Pressure in pascal
SPL_lv = 10 * np.log(p_pascal_lv/0.000020) #in dB
print("The lifting vehicle produces",SPL_lv,"dB at a distance of",S_lv * 0.3048,"m")

#Calculation for Joby vehicle
P_h_joby = 560 #horsepower
P_max_joby = P_h_joby / 0.00134102
N_joby = 12
V_joby = 200 / 3.6
T_joby = P_max_joby / V_joby
T_lb_joby = 0.2248 * T_joby
B_joby = 5
M_t_joby = 0.34 #tip mach number
x_joby = 0.8 * M_t_joby * m * B_joby * np.sin(tetha) #argument of Bessel function
A_joby = ((T_joby ** 3 / 2 / rho / (P_max_joby * FM) ** 2 ) * 10.7639) / N #Propeller disk area ft^2
R_joby = (A_joby / np.pi) ** 0.5 #Propeller radius ft
J_mb_joby = 0
for j in range(0, 10, 1):
    J_mb_joby = J_mb_joby + (-1) ** j / (math.factorial(j) * math.factorial(j + B_joby)) * (x_joby / 2) ** (2 * j * B_joby)
p_m_joby = (169.3 * m * B_joby * R_joby * M_t_joby / S_lv / A_joby * (0.76 * P_h_joby / (M_t_joby) ** 2 - T_lb_joby * np.cos(tetha)) * J_mb_joby) * N
p_pascal_joby = p_m_joby * 0.1 #Pressure in pascal
SPL_joby = 10 * np.log(p_pascal_joby/0.000020) #in dB
print("The Joby vehicle produces",SPL_joby,"dB at a distance of",S * 0.3048,"m")