import numpy as np

class SolverClass:

	def solve(self, problem, b):

		n = problem.n
		t, yv = self.RK4(problem, b, n)
		yPrevious = None
		errorSize = problem.n+1
		while yPrevious is None or np.max(abs(yPrevious[:,0:errorSize] - yv[:,0:errorSize])) > problem.Eh :
			n *= 2
			yPrevious = yv
			t, yv = self.RK4(problem, b, n)
			
		return t, yv
		
	def RK4(self, problem, b, n):
		dt = (problem.t-problem.t0)/float(n)
		t = np.zeros(n+1)
		yv = np.zeros((2, n+1))
		yv[0][0] = problem.y0
		yv[1][0] = problem.v0
		t[0] = problem.t0
		_k1 = np.zeros((2,1))
		_k2 = np.zeros((2,1))
		_k3 = np.zeros((2,1))
		_k4 = np.zeros((2,1))
		  
		for k in range(n):
			t[k+1] = t[k] + dt
			_k1 = problem.function(t[k],yv[:,k], b)
			_k2 = problem.function(t[k] + (dt/2), yv[:,k] + np.multiply((dt/2),_k1), b)
			_k3 = problem.function(t[k] + (dt/2), yv[:,k] + np.multiply((dt/2),_k2), b)
			_k4 = problem.function(t[k+1], yv[:,k] + np.multiply(dt,_k3), b)
			
			yv[:,k+1] = yv[:,k] + np.multiply((dt/6),(_k1 + np.multiply(2,_k2) + np.multiply(2,_k3) + _k4))

			
		return t, yv
