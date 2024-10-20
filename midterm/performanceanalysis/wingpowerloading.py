import numpy as np
import matplotlib.pyplot as plt

Vstall = 31
CLmax = 1.8
altitude = 1200
rho0 = 1.225
T0 = 288.15
g0=9.81
labda = -0.0065
R = 287.05
TOP = 160 #for 500 m take-off
sland = 500
CD0=0.03
e=0.8
rotoreff = 0.8
AR1 = 8
AR2 = 10
AR3 = 12
Vcruise = 200/3.6
roc = 5
CLcg = 1.6
climbgrad = 0.083

rho = rho0* (1 + labda*altitude/T0)**-(g0/(R*labda)+1)

wingloadinglist = np.arange(0.001,1600,0.1)
wingloadingstall = 0.5 * rho * Vstall**2 * CLmax
wingloadingstalllist = wingloadingstall * np.ones(len(wingloadinglist))
powerloadinglist = np.arange(0,1600,0.1)
CLTO = [0.88*CLmax/1.1**2,CLmax/1.1**2,1.15*CLmax/1.1**2]

powerloadingCL1 = TOP/wingloadinglist * CLTO[0] * rho/rho0
powerloadingCL2 = TOP/wingloadinglist * CLTO[1] * rho/rho0
powerloadingCL3 = TOP/wingloadinglist * CLTO[2] * rho/rho0

wingloadinglanding1 = CLmax*rho*sland/0.5915/2 *np.ones(len(wingloadinglist))
wingloadinglanding2 = 0.9*CLmax*rho*sland/0.5915/2 * np.ones(len(wingloadinglist))
wingloadinglanding3 = 1.1*CLmax*rho*sland/0.5915/2 * np.ones(len(wingloadinglist))

powerloadingcruise1 = rotoreff * (rho/rho0)**(3/4) * (CD0*0.5*rho*Vcruise**3/wingloadinglist + wingloadinglist / (np.pi * AR1 * e * 0.5 * rho * Vcruise))**-1
powerloadingcruise2 = rotoreff * (rho/rho0)**(3/4) * (CD0*0.5*rho*Vcruise**3/wingloadinglist + wingloadinglist / (np.pi * AR2 * e * 0.5 * rho * Vcruise))**-1
powerloadingcruise3 = rotoreff * (rho/rho0)**(3/4) * (CD0*0.5*rho*Vcruise**3/wingloadinglist + wingloadinglist / (np.pi * AR3 * e * 0.5 * rho * Vcruise))**-1

powerloadingroc1 = rotoreff/(roc+np.sqrt(wingloadinglist*2/rho)/(1.345*(AR1*e)**0.75/CD0**0.25))
powerloadingroc2 = rotoreff/(roc+np.sqrt(wingloadinglist*2/rho)/(1.345*(AR2*e)**0.75/CD0**0.25))
powerloadingroc3 = rotoreff/(roc+np.sqrt(wingloadinglist*2/rho)/(1.345*(AR3*e)**0.75/CD0**0.25))

powerloadingclimbgrad1 = rotoreff/(np.sqrt(wingloadinglist)*(climbgrad+(CD0+CLcg**2/(np.pi*AR1*e)/CLcg))*np.sqrt(2/rho/CLcg))
powerloadingclimbgrad2 = rotoreff/(np.sqrt(wingloadinglist)*(climbgrad+(CD0+CLcg**2/(np.pi*AR2*e)/CLcg))*np.sqrt(2/rho/CLcg))
powerloadingclimbgrad3 = rotoreff/(np.sqrt(wingloadinglist)*(climbgrad+(CD0+CLcg**2/(np.pi*AR3*e)/CLcg))*np.sqrt(2/rho/CLcg))

plt.plot(wingloadingstalllist,powerloadinglist,label='stall')
plt.plot(wingloadinglist,powerloadingCL1,label='TO at CLmax = 1.3')
plt.plot(wingloadinglist,powerloadingCL2,label='TO at CLmax = 1.5')
plt.plot(wingloadinglist,powerloadingCL3,label='TO at CLmax = 1.7')
plt.plot(wingloadinglanding2,powerloadinglist,label='landing at CLmax = 1.6')
plt.plot(wingloadinglanding1,powerloadinglist,label='landing at CLmax = 1.8')
plt.plot(wingloadinglanding3,powerloadinglist,label='landing at CLmax = 2.0')
plt.plot(wingloadinglist,powerloadingcruise1,label='cruise at A = 8')
plt.plot(wingloadinglist,powerloadingcruise2,label='cruise at A = 10')
plt.plot(wingloadinglist,powerloadingcruise3,label='cruise at A = 12')
plt.plot(wingloadinglist,powerloadingroc1,label='optimal roc at A = 8')
plt.plot(wingloadinglist,powerloadingroc2,label='optimal roc at A = 10')
plt.plot(wingloadinglist,powerloadingroc3,label='optimal roc at A = 12')
plt.plot(wingloadinglist,powerloadingclimbgrad1,label='optimal roc/V at A = 8')
plt.plot(wingloadinglist,powerloadingclimbgrad2,label='optimal roc/V at A = 10')
plt.plot(wingloadinglist,powerloadingclimbgrad3,label='optimal roc/V at A = 12')
intersec1 = np.argwhere(np.diff(np.sign(powerloadingcruise1 - powerloadingroc1))).flatten()
intersec2 = np.where(np.abs(wingloadinglist - wingloadinglanding2) <= 0.05)[0]
intersec3 = np.where(np.abs(wingloadinglist - wingloadinglanding3) <= 0.05)[0]
plt.fill_between(wingloadinglist[0:(intersec1[0]-50)],powerloadingcruise1[0:(intersec1[0]-50)],color='green',alpha=0.2)
plt.fill_between(wingloadinglist[intersec1[0]:intersec2[0]],powerloadingroc1[intersec1[0]:intersec2[0]],color='green',alpha=0.2)
plt.fill_between(wingloadinglist[intersec2[0]:intersec3[0]],powerloadingroc1[intersec2[0]:intersec3[0]],color='green',alpha=0.09)
intersec4 = np.where(np.abs(wingloadinglist - wingloadinglanding1) <= 0.05)[0]
plt.scatter(wingloadinglanding1[0],powerloadingroc1[intersec4],marker='o',alpha=1,c='black',s=80,zorder=10)
plt.xlabel('W/S [N/m^2]')
plt.ylabel('W/P [N/W]')
plt.xlim(-100,1600)
plt.ylim(0,0.5)
plt.legend(loc='upper center', bbox_to_anchor=(0.65, 1.01),
          ncol=2, fancybox=True, shadow=True)
plt.title('Wing/power loading diagram', loc='left')
plt.show()