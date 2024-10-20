from dataclasses import dataclass


@dataclass
class LiftingVehicle:
    """
    A class for a lifting vehicle.

    Attributes:
        maximum_disk_area (float): The maximum disk area. Based on 12x12 meters requirement = 144 m^2. [m^2]
    """
    maximum_disk_area: float = 144
