import random

class Energy: 
	def __init__(self, range_min: int, range_max: int) -> None:
		self.at_start: int = random.randrange(range_min, range_max)
		self.at_end: int = random.randrange(range_min, range_max)
		self.at_collision: int = random.randrange(0, self.at_start)
		self.at_collision: int = self.at_start + random.randrange(0, range_max - self.at_start)
 
	def __repr__(self) -> str:
		return f"{self.at_start}, {self.at_end}, {self.at_collision}"
 
	def get_headers() -> str:
		return "S_Energy, E_Energy, Col, Col_Point"