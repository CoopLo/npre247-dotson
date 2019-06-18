import nucleus 
import numpy as np 
import pandas as pd 
import random as rd 


def binary_qvalue(projectile, target, heavy, light):
	"""
	Calculates the q value of a binary nuclear reaction

	Parameters:
	-----------
	projectile : nucleus object, float.
		nucleus object is a nucleus projectile, charged
		float is a photon energy, uncharged.
	target : nucleus oject

	Returns:
	--------
	qvalue : float
		The qvalue for the reaction in MeV
	"""
	MeV = 931.5 # a conversion factor 

	if isinstance(projectile, nucleus.nucleus):
		qvalue = ((projectile.mass + target.mass) - (heavy.mass+light.mass))
		return qvalue*MeV


if __name__ == '__main__':
	
	C13 = nucleus.nucleus([13, 6, 13.003354])
	C12 = nucleus.nucleus([12, 6, 12.0])
	C14 = nucleus.nucleus([14, 6, 14.003241988])
	N14 = nucleus.nucleus([14, 7, 14.0030740052])
	
	

	proton = nucleus.nucleus([1, 1, 1.0078250321])
	neutron = nucleus.nucleus([1, 0, 1.0086649233])

	deuteron = nucleus.nucleus([2, 1, 2.0135532127])
	tritium = nucleus.nucleus([3, 1, 3.0160492])

	O16 = nucleus.nucleus([16, 8, 15.994915])
	He4 = nucleus.nucleus([4, 2, 4.002603])

	Be11 = nucleus.nucleus([11, 4, 11.021658])

	# print(neutron.mass)
	# print(O16.mass)
	# print(C13.mass)
	# print(He4.mass)

	q = binary_qvalue(neutron, O16, C13, He4) #this one agrees with the answer in the book
	q2 = binary_qvalue(deuteron, C13, C12, tritium) #this one disagrees??? should be 1.311 MeV
	q3 = binary_qvalue(proton, C14, N14, neutron)#this one agrees with the answer in the book
	q4 = binary_qvalue(neutron, N14, Be11, He4)#this one disagrees??? should be -0.1582 MeV
	print(deuteron.mass)
	print(tritium.mass)
	print(q)
	print(q2)
	print(q3)
	print(q4)