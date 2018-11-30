from Solver import SolverClass
from Problem import ProblemClass
from Plot import PlotClass
import time

class Tp1Class:

	def run(self):
		solver = SolverClass()
		plt = PlotClass()

		# # v⁴
		# problem = ProblemClass(y0=0.1, v0=1, t0=0, t=50, n=100, Eh=1.42)
		# start_time = time.time()
		# Eh, total_e, t, yv = solver.solve(problem, problem.b1, solver.ForwardEuler)
		# print('v⁴\n\nEuler\nTotal time: ',time.time()-start_time)
		# print('Evaluations = ',total_e, '\n')
		# # plt.plot1(yv[0,:], yv[1,:], "Euler, b(v) = v⁴ - Plano yv")
		# # plt.plot2(t, yv[0,:], "Euler, b(v) = v⁴ - Plano ty")
		# # plt.plot2(t, yv[1,:], "Euler, b(v) = v⁴ - Plano tv")		
		# start_time = time.time()
		# Eh, total_e, t, yv = solver.solve(problem, problem.b1, solver.RK4)
		# print('RK4\nTotal time: ',time.time()-start_time)
		# print('Evaluations = ',total_e, '\n')
		# plt.plot1(yv[0,:], yv[1,:], "RK4, b(v) = v⁴ - Plano yv")
		# plt.plot2(t, yv[0,:], "RK4, b(v) = v⁴ - Plano ty")
		# plt.plot2(t, yv[1,:], "RK4, b(v) = v⁴ - Plano tv")
		# start_time = time.time()
		# Eh, total_e, t, yv = solver.solve(problem, problem.b1, solver.AdamsBM4)
		# print('ABM4\nTotal time: ',time.time()-start_time)
		# print('Evaluations = ',total_e, '\n')
		# # plt.plot1(yv[0,:], yv[1,:], "ABM4, b(v) = v⁴ - Plano yv")
		# # plt.plot2(t, yv[0,:], "ABM4, b(v) = v⁴ - Plano ty")
		# # plt.plot2(t, yv[1,:], "ABM4, b(v) = v⁴ - Plano tv")

		# # 1-e^(-10v²)
		# ### + Amortecimento - Conforto
		# problem = ProblemClass(y0=0.1, v0=20, t0=0, t=50, n=100, Eh=19.18)
		# start_time = time.time()
		# Eh, total_e, t, yv = solver.solve(problem, problem.b2, solver.ForwardEuler)
		# print('1-e^(-10v²)\n\nEuler\nTotal time: ',time.time()-start_time)
		# print('Evaluations = ',total_e, '\n')
		# # plt.plot1(yv[0,:], yv[1,:], "Euler, b(v) = 1-e^(-10v²) - Plano yv")
		# # plt.plot2(t, yv[0,:], "Euler, b(v) = 1-e^(-10v²) - Plano ty")		
		# # plt.plot2(t, yv[1,:], "Euler, b(v) = 1-e^(-10v²) - Plano tv")		
		# start_time = time.time()
		# Eh, total_e, t, yv = solver.solve(problem, problem.b2, solver.RK4)
		# print('RK4\nTotal time: ',time.time()-start_time)
		# print('Evaluations = ',total_e, '\n')
		# # plt.plot1(yv[0,:], yv[1,:], "RK4, b(v) = 1-e^(-10v²) - Plano yv")
		# # plt.plot2(t, yv[0,:], "RK4, b(v) = 1-e^(-10v²) - Plano ty")
		# # plt.plot2(t, yv[1,:], "RK4, b(v) = 1-e^(-10v²) - Plano tv")		
		# start_time = time.time()
		# Eh, total_e, t, yv = solver.solve(problem, problem.b2, solver.AdamsBM4)
		# print('ABM4\nTotal time: ',time.time()-start_time)
		# print('Evaluations = ',total_e, '\n')
		# plt.plot1(yv[0,:], yv[1,:], "ABM4, b(v) = 1-e^(-10v²) - Plano yv")
		# plt.plot2(t, yv[0,:], "ABM4, b(v) = 1-e^(-10v²) - Plano ty")
		# plt.plot2(t, yv[1,:], "ABM4, b(v) = 1-e^(-10v²) - Plano tv")		

		# arctan(v)
		# - Amortecimento + Conforto
		problem =ProblemClass(y0=0.1, v0=1, t0=0, t=50, n=100, Eh=4.6) 
		start_time = time.time()
		Eh, total_e, t, yv = solver.solve(problem, problem.b3, solver.ForwardEuler)
		print('arctan(v)\n\nEuler\nTotal time: ',time.time()-start_time)
		print('Evaluations = ',total_e, '\n')
		plt.plot1(yv[0,:], yv[1,:], "Euler, b(v) = arctan(v) - Plano yv")
		# plt.plot2(t, yv[0,:], "Euler, b(v) = arctan(v) - Plano ty")
		# plt.plot2(t, yv[1,:], "Euler, b(v) = arctan(v) - Plano tv")
		start_time = time.time()
		Eh, total_e, t, yv = solver.solve(problem, problem.b3, solver.RK4)
		print('RK4\nTotal time: ',time.time()-start_time)
		print('Evaluations = ',total_e, '\n')
		plt.plot1(yv[0,:], yv[1,:], "RK4, b(v) = arctan(v) - Plano yv")
		# plt.plot2(t, yv[0,:], "RK4, b(v) = arctan(v) - Plano ty")
		# plt.plot2(t, yv[1,:], "RK4, b(v) = arctan(v) - Plano tv")
		start_time = time.time()
		Eh, total_e, t, yv = solver.solve(problem, problem.b3, solver.AdamsBM4)
		print('ABM4\nTotal time: ',time.time()-start_time)
		print('Evaluations = ',total_e, '\n')
		plt.plot1(yv[0,:], yv[1,:], "ABM4, b(v) = arctan(v) - Plano yv")
		plt.plot2(t, yv[0,:], "ABM4, b(v) = arctan(v) - Plano ty")
		# plt.plot2(t, yv[1,:], "ABM4, b(v) = arctan(v) - Plano tv")

		
		plt.show()


if __name__ == "__main__":	
	Tp1Class().run()