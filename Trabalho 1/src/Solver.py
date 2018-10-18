import sys
import numpy as np
import math

class SolverClass:

	def solve(self, problem, b):

		t, yv = self.RK4(problem, b)
		yPrevious = None
		errorSize = problem.n+1
		while yPrevious is None or np.max(abs(yPrevious[:,0:errorSize] - yv[:,0:errorSize])) > problem.Eh :
			problem.n *= 2
			t, yv = self.RK4(problem, b)
			yPrevious = yv
			
		return t, yv
		
	def RK4(self, problem, b):
		dt = (problem.t-problem.t0)/float(problem.n)
		t = np.zeros(problem.n+1)
		yv = np.zeros((2, problem.n+1))
		yv[0][0] = problem.y0
		yv[1][0] = problem.v0
		t[0] = problem.t0
		_k1 = np.zeros((2,1))
		_k2 = np.zeros((2,1))
		_k3 = np.zeros((2,1))
		_k4 = np.zeros((2,1))
		  
		for k in range(problem.n):
			t[k+1] = t[k] + dt
			_k1 = problem.function(t[k],yv[:,k], b)
			_k2 = problem.function(t[k] + (dt/2), yv[:,k] + np.multiply((dt/2),_k1), b)
			_k3 = problem.function(t[k] + (dt/2), yv[:,k] + np.multiply((dt/2),_k2), b)
			_k4 = problem.function(t[k+1], yv[:,k] + np.multiply(dt,_k3), b)
			
			yv[:,k+1] = yv[:,k] + np.multiply((dt/6),(_k1 + np.multiply(2,_k2) + np.multiply(2,_k3) + _k4))
			
			
		return t, yv
