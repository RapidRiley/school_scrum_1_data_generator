import random
from datetime import datetime

class Cyclus:
	def __init__(self, time: datetime) -> None:
		self.collision_ocurred: str = "Y" if random.randrange(0,2) == 1 else "N"
 
		# Generate collision point
		self.collision_point: str = self.get_point_string(random.randrange(0,8))
 
		# Generate id
		self.id: str = self.get_id_string(random.randrange(0,3))
 
		self.enter_speed = random.randrange(0, 200000)
		self.exit_speed = random.randrange(80000, 300000)
 
		self.measure_point = self.get_point_string(random.randrange(0,3))
		self.measure_time = time.strftime("%Y%m%d%p%H%M%S")
 
	def get_point_string(self, id: int) -> str:
		match id:
			case 0:
				return "CL1"
			case 1:
				return "CL2"
			case 2:
				return "CL3"
			case 3:
				return "CL4"
			case 4:
				return "CL5" 
			case 5:
				return "CP1"
			case 6:
				return "CS1"
			case 7:
				return "CS2"
		return "None"
 
	def get_id_string(self, id: int) -> str:
		match id:
			case 1:
				self.id = "PS"
			case 2:
				self.id = "SPS"
		return "LHC"
 
	def __repr__(self) -> str:
		return f"{self.collision_ocurred}, {self.collision_point}, {self.id}, {self.enter_speed}, {self.exit_speed} {self.measure_point}, {self.measure_time}"
 
	def get_headers() -> str:
		return "Cyclus_ID, Cyclus_EnterSpeed, Cyclus_ExitSpeed, Measurepoint, Measuretime"
 