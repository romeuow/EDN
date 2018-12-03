import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.animation import FuncAnimation
from Solver import SolverClass
from Problem import ProblemClass
# import time

class Tp2Class:
	def run(self):

		np.set_printoptions(precision=3, suppress=True)

		solver = SolverClass()
		problem = ProblemClass(lbda=0.5, M=10)

		# v = solver.solve(problem, solver.ForwardEuler)
		# u = solver.solve(problem, solver.BackwardEuler)
		# y = solver.solve(problem, solver.CrankNicolson)
		
		# style.use('fivethirtyeight')
	
		# fig = plt.figure()

		# def init():
		# 	plt.clf()
			
		# def animate(i):
		# 	h = problem.L/(problem.M-1)
		# 	x=0
		# 	dx = [x]
		# 	for j in range(problem.M-1):
		# 		x+=h
		# 		dx.append(x)

		# 	plt.plot(dx,v[i],'yo')
		# 	plt.plot(dx,u[i],'go')
		# 	plt.plot(dx,y[i],'bo')

		# ani = FuncAnimation(fig, animate, problem.N(), init_func=init, interval=5)
		# plt.show()

		problem.exact_solution()

if __name__ == "__main__":	
	Tp2Class().run()