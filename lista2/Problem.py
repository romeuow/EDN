import numpy as np

class ProblemClass:	
	
	def __init__(self, y0, t0, t, n, Eh):
		self.y0 = y0
		self.t0 = t0
		self.t = t
		self.n = n
		self.Eh = Eh

	def f2(self, t, y):
		return (2*y)/t + (np.power(t,2)*np.exp(t))
	
	def exactf2(self, t):
		return t*t*(np.exp(t) - np.exp(1))

	def f4(self, t, y):
		return 1/(2*y-2)
	
	def df4(self, t, y):
		return -2/((2*y-2)**2)

	def ddf4(self, t, y):
		return 8/((2*y-2)**3)
	
	def exactf4(self, t, eps=0.001):
		return 1 + np.sqrt(t+eps)

	def miniH(self, h):
		return abs(h*98.01/2 + 0.000000005/h)