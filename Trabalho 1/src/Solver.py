import numpy as np
from Problem import ProblemClass

class SolverClass:

	def solve(self, problem, b, method):
		n = problem.n
		total_e, t, yv = method(problem, b, n)
		yPrevious = None
		errorSize = problem.n+1
		while yPrevious is None or np.max(abs(yPrevious[:,0:errorSize] - yv[:,0:errorSize])) > problem.Eh :
			n *= 2
			yPrevious = yv
			# t, yv = self.RK4(problem, b, n)
			e, t, yv = method(problem, b, n)
			total_e += e

		return total_e, t, yv


	def ForwardEuler(self, problem, b, n):
		e = 0
		dt = (problem.t-problem.t0)/float(n)
		t = np.zeros(n+1)
		yv = np.zeros((2, n+1))
		yv[0][0] = problem.y0
		yv[1][0] = problem.v0
		t[0] = problem.t0
		for k in range(n):
			t[k+1] = t[k] + dt
			yv[:,k+1] = yv[:,k] + np.multiply(dt, problem.function(t[k], yv[:,k], b))
			e+=1
		return e, t, yv



	def RK4(self, problem, b, n):
		e = 0
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

			e+=4
			
		return e, t, yv


	def AdamsBM4(self, problem, b, n):
		dt = (problem.t-problem.t0)/float(n)

		# Como não sei solução exata uso RK4 para inicializar o método e obter yv_{0,1,2,3}
		########		OBS: Com a função b=v^4 tenho overflow		########
		auxProblem = ProblemClass(y0=problem.y0, v0=problem.v0, t0=problem.t0, t=4, n=3, Eh=0.05)
		e, t, yv = self.RK4(auxProblem, b, auxProblem.n)
		
		# Here np.pad says, "Take the array a and add 0 rows above it, 0 rows below it, 
		# 0 columns to the left of it, and n-3 (total n+1) columns to the right of it. Fill these columns 
		# with a constant specified by constant_values".
		yv = np.pad(yv, ((0,0),(0,n-3)), mode='constant', constant_values=0)

		t = np.zeros(n+1)
		t[0] = problem.t0
		t[1] = problem.t0 + dt
		t[2] = problem.t0 + (2*dt)
		t[3] = problem.t0 + (3*dt)

		p = np.zeros((2, n+1))

		for k in range(3, n):
			t[k+1] = t[k] + dt
			p[:,k+1] = yv[:,k] + (dt/24) * (np.multiply(55,	problem.function(t[k],	yv[:,k],	b))-(np.multiply(59,problem.function(t[k-1],yv[:,k-1],	b)))+(np.multiply(37,	problem.function(t[k-2],yv[:,k-2], b)))-(np.multiply(9,problem.function(t[k-3],yv[:,k-3], b))))
			yv[:,k+1] = yv[:,k] + (dt/24) * (np.multiply(9,	problem.function(t[k+1],p[:,k+1], 	b))+(np.multiply(19,problem.function(t[k],	yv[:,k],	b)))-(np.multiply(5,	problem.function(t[k-1],yv[:,k-1], b)))+(problem.function(t[k-2],yv[:,k-2], b)))
			e+=8

		return e, t, yv