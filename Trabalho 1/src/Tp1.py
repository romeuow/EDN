from Solver import SolverClass
from Problem import ProblemClass
from Plot import PlotClass

class Tp1Class:

	def run(self):
		solver = SolverClass()
		problem = ProblemClass(y0=0.1, v0=1, t0=0, t=50, n=50, Eh=0.05)
		plt = PlotClass()

		t, yv = solver.solve(problem, problem.b1)
		plt.plot1(yv[0,:], yv[1,:], "b(v) = v⁴ - Plano yv")
		plt.plot2(t, yv[0,:], "b(v) = v⁴ - Plano ty")

		t, yv = solver.solve(problem, problem.b2)
		plt.plot1(yv[0,:], yv[1,:], "b(v) = 1-e^(-10v²) - Plano yv")
		plt.plot2(t, yv[0,:], "b(v) = 1-e^(-10v²) - Plano ty")

		t, yv = solver.solve(problem, problem.b3)
		plt.plot1(yv[0,:], yv[1,:], "b(v) = arctan v - Plano yv")
		plt.plot2(t, yv[0,:], "b(v) = arctan v - Plano ty")

		plt.show()

if __name__ == "__main__":	
	Tp1Class().run()