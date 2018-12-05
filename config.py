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

basis_points = [[   0.000000, 0.000000, 0.000000],
                [   0.500000, 0.500000, 0.500000],
                [   0.250000, 0.750000, 0.750000],
                [   0.250000, 0.250000, 0.750000],
                [   0.500000, 0.000000, 0.500000],
                [   0.250000, 0.750000, 0.250000],
                [   0.000000, 0.500000, 0.500000],
                [   0.750000, 0.750000, 0.750000],
                [   0.500000, 0.500000, 0.000000],
                [   0.750000, 0.250000, 0.250000],
                [   0.750000, 0.250000, 0.750000],
                [   0.000000, 0.000000, 0.500000],
                [   0.750000, 0.750000, 0.250000],
                [   0.500000, 0.000000, 0.000000],
                [   0.250000, 0.250000, 0.250000],
                [   0.000000, 0.500000, 0.000000]]

unit_cell = KMCUnitCell(
    cell_vectors=cell_vectors,
    basis_points=basis_points)

# -----------------------------------------------------------------------------
# Lattice
# Note that we run with periodicity in y and z but not in x.
lattice = KMCLattice(
    unit_cell=unit_cell,
    repetitions=(2,2,2),
    periodic=(True, True, True))

# -----------------------------------------------------------------------------
# Configuration

types = ['Ge']*128

for i in range(128):
    if (i % 2 == 1):
        types[i] = 'V'
types[15] = 'B'
print (types)

possible_types = ['Ge', 'B', 'V']

configuration = KMCConfiguration(
    lattice=lattice,
    types=types,
    possible_types=possible_types)
