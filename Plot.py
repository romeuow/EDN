import matplotlib.pyplot as plt

class PlotClass:

	def plot(self, t, y, t1, y_exact, title=None):
		fig = plt.figure()
		lines=plt.plot(t, y, t1, y_exact)
		l1, l2 = lines
		plt.setp(l1, linewidth=2, color='b', linestyle='--')  # line1 is thick and red
		plt.setp(l2, linewidth=2, color='g', linestyle='-') 
		plt.legend(lines, ['Numérica','Exata'])
		if title:
			fig.suptitle(title, fontsize=20)
		plt.xlabel('t', fontsize=16)
		plt.ylabel('y', fontsize=16)
		plt.show()