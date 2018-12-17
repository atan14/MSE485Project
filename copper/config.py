# Copyright (c)  2014  Mikael Leetmaa
#
# This file is part of the KMCLib project distributed under the terms of the
# GNU General Public License version 3, see <http://www.gnu.org/licenses/>.
#

from KMCLib import *
import random

# -----------------------------------------------------------------------------
# Unit cell

cell_vectors = [[   5.762860e+00,   0.000000e+00,   0.000000e+00],
                [   0.000000e+00,   5.762860e+00,   0.000000e+00],
                [   0.000000e+00,   0.000000e+00,   5.762860e+00]]

basis_points = [[0.0, 0.0, 0.0], #0
                [0.25, 0.75, 0.75], #1
                [0.5, 0.0, 0.5],#2
                [0.0, 0.5, 0.5],#3
                [0.5, 0.5, 0.0], #4
                [0.75, 0.25, 0.75],#5
                [0.75, 0.75, 0.25], #6
                [0.25, 0.25, 0.25]] #7

unit_cell = KMCUnitCell(
    cell_vectors=cell_vectors,
    basis_points=basis_points)

# -----------------------------------------------------------------------------
# Lattice
# Note that we run with periodicity in y and z but not in x.
lattice = KMCLattice(
    unit_cell=unit_cell,
    repetitions=(10,10,10),
    periodic=(True, True, True))

# -----------------------------------------------------------------------------
# Configuration

num_atoms = 10*10*10*len(basis_points)

types = ['Ge']*num_atoms
for i in range(40):
    types[random.randint(1, num_atoms)] = 'V'
idx = random.randint(1, num_atoms)
types[idx] = 'B'

possible_types = ['Ge', 'B', 'V']

configuration = KMCConfiguration(
    lattice=lattice,
    types=types,
    possible_types=possible_types)
