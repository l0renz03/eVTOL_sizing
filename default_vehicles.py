from cruise_vehicle import CruiseVehicle
from lifting_vehicle import LiftingVehicle

cruise_vehicle = CruiseVehicle(mtow=1092, C_L_max=1.8, L_D=15, oew=672, battery_mass=71.3, wing_span=10)
lifting_vehicle = LiftingVehicle()
cruise_vehicle.generate_payload_range()
