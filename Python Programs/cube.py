print("Program to calculate the properties of a Cube")
from math import sqrt 
class cube :
	def __init__ (Self, a):
		Self.a = a

	def sa (Self):
		return 6 * Self.a * Self.a

	def lateral_sa (Self):
		return 4 * Self.a * Self.a

	def vol (Self):
		return Self.a * Self.a * Self.a

	def diag (Self):
		return sqrt(3) * Self.a
		
c1 = cube(2)

print("Cube with side :", c1.a, "\nSurface Area :", c1.sa(), "\nLateral_sa : ", c1.lateral_sa(), "\nVolume : ", c1.vol(), "\nDiagonal : ", c1.diag())
