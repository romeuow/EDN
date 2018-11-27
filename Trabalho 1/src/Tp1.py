from Solver import SolverClass
from Problem import ProblemClass
from Plot import PlotClass
import time

class Tp1Class:

	def run(self):
		solver = SolverClass()
		problem = ProblemClass(y0=0.1, v0=1, t0=0, t=50, n=100, Eh=0.04)
		plt = PlotClass()

		start_time = time.time()
		total_e, t, yv = solver.solve(problem, problem.b1, solver.AdamsBM4)
		print(time.time()-start_time)
		print(total_e)
		plt.plot1(yv[0,:], yv[1,:], "b(v) = v⁴ - Plano yv")
		plt.plot2(t, yv[0,:], "b(v) = v⁴ - Plano ty")
		
		start_time = time.time()
		total_e, t, yv = solver.solve(problem, problem.b2, solver.AdamsBM4)
		print(time.time()-start_time)
		print(total_e)
		plt.plot1(yv[0,:], yv[1,:], "b(v) = 1-e^(-10v²) - Plano yv")
		plt.plot2(t, yv[0,:], "b(v) = 1-e^(-10v²) - Plano ty")

		start_time = time.time()
		total_e, t, yv = solver.solve(problem, problem.b3, solver.AdamsBM4)
		print(time.time()-start_time)
		print(total_e)
		plt.plot1(yv[0,:], yv[1,:], "b(v) = arctan v - Plano yv")
		plt.plot2(t, yv[0,:], "b(v) = arctan v - Plano ty")

		plt.show()


if __name__ == "__main__":	
	Tp1Class().run()