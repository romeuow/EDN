import sys
import numpy as np
import math


class OneStepClass:

	def solver(self, problem, method, f, exact):
		if not callable(method):
			raise TypeError('method is %s, not a function' % type(method))
		if not callable(f):
			raise TypeError('f is %s, not a function' % type(f))
		if not callable(exact):
			raise TypeError('exact is %s, not a function' % type(exact))
		
		t, y = method(f, problem.t0, problem.y0, problem.t, problem.n)
		yExact = exact(t)

		while np.max(abs(yExact - y)) > problem.Eh:
			problem.n *= 2
			t, y = method(f, problem.t0, problem.y0, problem.t, problem.n)
			yExact = exact(t)

		h = float((problem.t-problem.t0)/problem.n)
		return t, y, problem.n, h
		


	def ForwardEuler(f, t0, y0, T, n=1, dt=-1):
		"""Solve y'=f(t,y), y(0)=y0, with n steps until t=T."""
		if dt == -1:
			dt = (T-t0)/float(n)
		else:
			n = int(math.ceil((T-t0)/dt))
		t = np.zeros(n+1)
		y = np.zeros(n+1)  # y[k] is the solution at time t[k]
		y[0] = y0
		t[0] = t0
		for k in range(n):
			t[k+1] = t[k] + dt
			y[k+1] = y[k] + dt*f(t[k], y[k])
		return t, y


