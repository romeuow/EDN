import math
import matplotlib.pyplot as plt
from Problem import ProblemClass
from OneStep import OneStepClass as os

class MainClass:

	def plot(self, t, y, t1, y_exact, title=None):
		fig = plt.figure()
		lines=plt.plot(t, y, t1, y_exact)
		l1, l2 = lines
		plt.setp(l1, linewidth=2, color='b', linestyle='--')  # line1 is thick and red
		plt.setp(l2, linewidth=2, color='g', linestyle='-') 
		plt.legend(lines, ['Numérica','Exata'])
		if title:
			fig.suptitle(title, fontsize=20)
		plt.xlabel('t', fontsize=16)
		plt.ylabel('y', fontsize=16)
		plt.show()

	def run(self):		


		#Questão 2b da lista
		problem = ProblemClass(y0=0, t0=1, t=2, n=4, Eh=0.5)
		t, y = os.ForwardEuler(f=problem.f2, t0=problem.t0, y0=problem.y0, T=problem.t, dt=0.2)
		t1, y1, n, h = os.solver(os, problem, os.ForwardEuler, problem.f2, problem.exactf2)
		self.plot(t, y, t1, problem.exactf2(t1))

		#Questão 2c da lista
		t, y = os.ForwardEuler(f=problem.f2, t0=problem.t0, y0=problem.y0, T=problem.t, dt=0.1)
		self.plot(t, y, t1, problem.exactf2(t1))		

		# #Questão 4 da lista
		# problem = ProblemClass(y0=(1+math.sqrt(0.001)), t0=0, t=4, n=4, Eh=0.75)

		# #Forward Euler
		# t, y, n, h = os.solver(os, problem, os.ForwardEuler, problem.f4, problem.exactf4)
		# self.plot(t, y, t, problem.exactf4(t), "Solution of Q4 using forward Euler method h = " + str(h) + "  n = " + str(n))

		# #Heun
		# t, y, n, h = os.solver(os, problem, os.Heun , problem.f4, problem.exactf4)
		# self.plot(t, y, t, problem.exactf4(t), "Solution of Q4 using Heun method h = " + str(h) + "  n = " + str(n))

		# #Ponto Medio
		# t, y, n, h = os.solver(os, problem, os.PontoMedio , problem.f4, problem.exactf4)
		# self.plot(t, y, t, problem.exactf4(t), "Solution of Q4 using midpoint method h = " + str(h) + "  n = " + str(n))

		# #Taylor
		# t, y, n, h = os.solver(os, problem, os.Taylor , problem.f4, problem.exactf4, problem.df4, problem.ddf4)
		# self.plot(t, y, t, problem.exactf4(t), "Solution of Q4 using Taylor method h = " + str(h) + "  n = " + str(n))

		# #RK4
		# t, y, n, h = os.solver(os, problem, os.Heun , problem.f4, problem.exactf4)
		# self.plot(t, y, t, problem.exactf4(t), "Solution of Q4 using Runge-Kutta method h = " + str(h) + "  n = " + str(n))


if __name__ == "__main__":
	MainClass().run()