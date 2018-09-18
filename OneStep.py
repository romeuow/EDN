import sys
import numpy as np
import math


class OneStepClass:

	def solver(self, method, f, exact, y0=(1+math.sqrt(0.001)), t0=0, t=4, n=4, Eh=0.0005):
		if not callable(f):
			raise TypeError('f is %s, not a function' % type(f))
		if not callable(method):
			raise TypeError('method is %s, not a function' % type(method))
		
		t,y = method(f, t0, y0, t, n)
		yExact = exact(t)

		while abs(yExact - y) > Eh:
			n *= 2
			t,y = method(f, t0, y0, t, n)
			yExact = exact(t)

		


	def ForwardEuler(self, f, t0, y0, T, n=1, dt=-1):
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


