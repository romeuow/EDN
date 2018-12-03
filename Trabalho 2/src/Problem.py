import numpy as np
from scipy import integrate

class ProblemClass:	
	
	def __init__(self, lbda, M):
		self.k = 10
		self.L = np.pi
		self.lbda = lbda
		self.M = M
		self.T = 0.5

	def fx1(self, x):
		return (4/np.pi)*(x - (np.pi/4))

	def fx2(self, x):
		return (4/np.pi)*((3*np.pi/4) - x)

	def f_initial_conditions(self, x):
		if (x >= np.pi/4) and (x <= np.pi/2):
			return self.fx1(x)
		elif (x > np.pi/2) and (x <= 3*np.pi/4):
			return self.fx2(x)
		else:
			return 0		

	def exact_solution(self, x, t):

		def integrand(x, a, n):
			return self.f_initial_conditions(a) * np.sin((n*np.pi/self.L)*x)

		exact = 0
		for n in range(5):
			bn = 2/self.L*integrate.quad(integrand, np.pi/4, np.pi/2, args=(np.pi/2, n))[0] + integrate.quad(integrand, np.pi/2, 3*np.pi/4, args=(3*np.pi/4, n))[0]
			exact += bn * (np.exp((-1)*(n*np.pi/self.L)**2*self.k*t)) * np.sin((n*np.pi/self.L)*x)

		return exact


	def N(self):
		return int(np.ceil(self.T * self.k * (self.M ** 2) * (1 / (self.lbda * (self.L ** 2)))))

