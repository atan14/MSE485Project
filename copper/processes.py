# Copyright (c)  2014  Mikael Leetmaa
#
# This file is part of the KMCLib project distributed under the terms of the
# GNU General Public License version 3, see <http://www.gnu.org/licenses/>.
#

from KMCLib import *
import numpy as np 
from operator import add
# -----------------------------------------------------------------------------
# Interactions




# Fill the list of processes.
def substitutional_near_jump(elements_before, elements_after, rate_constant):
    from operator import add
    from KMCLib import *
    basis_points = [[0.0, 0.0, 0.0], #0
                    [0.5, 0.5, 0.0], #1
                    [0.5, 0.0, 0.5],#2
                    [0.0, 0.5, 0.5]] #3

    direction = [[0.5, 0.0, 0.5],
                 [0.5, 0.0, -0.5],
                 [-0.5, 0.0, -0.5],
                 [-0.5, 0.0, 0.5],
                 [0.0, 0.5, 0.5],
                 [0.0, 0.5, -0.5],
                 [0.0, -0.5, 0.5],
                 [0.0, -0.5, -0.5],
                 [0.5, 0.5, 0.0],
                 [0.5, -0.5, 0.0],
                 [-0.5, 0.5, 0.0],
                 [-0.5, -0.5, 0.0]]


    processes = []
    i=0
    n=0
    while (i<len(basis_points)):
        while (n<len(direction)):
            jump1 = list(map(add, basis_points[i], direction[n]))
            coordinates = [basis_points[i], jump1]
            processes.append(KMCProcess(coordinates=coordinates,
                                        elements_before=elements_before,
                                        elements_after=elements_after,
                                        basis_sites=[i],
                                        rate_constant=rate_constant))
            n=n+1
        i=i+1
    return processes

#Set parameters
T = 800 #Kelvin
beta = 1/(8.617E-5 * T) # eV

# Copper - Vacancy jump.
elements_after = ['V', 'Cu']
elements_before  = ['Cu', 'V']

#rates
rate_constant        = .083333

#list all of the processes
processes = []
processes = processes + substitutional_near_jump(elements_before, elements_after, rate_constant)


# The final interactions object.
interactions = KMCInteractions(
    processes=processes,
    implicit_wildcards=True)
