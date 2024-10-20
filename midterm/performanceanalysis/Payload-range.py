import matplotlib.pyplot as plt
#Parameters
m_TO = 1092 #kg
m_OE = 672 #kg
m_PLmax = 420 # kg
LD = 15
E_sb = 235 #Wh/kg
eta_b = 0.9
eta_p = 0.8
m_b = 71.3 #kg
g = 9.81 #N/kg

#Range diagram
Rlst = [0]
m_PLlst = [420]
for i in range(0, 421,1):
    m_PL = m_PLmax - i
    m = m_OE + m_PL
    print(m)
    R = 3.6 * LD * E_sb * eta_b * eta_p * m_b / g / m
    print(R)
    m_PLlst.append(m_PL)
    Rlst.append(R)

plt.title("Payload-Range diagram")
plt.plot(Rlst, m_PLlst)
plt.xlabel("Range [km]")
plt.ylabel("Payload [kg]")
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.show()


