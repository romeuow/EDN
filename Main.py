import math
import matplotlib.pyplot as plt
from Problem import ProblemClass
from OneStep import OneStepClass as os

class MainClass:

	def plot(self, t, y, y_exact, title=None):
		fig = plt.figure()
		lines=plt.plot(t, y, t, y_exact)
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
		
		problem = ProblemClass(y0=(1+math.sqrt(0.001)), t0=0, t=4, n=4, Eh=0.0001)

		t, y, n, h = os.solver(os, problem, os.ForwardEuler, problem.f4, problem.exactf4)
		print(n,h)
		self.plot(t, y, problem.exactf4(t), "Solution of Q4 using forward Euler method h = " + str(h) + "   n = " + str(n))

if __name__ == "__main__":
	MainClass().run()