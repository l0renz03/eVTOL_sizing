from dataclasses import dataclass
from performance import payload_range


@dataclass
class CruiseVehicle:
    """
    A class for a cruise vehicle.

    Attributes:
        mtow (float): The maximum takeoff weight. [kg]
        oew (float): The operating empty weight. [kg]
        C_L_max (float): The maximum lift coefficient. [-]
        L_D (float): The lift-to-drag ratio. [-]
        battery_mass (float): The battery mass. [kg]
        propeller_efficiency (float): The propeller efficiency, assumed to be 0.8. [-]
        V_cruise (float): The cruise speed, assumed to be 200 km/h (55.6 m/s). [m/s]
        range (float): The range, assumed to be 50 km (50000 m). [m]
        battery_efficiency (float): The battery efficiency, assumed to be 0.9. [-]
        payload (float): The payload, assumed to be 420 kg. [kg]
        takeoff_distance (float): The takeoff distance, assumed to be 500 m. [m]
    """
    oew: float
    mtow: float
    C_L_max: float
    L_D: float
    battery_mass: float
    wing_span: float
    propeller_efficiency: float = 0.8
    V_cruise: float = 200 / 3.6
    range: float = 50 * 1000
    battery_efficiency: float = 0.9
    payload: float = 420
    takeoff_distance: float = 500

    def get_cruise_endurance(self):
        """
        Calculate the cruise endurance.

        Returns:
            float: The cruise endurance. [s]
        """
        return self.range / self.V_cruise

    def generate_payload_range(self):
        """
        Generate a payload range.

        Returns:
            range: The payload range.
        """
        return payload_range.generate_electric_payload_range(self.oew, self.payload, self.L_D, self.battery_mass,
                                                             self.propeller_efficiency)
