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

		np.set_printoptions(precision=3, suppress=True)

		solver = SolverClass()
		problem = ProblemClass(lbda=1, M=14)

		error1, e1,	v = solver.solve(problem, solver.ForwardEuler)
		error2, e2,	u = solver.solve(problem, solver.BackwardEuler)
		error3, e3, y = solver.solve(problem, solver.CrankNicolson)
		
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
		
		fig1 = plt.figure()
		fig2 = plt.figure()
		fig3 = plt.figure()

		ax1 = fig1.gca(projection='3d')
		ax2 = fig2.gca(projection='3d')
		ax3 = fig3.gca(projection='3d')

		ax1.set_title('F.Euler')
		ax1.set_xlabel('Space')
		ax1.set_ylabel('Time')
		ax1.set_zlabel('u')

		ax2.set_title('B.Euler')
		ax2.set_xlabel('Space')
		ax2.set_ylabel('Time')
		ax2.set_zlabel('u')

		ax3.set_title('Crank Nicolson')
		ax3.set_xlabel('Space')
		ax3.set_ylabel('Time')
		ax3.set_zlabel('u')

		ax1.plot_surface(X, Y, v, linewidth=0, cmap=cm.coolwarm, antialiased=False)
		ax2.plot_surface(X, Y, u, linewidth=0, cmap=cm.coolwarm, antialiased=False)
		ax3.plot_surface(X, Y, y, linewidth=0, cmap=cm.coolwarm, antialiased=False)
		print(error1,error2,error3)
		plt.show()


		# Animação
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
		# 	plt.plot(dx,e1[i], 'rx')
			

		# ani = FuncAnimation(fig, animate, problem.N, init_func=init, interval=100)

if __name__ == "__main__":	
	Tp2Class().run()