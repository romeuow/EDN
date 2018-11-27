import numpy as np

class ProblemClass:	
	
	def __init__(self, y0, v0, t0, t, n, Eh):
		self.y0 = y0
		self.t0 = t0
		self.t = t
		self.n = n
		self.v0 = v0
		self.Eh = Eh

	# system:
	# y' = v(t)
	# v' = -b(v)v(t)-y(t)
	def function(self, t, yv, b):
		return yv[1] , (np.multiply(-b(yv[1]),yv[1]) - yv[0])

	# v⁴
	def b1(self, v):
		return np.power(v, 4)

	# 1-e^(-10v²)
	def b2(self, v):
		return 1 - np.exp(-10*v**2)

	# arctan v
	def b3(self, v):
		return np.arctan(v)