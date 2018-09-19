import numpy as np

class ProblemClass:	
	
	def __init__(self, y0, t0, t, n, Eh):
		self.y0 = y0
		self.t0 = t0
		self.t = t
		self.n = n
		self.Eh = Eh

	def exactf4(self, t, eps=0.001):
		return (1 + np.sqrt(t+eps))

	def f4(self, t, y):
		return 1/(2*y-2)
	
	def df4(self, t, y):
		return -2/((2*y-2)**2)

	def ddf4(self, t, y):
		return 8/((2*y-2)**3)