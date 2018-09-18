import math

class ProblemClass:	
	
	def f2(self, t, y):
		return (2*y/t) + (t*t*math.exp(t))
	
	def f4(self, t, y):
		return 1/(2*y-2)
	
	def df4(self, t, y):
		return -2/math.pow(2*y-2,2)

	def ddf4(self, t, y):
		return 8/math.pow(2*y-2, 3)

	def exactF4(self, t, eps=0.001):
		return 1 + math.sqrt(t+eps)