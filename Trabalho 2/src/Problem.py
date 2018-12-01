import numpy as np

class ProblemClass:	
	
	def __init__(self, lbda, M):
		self.k = 10
		self.L = np.pi
		self.lbda = lbda
		self.M = M
		self.T = 0.5
		
	def f_initial_conditions(self, x):
		if (x >= np.pi/4) and (x <= np.pi/2):
			return (4/np.pi)*(x - (np.pi/4))
		elif (x > np.pi/2) and (x <= 3*np.pi/4):
			return (4/np.pi)*((3*np.pi/4) - x)
		else:
			return 0		

	def N(self):
		return int(np.ceil(self.T * self.k * (self.M ** 2) * (1 / (self.lbda * (self.L ** 2)))))