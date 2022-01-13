"""
----------------------------------------------------------------------------------------------------
	BulletModel
				
	A single bullet for the player.
----------------------------------------------------------------------------------------------------
"""


class BulletModel:
	
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def update(self, delta):
		self.y = self.y + delta




