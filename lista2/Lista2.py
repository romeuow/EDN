import math
import numpy as np
from scipy.interpolate import interp1d
import sys
sys.path.insert(0, '../')
from scipy.optimize import minimize
from Problem import ProblemClass
from OneStep import OneStepClass
from Plot import PlotClass


class Lista2Class:

	

	def run(self):

		# #Questão 2b
		os = OneStepClass()
		ptl = PlotClass()
		problem = ProblemClass(y0=0, t0=1, t=2, n=4, Eh=0.01)
		t, y = os.ForwardEuler(f=problem.f2, t0=problem.t0, y0=problem.y0, T=problem.t, dt=0.2)
		t1, y1, n, h = os.solver(problem, os.ForwardEuler, problem.f2, problem.exactf2)
		ptl.plot(t, y, t1, problem.exactf2(t1))


		#Questão 2c
		t, y = os.ForwardEuler(f=problem.f2, t0=problem.t0, y0=problem.y0, T=problem.t, dt=0.1)
		# self.plot(t, y, t1, problem.exactf2(t1))
		# print(t)
		# print(y)
		# print(np.abs(problem.exactf2(t) - y))

		#Questão 2d
		interFunction = interp1d(t, problem.exactf2(t))
		y_t = interFunction(1.97)
		# print(y_t)
		# print(problem.exactf2(1.97))

		#Questão 2f
		res = minimize(problem.miniH, 20)
		#print(res.x)
		
		# # Questão 2g ?????????
		# h = np.zeros(10)
		# Eh = np.zeros(10)
		# for k in range(0,10):
		# 	h[k] = 0.025 * (k+1)
		# 	# print(h[k])
		# 	t, y = os.ForwardEuler(f=problem.f2, t0=problem.t0, y0=problem.y0, T=problem.t, dt=h[k])
		# 	# print(np.abs(problem.exactf2(t) - y))
		# 	Eh[k] = np.max(np.abs(problem.exactf2(t) - y))
		#   # print(Eh)
		# fig = plt.figure()
		# err=plt.plot(h, Eh)
		# plt.setp(err, linewidth=2, color='b', linestyle='-') 
		# fig.suptitle("Erro global", fontsize=20)
		# plt.xlabel('h', fontsize=16)
		# plt.ylabel('E(h)', fontsize=16)
		# plt.show()


		# Questão 4
		problem = ProblemClass(y0=(1+math.sqrt(0.001)), t0=0, t=4, n=4, Eh=0.5)

		#Forward Euler
		t, y, n, h = os.solver(problem, os.ForwardEuler, problem.f4, problem.exactf4)
		ptl.plot(t, y, t, problem.exactf4(t), "Solution of Q4 using forward Euler method h = " + str(h) + "  n = " + str(n))

		#Heun
		t, y, n, h = os.solver(problem, os.Heun , problem.f4, problem.exactf4)
		ptl.plot(t, y, t, problem.exactf4(t), "Solution of Q4 using Heun method h = " + str(h) + "  n = " + str(n))

		#Ponto Medio
		t, y, n, h = os.solver(problem, os.PontoMedio , problem.f4, problem.exactf4)
		ptl.plot(t, y, t, problem.exactf4(t), "Solution of Q4 using midpoint method h = " + str(h) + "  n = " + str(n))

		#Taylor
		t, y, n, h = os.solver(problem, os.Taylor , problem.f4, problem.exactf4, problem.df4, problem.ddf4)
		ptl.plot(t, y, t, problem.exactf4(t), "Solution of Q4 using Taylor method h = " + str(h) + "  n = " + str(n))

		# #RK4
		t, y, n, h = os.solver(problem, os.Heun , problem.f4, problem.exactf4)
		ptl.plot(t, y, t, problem.exactf4(t), "Solution of Q4 using Runge-Kutta method h = " + str(h) + "  n = " + str(n))



if __name__ == "__main__":
	Lista2Class().run()