import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib import cm
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
from Solver import SolverClass
from Problem import ProblemClass

class Tp2Class:
	def run(self):

		np.set_printoptions(precision=0.5, suppress=True)

		solver = SolverClass()
		problem = ProblemClass(lbda=1, M=14)

		error1, e1,	v = solver.solve(problem, solver.ForwardEuler)
		error2, e2,	u = solver.solve(problem, solver.BackwardEuler)
		error3, e3, y = solver.solve(problem, solver.CrankNicolson)
		print('Aqui')
		
		style.use('fivethirtyeight')

		X = [0]
		Y = [0]
		x = 0
		h = problem.L/(problem.M-1)
		for _ in range(problem.M-1): 
			x+=h
			X.append(x)
		for k in range(problem.N-1):
			Y.append(k)

		X, Y = np.meshgrid(X, Y)
		
		fig2 = plt.figure()
		ax = fig2.gca(projection='3d')

		surf = ax.plot_surface(X, Y, v, linewidth=0, cmap=cm.coolwarm, antialiased=False)
		ax.set_xlabel('Space')
		ax.set_ylabel('Time')
		ax.set_zlabel('u')
		plt.tight_layout()
		plt.show(block=False)


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