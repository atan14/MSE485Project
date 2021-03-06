# Copyright (c)  2014  Mikael Leetmaa
#
# This file is part of the KMCLib project distributed under the terms of the
# GNU General Public License version 3, see <http://www.gnu.org/licenses/>.
#

from KMCLib import *

# -----------------------------------------------------------------------------
# Unit cell

cell_vectors = [[   5.762860e+00,   0.000000e+00,   0.000000e+00],
                [   0.000000e+00,   5.762860e+00,   0.000000e+00],
                [   0.000000e+00,   0.000000e+00,   5.762860e+00]]

basis_points = [[0.0, 0.0, 0.0], #0
                [0.5, 0.5, 0.5], #1
                [0.25, 0.75, 0.75], #2
                [0.25, 0.25, 0.75],#3
                [0.5, 0.0, 0.5],#4
                [0.25, 0.75, 0.25],#5
                [0.0, 0.5, 0.5],#6
                [0.75, 0.75, 0.75],#7
                [0.5, 0.5, 0.0], #8
                [0.75, 0.25, 0.25],#9
                [0.75, 0.25, 0.75],#10
                [0.0, 0.0, 0.5],#11
                [0.75, 0.75, 0.25], #12
                [0.5, 0.0, 0.0], #13
                [0.25, 0.25, 0.25], #14
                [0.0, 0.5, 0.0]] #15

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

types = ['Ge']*128

for i in range(128):
    if (i % 2 == 1):
        types[i] = 'V'
types[1] = 'B'
print (types)

possible_types = ['Ge', 'B', 'V']

configuration = KMCConfiguration(
    lattice=lattice,
    types=types,
    possible_types=possible_types)
