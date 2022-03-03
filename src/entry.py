import random
from datetime import datetime, timedelta

from run_time import Start, End
from energy import Energy
from cyclus import Cyclus
from particle import Particle

class Entry:
	def __init__(self, run_id: int): 
		random.seed()
		# Set id
		self.run_id = run_id
 
		# Set start timestamp
		self.start = Start(datetime.now())
 
		# Generate cycle data
		self.cyclus = Cyclus(datetime.now())
 
		# Generate end timestamp
		self.end = End(datetime.now() +
			timedelta(
				seconds=random.randrange(0,1800),
				milliseconds=random.randrange(0,999)
			)
		)
 
		# Generate energy values
		self.energy = Energy(0, 100000)
 
		self.particles = [Particle() for n in range(5)]
 
 
	def __repr__(self):
		data: str = f"{self.run_id}, "
		data += f"{self.start}, "
		data += f"{self.end}, "
		data += f"{self.energy}, "
		data += f"{self.cyclus}"
		for particle in self.particles:
			data += f", {particle}"
		return data + "\n"
 
	def get_headers() -> str:
		return (f"Run_ID, {Start.get_headers()}, "
			f"{End.get_headers()}, "
			f"{Energy.get_headers()}, "
			f"{Cyclus.get_headers()}, "
			f"{Particle.get_headers(5)}"
			"\n"
		)