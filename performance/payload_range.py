import numpy as np
from matplotlib import pyplot as plt

import constants


def generate_electric_payload_range(oew: float, payload: float, L_D: float, battery_mass: float,
                                    propeller_efficiency: float,
                                    energy_density: float = constants.battery_energy_density,
                                    battery_efficiency: float = constants.battery_efficiency):
    """
    Generates the payload range diagram for an electric aircraft.

    :param oew: Operating empty weight. [kg]
    :param payload: Payload mass. [kg]
    :param L_D: Lift-to-drag ratio. [-]
    :param battery_mass: Battery mass. [kg]
    :param propeller_efficiency: Propeller efficiency. [-]
    :param energy_density: Battery energy density. By default, value taken from constants. [Wh/kg]
    :param battery_efficiency: Battery efficiency. By default, value taken from constants. [-]
    """
    payloads = np.linspace(0, payload, 100)
    ranges = (3.6 * L_D * energy_density * battery_efficiency * propeller_efficiency * battery_mass /
              constants.g / (oew + payloads))
    payloads = np.append(payloads, payload)
    ranges = np.append(ranges, 0)
    plt.plot(ranges, payloads)
    plt.xlabel('Range [km]')
    plt.ylabel('Payload [kg]')
    plt.xlim(left=0)
    plt.ylim(bottom=0)
    plt.show()
