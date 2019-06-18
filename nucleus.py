import numpy as np 
import pandas as pd
import sys



class nucleus(object):
	"""
	A nucleus of an atom, with a charge +Ze.
	"""

	def __init__(self, data, energy=None, decay=None):
		"""
		Parameters:
		-----------
		data : list of float 
			This is a list of [A, Z, mass]
			Z is the number of protons
			A is the mass number
			mass is the average mass from the periodic table, 
			unless otherwise specified, in MeV
		energy : float
			The energy of the nucleus in MeV.
		decay : float, [0, 1]
			A float between the values [0, 1] inclusive. 
			Default is none.
			Gives the probability of decaying after an arbitrary
			timestep.
		"""
		super(nucleus, self).__init__()
		self.A = data[0]
		self.Z = data[1]
		self.N = self.A-self.Z
		self.mass = data[2]

		assert abs(self.A) - 0.5 < self.mass, "Mass is not close to A" 

	def decay(self):
		pass

def read_periodic_table(file_path):
	ptable = pd.read_csv(file_path)
	return ptable

def get_element(identifier, ptable):
	"""
	Retrieves a particular element from the periodic table

	Parameters:
	-----------
	identifier : string, int
		String is the atomic symbol
		int is the number of protons
	ptable : pandas dataframe
		A periodic table of the elements

	Returns:
	--------
	A, Z, mass
	"""

	if isinstance(identifier, str): 
		info = ptable.loc[ptable['Symbol'] == identifier]
		info = info.values.tolist()
		mass = info[0][3]
		Z = info[0][0]
		A = round(mass)
		return A, Z, mass
	elif isinstance(identifier, int):
		info = ptable.loc[ptable['Atomic Number'] == identifier]
		info = info.values.tolist()
		mass = info[0][3]
		Z = info[0][0]
		A = round(mass)
		return A, Z, mass



if __name__ == '__main__':
	
	path = "ptable.csv"
	ptable = read_periodic_table(path)
	H = nucleus(get_element(1, ptable))
	Li = nucleus(get_element('Li', ptable))
