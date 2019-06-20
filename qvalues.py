import atom
import numpy as np 
import random as rd 


def charge_sum(atom_list):
	"""
	Sums the charges in a list of atom objects

	Parameters: 
	-----------
	atom_list : list atom object
		The list of atoms whose charges you would like to add

	Returns:
	--------
	charge : int
		The total charge given as a number of elementary charges
	"""

	charge = 0

	for atom in atom_list:
		charge = charge + atom.charge

	return charge

def mass_sum(atom_list):
	"""
	Sums the masses in a list of atom objects

	Parameters: 
	-----------
	atom_list : list atom object
		The list of atoms whose masses you would like to add

	Returns:
	--------
	charge : float
		The total mass in AMU
	"""

	mass = 0

	for atom in atom_list:
		mass = mass + atom.mass

	return mass

def charge_balanced(reactants, products):
	"""
	Checks that charge is conserved in a nuclear reaction.

	Parameters:
	-----------
	reactants : list atom object
		a list of the atoms in a nuclear reaction
	products : list atom object
		a list of the atoms produced by a nuclear reaction 

	Returns:
	--------
	Boolean
	"""

	if charge_sum(reactants) == charge_sum(products):
		return True
	else:
		return False

def balance_charge(reactants, products):
	"""
	Balances the charge by adding electrons to one side until charge is balanced.

	Parameters: 
	-----------
	reactants : list atom object
		a list of the atoms in a nuclear reaction
	products : list atom object
		a list of the atoms produced by a nuclear reaction

	Returns:
	--------
	reac_balanced, prod_balanced: 
		These are a list of atom objects that have balanced charge between them.
	"""

	reac_balanced = reactants
	prod_balanced = products

	e = atom.electron

	while not charge_balanced(reac_balanced, prod_balanced):

		if charge_sum(reac_balanced) < charge_sum(prod_balanced):
			prod_balanced.append(e) #adds electron to products.
		else:
			reac_balanced.append(e)

	return reac_balanced, prod_balanced


def qvalue(reactants, products):
	"""
	Calculates the q value of a binary nuclear reaction

	Parameters: 
	-----------
	reactants : list atom object
		a list of the atoms in a nuclear reaction
	products : list atom object
		a list of the atoms produced by a nuclear reaction

	Returns:
	--------
	qvalue : float
		The qvalue for the reaction in MeV
	"""
	MeV = 931.5 # a conversion factor 

	if charge_balanced(reactants, products):
		qvalue = mass_sum(reactants) - mass_sum(products)

	else:
		reac_balanced, prod_balanced = balance_charge(reactants, products)
		qvalue = mass_sum(reac_balanced) - mass_sum(prod_balanced)

	return qvalue*MeV


if __name__ == '__main__':
	
	C13 = atom.atom([13, 6, 13.0033548378])
	C12 = atom.atom([12, 6, 12.0])
	C14 = atom.atom([14, 6, 14.003241988])
	N14 = atom.atom([14, 7, 14.0030740052])
	
	

	proton = atom.atom([1, 1, 1.0078250321], charge = 1)


	deuteron = atom.atom([2, 1, 2.0135532127], charge = 1)
	tritium = atom.atom([3, 1, 3.0160492])

	O16 = atom.atom([16, 8, 15.994915])

	B11 = atom.atom([11, 5, 11.0093055])


	print(qvalue([C13, deuteron],[C12, tritium]))
	print(qvalue([N14, atom.neutron],[B11, atom.alpha]))
