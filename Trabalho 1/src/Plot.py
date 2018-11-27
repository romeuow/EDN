import matplotlib.pyplot as plt

class PlotClass:

	def plot1(self, y, v, title=None):
		fig = plt.figure()
		plt.xlabel('y(t)', fontsize=16)
		plt.ylabel('v(t)', fontsize=16)
		l1 = plt.plot(y,v)
		plt.setp(l1, linewidth=1, color='b', linestyle='-')
		if title:
			fig.suptitle(title, fontsize=20)
		plt.draw()

	def plot2(self, t, y, title=None):
		fig = plt.figure()
		ax = fig.add_subplot(111)
		ax.spines['left'].set_position('zero')
		ax.spines['right'].set_color('none')
		ax.spines['bottom'].set_position('zero')
		ax.spines['top'].set_color('none')
		l1 = plt.plot(t,y)
		plt.setp(l1, linewidth=0.5, color='red', linestyle='-')
		if title:
			fig.suptitle(title, fontsize=20)
		plt.xlabel('t', fontsize=16)
		plt.ylabel('y(t)', fontsize=16)
		plt.draw()

	def show(self):
		plt.show()