import matplotlib.pyplot as plt
import numpy as np
#Parameters
eta_p = 0.8
g = 9.81 #N/kg
S = 14.3 #m^2
CLmax = 1.8
rho = 1.225 #kg/m^3
LD = 15
a_HTO = 1.6 #m/s^2
P_max_cv = 107000 #W
V_stall = 70 / 3.6 #m/s
V_TO = 1.15 * V_stall #m/s
m_lv = 761 #kg
m_cv = 1092 #kg
v_cvTO = 1.15 * (2*m_cv*g/rho/CLmax/S)**0.5 #m/s
t_VTO = 100 #s

#Lift analysis
L_VTO_lv = (m_lv + m_cv) * g #N
L_HTO_lvlst = [L_VTO_lv] #N
L_HTO_cvlst = [0]
t_lst = [0]
for t in range(101,200,1):
    t_lst.append(t)
    v = a_HTO * (t - t_VTO) #m/s
    L_HTO_cv = 0.5 * rho * S * CLmax * v ** 2 #N
    L_HTO_lv = L_VTO_lv - L_HTO_cv #N
    if L_HTO_lv < (m_lv * g):
        L_HTO_lv = m_lv * g
    if L_HTO_cv > (m_cv * g):
        L_HTO_cv = m_cv * g
        t_HTO = t
    L_HTO_lvlst.append(L_HTO_lv)
    L_HTO_cvlst.append(L_HTO_cv)

#Flight profile diagram
#Parameters
ROD = 9 #m/s
ROC = 5 #m/s
h_cruise = 1200 #m
s_HTO = 500 #m
a_HTO = 1.6 #m/s^2
a_VTO = 2 #m/s^2
V_max_VTO = 5 #m/s chosen

#calculations takeoff + climb
#horizontal takeoff
t_HTO = v_cvTO / a_HTO
#vertical takeoff
t_VTO = 100 - t_HTO
h_VTO = 2 * a_VTO ** 2 + V_max_VTO * t_VTO
#climb
V_climb = ((eta_p / g * P_max_cv / m_cv - ROC) * 3.6 * LD) / 3.6 #m/s
angle_climb = np.arcsin(ROC/V_climb) #radians
t_climb = (h_cruise - h_VTO) / ROC #s
Delta_v_climb = V_climb - 1.15 * V_stall #m/s
t_climb_acc = Delta_v_climb / a_HTO #s
d_climb_acc = 0.5 * a_HTO * (t_climb_acc) ** 2 + 1.15 * V_stall * t_climb_acc #m
#print("s_climb_acc is", s_climb_acc)
#h_climb_acc =
#t_climb_rest =
s_climb = ((V_climb ** 2 - (ROC) ** 2))**0.5 * t_climb
#calculations descent + landing
#horizontal landing
s_HL = 500
a_HL = 1.6
t_HL = v_cvTO / a_HL
#vertical landing
a_VL = 1.9
V_maxVL = 6 #chosen
t_VL = 100 - t_HL
h_VL = 2 * a_VL ** 2 + V_maxVL * t_VL
#descent
angle_descent = 12 /180 * np.pi
h_descent = h_cruise - h_VL
t_descent = h_descent / ROD
s_descent = h_descent / np.sin(angle_descent)
#plotting
s_cruise = 50000 - s_HTO - s_climb - s_descent - s_HL
h_lst = [0, h_VTO, h_VTO, h_cruise, h_cruise, h_VL, h_VL, 0, 0]
s_lst = [0,0.1,s_HTO, s_climb + s_HTO, s_cruise, s_descent + s_cruise + s_climb + s_HTO, s_HL + s_cruise + s_climb + s_HTO + s_descent, 49999.5, 50000]
plt.plot(s_lst, h_lst)
plt.show()
print(h_VTO, h_VL)

plt.plot(t_lst, L_HTO_lvlst, label = "Lifting vehicle")
plt.plot(t_lst, L_HTO_cvlst, label = "Cruise vehicle")
plt.xlabel("time [s]")
plt.ylabel("Lift [N]")
plt.legend(loc="upper right")
plt.title("Lift analysis")
plt.show()

print(t_VTO, t_HTO, t_climb, t_descent, t_HL, t_VL)
print(h_VTO, s_HTO, s_climb, s_cruise, s_descent, s_HL, h_VL)