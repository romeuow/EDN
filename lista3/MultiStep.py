import numpy as np

class MultiStepClass:

	def solver(self, problem, method):
		
		n = problem.n
		t, y = method(problem.f4, problem, n)
		yExact = problem.exactf4(t)

		while np.max(abs(yExact - y)) > problem.Eh:
			n *= 2
			t, y = method(problem.f4, problem, n)
			yExact = problem.exactf4(t)

		h = float((problem.t-problem.t0)/n)
		
		return t, y, n, h

	def AdamsBM4(self, f, problem, n):

		dt = (problem.t-problem.t0)/float(n)

		t = np.zeros(n+1)
		p = np.zeros(n+1)
		y = np.zeros(n+1)  # y[k] is the solution at time t[k]

		t[0] = problem.t0
		t[1] = problem.t0 + dt
		t[2] = problem.t0 + (2*dt)
		t[3] = problem.t0 + (3*dt)
		y[0] = round(problem.exactf4(t[0]),5)
		y[1] = round(problem.exactf4(t[1]),5)
		y[2] = round(problem.exactf4(t[2]),5)
		y[3] = round(problem.exactf4(t[3]),5)

		for k in range(3, n):
			t[k+1] = t[k] + dt
			p[k+1] = y[k] + (dt/24) * ((55*f(t[k],y[k]))-(59*f(t[k-1],y[k-1]))+(37*f(t[k-2],y[k-2]))-(9 *f(t[k-3],y[k-3])))
			c_1 = y[k] + (dt/24) * ((9*f(t[k+1],p[k+1]))+(19*f(t[k],y[k]))-(5*f(t[k-1],y[k-1]))+(f(t[k-2],y[k-2])))
			c_2 = y[k] + (dt/24) * ((9*f(t[k+1],c_1))+(19*f(t[k],y[k]))-(5*f(t[k-1],y[k-1]))+(f(t[k-2],y[k-2])))
			y[k+1] = c_2

		return t, y