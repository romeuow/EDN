import matplotlib.pyplot as plt

class PlotClass:

	def plot(self, y, v, title=None):
		fig = plt.figure()
		l1 = plt.plot(y,v)
		plt.setp(l1, linewidth=2, color='b', linestyle='--')  # line1 is thick and red
		plt.legend(l1, 'v⁴')
		if title:
			fig.suptitle(title, fontsize=20)
		plt.xlabel('y', fontsize=16)
		plt.ylabel('v', fontsize=16)
		plt.show()