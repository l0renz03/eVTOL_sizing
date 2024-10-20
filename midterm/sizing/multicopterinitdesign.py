import numpy as np
import matplotlib.pyplot as plt

MTOW =5000
nblades = 3
nrotors = 6
rblades = 3
density = 1.11
g = 9.81
rotrate=300
FoM = 0.7
ToverWcruise = 1.2
ToverWTO = 1.2
rangex=50000
batterydensity=235
alpha = np.arccos(1/ToverWcruise)
S = 4
CD = 1.2
c = 340
cruisespeed = 200/3.6
loiterspeed = 200/3.6

def diskloadingcalc():
    diskarea = np.pi*nrotors*rblades**2
    diskloading = MTOW/diskarea
    return diskloading, diskarea

def powercalc(diskarea,ToverW):
    power = 1/FoM * np.sqrt((ToverW*MTOW*g)**3/(density*2*diskarea))
    return power

diskarea=diskloadingcalc()[1]
powercruise = powercalc(diskarea,ToverWcruise)
powerto = powercalc(diskarea,ToverWTO)

def thrustcalc():
    maxthrust = ToverWcruise*MTOW*g
    return maxthrust

def maxspeedcalc(maxthrust):
    maxspeed = np.sqrt(2*maxthrust*np.sin(alpha)/(density*CD*S))
    return maxspeed

diskloading = diskloadingcalc()[0]
diskarea = diskloadingcalc()[1]
maxthrust=thrustcalc()
maxspeed=maxspeedcalc(maxthrust)
Vlist = np.arange(20,100,0.01)

maxenergy = 1/FoM * np.sqrt(((MTOW*g)**2+(CD*0.5*density*maxspeed**2*S)**2)**(3/2)/(density*2*diskarea)) * rangex/maxspeed
print('power to',powerto)
energylist = 1/FoM * np.sqrt((((MTOW*g)**2+(CD*0.5*density*Vlist**2*S)**2)**(3/2))/(density*2*diskarea)) * (rangex/Vlist+600)

plt.plot(Vlist,energylist)
plt.show()
energycons = 1/FoM * np.sqrt((((MTOW*g)**2+(CD*0.5*density*cruisespeed**2*S)**2)**(3/2))/(density*2*diskarea)) * (rangex/cruisespeed) + 1/FoM * np.sqrt((((MTOW*g)**2+(CD*0.5*density*cruisespeed**2*S)**2)**(3/2))/(density*2*diskarea)) * (600)
print('cruise speed:', cruisespeed)
print('energy used', energycons)
print('energy used:')
print('power in cruise', energycons/(rangex/cruisespeed+600))

batterymass = powercruise * rangex/cruisespeed/3600 /batterydensity
Mt=0.6
noise = 83.4 + 15.3*np.log10(powerto/.8)-20*np.log10(2*rblades)+38.5*Mt - 3*(nblades-2)+10*np.log10(nrotors)
print(noise)
#T/W is aprox 2,(for drones)
#C_D = 0.4-1.2
# S is aprox. 3 m^2
# Assume x% of total thrust used during cruise
# E = P * R/V_c
# T = sqrt (W^2 + D^2)
#MTOW