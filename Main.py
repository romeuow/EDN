from Problem import ProblemClass as pc
from OneStep import OneStepClass as os

class MainClass:

	t,y = os.solver(os.ForwardEuler, pc.f4, pc.exactF4) 