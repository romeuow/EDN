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
		problem = ProblemClass(lbda=0.5, M=14)

		error1, e1,	v = solver.solve(problem, solver.ForwardEuler)
		error2, e2,	u = solver.solve(problem, solver.BackwardEuler)
		error3, e3, y = solver.solve(problem, solver.CrankNicolson)
		
		style.use('fivethirtyeight')
	
		fig = plt.figure()

		def init():
			plt.clf()

		def animate(i):
			h = problem.L/(problem.M-1)
			x=0
			dx = [x]
			for j in range(problem.M-1):
				x+=h
				dx.append(x)

			plt.plot(dx,v[i],'yo')
			plt.plot(dx,u[i],'go')
			plt.plot(dx,y[i],'bo')
			plt.plot(dx,e1[i], 'rx')

		ani = FuncAnimation(fig, animate, problem.N, init_func=init, interval=100)
		print(error1,error2,error3)
		plt.show()

if __name__ == "__main__":	
	Tp2Class().run()