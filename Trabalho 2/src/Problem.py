import numpy as np
from scipy import integrate

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

	def exact_solution(self, x, t):

		def integrand(x, a, n):

			if (a >= np.pi/4) and (a <= np.pi/2):
				return (4/np.pi)*(x - (np.pi/4))*np.sin(n*np.pi/self.L*x)
			else:
				return (4/np.pi)*((3*np.pi/4) - x)*np.sin(n*np.pi/self.L*x)

		exact = 0
		for n in range(1,3)
			bn = 2/self.L*integrate.quad(integrand, np.pi/4, np.pi/2, args=(np.pi/2, n))[0] + integrate.quad(integrand, np.pi/2, 3*np.pi/4, args=(3*np.pi/4, n))[0]
			exact += bn * (np.exp(-(n*np.pi/self.L)**2))*problem.k*t*np.sin(n*np.pi/self.L*x)
		exact += 

		print(bn)


	def N(self):
		return int(np.ceil(self.T * self.k * (self.M ** 2) * (1 / (self.lbda * (self.L ** 2)))))

