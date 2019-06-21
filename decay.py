import atom
import numpy as np 
import random as rd


def gamma(parent, energy=0):
	"""
	Produces a single daughter particle and an 
	energetic gamma ray/photon. Gamma rays are 
	produced by nuclear reactions.
	The daughter is typically a ground state or 
	lower excited state of the parent. 

	Parameters:
	-----------
	parent : atom object
		The parent atom/nucleus

	energy : float, optional
		The energy of the released gamma ray. 
		If not specified, the decay mode will 
		be chosen with probabilities. Should 
		be specified for current implementation.

	Returns:
	-------- 
	daughters : atom object or list atom objects
		The daughters produced by the decay mode.
	"""
	pass

def alpha(parent):
	"""
	Produces a single daughter nucleus and an 
	alpha particle, which is an ionized helium 
	atom. Nuclei tend to group themselves in to 
	alpha particles.

	Parameters:
	-----------
	parent : atom object
		The parent atom/nucleus

	Returns:
	-------- 
	daughters : atom object or list atom objects
		The daughters produced by the decay mode.
	"""
	pass

def beta(parent): #beta electron, default
	"""
	A neutron releases an electron. Z number
	increases. Daughters include electron (beta -)
	and anti-neutrino. This involves the weak-force.
	Z is not conserved.

	Parameters:
	-----------
	parent : atom object
		The parent atom/nucleus

	Returns:
	-------- 
	daughters : atom object or list atom objects
		The daughters produced by the decay mode.
	"""
	pass

def beta_p(parent): #beta-positron
	"""
	A proton releases a positron. Z number
	decreases. Daughters include positron (beta +)
	and a neutrino. This involves the weak force.
	Z is not conserved.

	Parameters:
	-----------
	parent : atom object
		The parent atom/nucleus

	Returns:
	-------- 
	daughters : atom object or list atom objects
		The daughters produced by the decay mode.
	"""	
	pass

def internal_conversion(parent):
	"""
	An excited parent nucleus transfers energy to 
	one of its orbital electrons and the electron
	is ejected. The products are the same, ionized,
	parent with its nucleus in the ground state and
	an electron.

	Parameters:
	-----------
	parent : atom object
		The parent atom/nucleus

	Returns:
	-------- 
	daughters : atom object or list atom objects
		The daughters produced by the decay mode.
	"""	
	pass

def electron_capture(parent):
	"""
	An electron is captured by a proton producing
	a neutron. Z number decreases, nucleus is in
	an excited state (energy equal to absorbed 
	electron) and a neutrino is released.
	Z is not conserved.

	Parameters:
	-----------
	parent : atom object
		The parent atom/nucleus

	Returns:
	-------- 
	daughters : atom object or list atom objects
		The daughters produced by the decay mode.
	"""
	pass

def neutron_decay(parent):
	"""
	A heavy, unstable, isotope ejects a neutron
	from the nucleus. Z is conserved. Produces a
	lighter isotope of the parent and a neutron.
	
	Parameters:
	-----------
	parent : atom object
		The parent atom/nucleus

	Returns:
	-------- 
	daughters : atom object or list atom objects
		The daughters produced by the decay mode.
	"""
	pass

def proton_decay(parent):
	"""
	A proton is ejected from the nucleus. 
	Z is not conserved. 

	Parameters:
	-----------
	parent : atom object
		The parent atom/nucleus

	Returns:
	-------- 
	daughters : atom object or list atom objects
		The daughters produced by the decay mode.
	"""
	pass

