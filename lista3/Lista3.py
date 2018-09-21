import sys
import math
sys.path.insert(0, '../')
sys.path.insert(1, '../lista2')
from Problem import ProblemClass
from MultiStep import MultiStepClass
from Plot import PlotClass

class Lista3Class:

	def run(self):
		ms = MultiStepClass()		
		pl = PlotClass()
		problem = ProblemClass(y0=(1+math.sqrt(0.001)), t0=0, t=4, n=4, Eh=0.00002)

		t, y, n, h = ms.solver(problem, ms.AdamsBM4)
		pl.plot(t, y, t, problem.exactf4(t))
		

if __name__ == "__main__":
	Lista3Class().run()