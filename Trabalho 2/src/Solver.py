import numpy as np
from scipy.sparse import diags
from scipy. linalg import lu_factor, lu_solve

class SolverClass:

	def solve(self, problem, method):
		return method(problem)

	def ForwardEuler(self, problem):
		exact = np.zeros((problem.N, problem.M))
		v = np.zeros((problem.N, problem.M))
		error = np.zeros((problem.N, problem.M))

		# Aplicando condição inicial
		h = problem.L/(problem.M-1)
		x = 0
		for j in range(problem.M):
			v[0][j] = problem.f_initial_conditions(x)
			x += h
		
		# Definindo a matriz tri diagonal (λ, 1-2λ, λ)
		tri = np.array([problem.lbda*np.ones(problem.M-1), 1-2*problem.lbda*np.ones(problem.M), problem.lbda*np.ones(problem.M-1)])
		offset = [-1,0,1]
		A = diags(tri, offset).toarray()

		# print(np.flipud(v))
		for i in range(problem.N-1):
			aux = np.matmul(A, v[i])
			v[i+1,1:-1] = aux[1:-1]
			error[i+1,:] = np.abs(v[i+1,:] - exact[i+1,:])
		# print('\n\n', np.flipud(v))
		return np.max(error[-1,:]), exact, v

	def BackwardEuler(self, problem):
		exact = np.zeros((problem.N, problem.M))
		v = np.zeros((problem.N, problem.M))
		error = np.zeros((problem.N, problem.M))

		# Aplicando condição inicial
		h = problem.L/(problem.M-1)
		x = 0
		for j in range(problem.M):
			v[0][j] = problem.f_initial_conditions(x)
			x += h
		
		# Definindo a matriz tri diagonal (-λ, 1+2λ, -λ)
		tri = np.array([(-1)*problem.lbda*np.ones(problem.M-1), 1+2*problem.lbda*np.ones(problem.M), (-1)*problem.lbda*np.ones(problem.M-1)])
		offset = [-1,0,1]
		A = diags(tri, offset).toarray()
		
		# print(np.flipud(v))
		for i in range(problem.N-1):
			aux = lu_solve(lu_factor(A), v[i], 0)
			v[i+1,1:-1] = aux[1:-1]
			error[i+1,:] = np.abs(v[i+1,:] - exact[i+1,:])

			
		# print('\n\n', np.flipud(v))

		return np.max(error[-1,:]), exact, v

	def CrankNicolson(self, problem):
		v = np.zeros((problem.N, problem.M))
		exact = np.zeros((problem.N, problem.M))
		error = np.zeros((problem.N, problem.M))

		# Aplicando condição inicial
		h = problem.L/(problem.M-1)
		x = 0
		for j in range(problem.M):
			v[0][j] = problem.f_initial_conditions(x)
			exact[0][j] = problem.f_initial_conditions(x)
			x += h
		x = 0
		
		# Definindo a matriz tri diagonal (λ, 2-2λ, λ)
		tri = np.array([(-1)*problem.lbda*np.ones(problem.M-1), 2+2*problem.lbda*np.ones(problem.M), (-1)*problem.lbda*np.ones(problem.M-1)])
		offset = [-1,0,1]
		A = diags(tri, offset).toarray()
		tri = np.array([problem.lbda*np.ones(problem.M-1), 2-2*problem.lbda*np.ones(problem.M), problem.lbda*np.ones(problem.M-1)])
		B = diags(tri, offset).toarray()
		# print(np.flipud(v))


		for i in range(problem.N-1):
			aux = lu_solve(lu_factor(A), np.matmul(B,v[i]), 0)
			v[i+1,1:-1] = aux[1:-1]			
			for j in range(problem.M-1):
				exact[i+1,j+1] = problem.exact_solution(x,i+1)
				x += h
			error[i+1,:] = np.abs(v[i+1,:] - exact[i+1,:])

		print(v)
		print(exact)
		print(error)

		return np.max(error[-1,:]), exact, v
