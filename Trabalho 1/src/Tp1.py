from Solver import SolverClass
from Problem import ProblemClass
from Plot import PlotClass

class Tp1Class:

	def run(self):
		solver = SolverClass()
		problem = ProblemClass(y0=1, v0=1, t0=0, t=50, n=25, Eh=0.05)
		ptl = PlotClass()

		t, yv = solver.solve(problem, problem.b3)
		ptl.plot(yv[0,:], yv[1,:])

if __name__ == "__main__":	
	Tp1Class().run()