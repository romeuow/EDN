import sys
import numpy as np
import math

class OneStepClass:

	def solver(self, problem, method, f, exact, dy=None, dyy=None):
		
		if dy is not None:
			t, y = method(f, problem.t0, problem.y0, problem.t, dy, dyy, problem.n)
		else:
			t, y = method(f, problem.t0, problem.y0, problem.t, problem.n)
		yExact = exact(t)

		while np.max(abs(yExact - y)) > problem.Eh:
			problem.n *= 2
			if dy is not None:
				t, y = method(f, problem.t0, problem.y0, problem.t, dy, dyy, problem.n)
			else:
				t, y = method(f, problem.t0, problem.y0, problem.t, problem.n)
			yExact = exact(t)

		h = float((problem.t-problem.t0)/problem.n)
		return t, y, problem.n, h		


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

	def Heun(self, f, t0, y0, T, n=1, dt=-1):
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
			y[k+1] = y[k] + (dt/2)*(f(t[k], y[k]) + f(t[k+1], y[k] + dt*f(t[k],y[k])))
		return t, y

	def PontoMedio(self, f, t0, y0, T, n=1, dt=-1):
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
			y[k+1] = y[k] + dt*f(t[k]+(dt/2), y[k]+(dt/2)*f(t[k],y[k]))
		return t, y
  
  
	def Taylor(self, f, t0, y0, T, dy, dyy, n=1, dt=-1):
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
			fk = f(t[k], y[k]) # f em t(k), y(k)
			dfk = dy(t[k], y[k]) # dy de em f t(k), y(k)
			ddfk = dyy(t[k], y[k]) # dyy de f em t(k), y(k)
			
			t[k+1] = t[k] + dt
			
			a1 = dt * fk
			a2 = ((dt**2)/2) * dfk * fk
			a3 = ((dt**3)/6) * ((ddfk * (fk**2)) + ((dfk**2) * fk))
			
			y[k+1] = y[k] + a1 + a2 + a3
			
		return t, y
  
	def RK4(self, f, t0, y0, T, n=1, dt=-1):
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
			_k1 = f(t[k],y[k])
			_k2 = f(t[k] + (dt/2), y[k] + ((dt/2)*_k1))
			_k3 = f(t[k] + (dt/2), y[k] + ((dt/2)*_k2))
			_k4 = f(t[k+1], y[k] + (dt*_k3))
			
			y[k+1] = y[k] + (dt/6)*(_k1+ 2*_k2 + 2*_k3 + _k4)
		return t, y