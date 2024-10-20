import numpy as np
from wingpowerloading import wingloadinglanding2,altitude,rho
AR = 10
MTOWcruise = 1092
g=9.81
Vcruise = 200/3.6
T = 288.15 - 0.0065*altitude
wingloading = wingloadinglanding2[0]
S = MTOWcruise*g/wingloading
quarterchordsweep = np.arccos(1)
taperratio = 0.2*(2-quarterchordsweep*np.pi/180)
b = np.sqrt(S*AR)
cr = 2*S/((1+taperratio)*b)
ct = taperratio * cr
Mcruise = Vcruise/(1.4*287.05*T)
Mdd = Mcruise + 0.03
halfchordsweep = -np.arcsin((cr-ct)/(2*b))
CL=MTOWcruise*g/(0.5*rho*Vcruise**2*S)
thicknesstochord = np.minimum(((np.cos(halfchordsweep))**3*(0.935-Mdd*np.cos(halfchordsweep))-0.115*CL**1.5)/(np.cos(halfchordsweep))**2,0.18)

print('wingspan:', b)
print('S', S)
print('cr:', cr)
print('ct:', ct)
print('halfchordsweep',halfchordsweep*180/np.pi)
print('toverc',thicknesstochord)
