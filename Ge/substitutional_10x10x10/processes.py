# Copyright (c)  2014  Mikael Leetmaa
#
# This file is part of the KMCLib project distributed under the terms of the
# GNU General Public License version 3, see <http://www.gnu.org/licenses/>.
#

from KMCLib import *
# -----------------------------------------------------------------------------
# Interactions

# Define processes.
def substitutional_near_jump(elements_before, elements_after, rate_constant):
    from operator import add
    from KMCLib import *

    basis_points = [[0.0, 0.0, 0.0],  # 0
                    [0.25, 0.75, 0.75],  # 1
                    [0.5, 0.0, 0.5],  # 2
                    [0.0, 0.5, 0.5],  # 3
                    [0.5, 0.5, 0.0],  # 4
                    [0.75, 0.25, 0.75],  # 5
                    [0.75, 0.75, 0.25],  # 6
                    [0.25, 0.25, 0.25]]  # 7

    direction1 = [[0.25, 0.25, 0.25],
                  [-0.25, -0.25, 0.25],
                  [-0.25, 0.25, -0.25],
                  [0.25, -0.25, -0.25]]
    direction2 = [[-0.25, -0.25, -0.25],
                  [-0.25, 0.25, 0.25],
                  [0.25, -0.25, 0.25],
                  [0.25, 0.25, -0.25]]

    basis_dir1 = [basis_points[0], basis_points[2], basis_points[3], basis_points[4]]
    basis_dir2 = [basis_points[1], basis_points[5], basis_points[6], basis_points[7]]

    processes = []
    for basis_idx, basis in enumerate(basis_points):
        if basis in basis_dir1:
            for direction in direction1:
                jump1 = list(map(add, basis, direction))
                coordinates = [basis, jump1]
                processes.append(KMCProcess(coordinates=coordinates,
                                            elements_before=elements_before,
                                            elements_after=elements_after,
                                            basis_sites=[basis_idx],
                                            rate_constant=rate_constant))
        elif basis in basis_dir2:
            for direction in direction2:
                jump1 = list(map(add, basis, direction))
                coordinates = [basis, jump1]
                processes.append(KMCProcess(coordinates=coordinates,
                                            elements_before=elements_before,
                                            elements_after=elements_after,
                                            basis_sites=[basis_idx],
                                            rate_constant=rate_constant))
    return processes


def substitutional_far_jump(elements_before, elements_after, rate_constant):
    from operator import add, mod
    from KMCLib import *

    basis_points = [[0.0, 0.0, 0.0],  # 0
                    [0.25, 0.75, 0.75],  # 1
                    [0.5, 0.0, 0.5],  # 2
                    [0.0, 0.5, 0.5],  # 3
                    [0.5, 0.5, 0.0],  # 4
                    [0.75, 0.25, 0.75],  # 5
                    [0.75, 0.75, 0.25],  # 6
                    [0.25, 0.25, 0.25]]  # 7

    direction1 = [[0.25, 0.25, 0.25],
                  [-0.25, -0.25, 0.25],
                  [-0.25, 0.25, -0.25],
                  [0.25, -0.25, -0.25]]
    direction2 = [[-0.25, -0.25, -0.25],
                  [-0.25, 0.25, 0.25],
                  [0.25, -0.25, 0.25],
                  [0.25, 0.25, -0.25]]

    basis_dir1 = [basis_points[0], basis_points[2], basis_points[3], basis_points[4]]
    basis_dir2 = [basis_points[1], basis_points[5], basis_points[6], basis_points[7]]

    processes = []
    for basis_idx, basis in enumerate(basis_points):
        if basis in basis_dir1:
            for jump1 in direction1:
                loc1 = list(map(add, basis, jump1))
                basis_mapping = list(map(mod, loc1, [1, 1, 1]))
                if basis_mapping in basis_dir1:
                    for jump2 in direction1:
                        loc2 = list(map(add, loc1, jump2))
                        if basis != loc2:
                            coordinates = [basis, loc2]
                            processes.append(KMCProcess(coordinates=coordinates,
                                                        elements_before=elements_before,
                                                        elements_after=elements_after,
                                                        basis_sites=[basis_idx],
                                                        rate_constant=rate_constant))
                elif basis_mapping in basis_dir2:
                    for jump2 in direction2:
                        loc2 = list(map(add, loc1, jump2))
                        if basis != loc2:
                            coordinates = [basis, loc2]
                            processes.append(KMCProcess(coordinates=coordinates,
                                                        elements_before=elements_before,
                                                        elements_after=elements_after,
                                                        basis_sites=[basis_idx],
                                                        rate_constant=rate_constant))
        elif basis in basis_dir2:
            for jump1 in direction2:
                loc1 = list(map(add, basis, jump1))
                basis_mapping = list(map(mod, loc1, [1, 1, 1]))
                if basis_mapping in basis_dir1:
                    for jump2 in direction1:
                        loc2 = list(map(add, loc1, jump2))
                        if basis != loc2:
                            coordinates = [basis, loc2]
                            processes.append(KMCProcess(coordinates=coordinates,
                                                        elements_before=elements_before,
                                                        elements_after=elements_after,
                                                        basis_sites=[basis_idx],
                                                        rate_constant=rate_constant))
                elif basis_mapping in basis_dir2:
                    for jump2 in direction2:
                        loc2 = list(map(add, loc1, jump2))
                        if basis != loc2:
                            coordinates = [basis, loc2]
                            processes.append(KMCProcess(coordinates=coordinates,
                                                        elements_before=elements_before,
                                                        elements_after=elements_after,
                                                        basis_sites=[basis_idx],
                                                        rate_constant=rate_constant))

    return processes


T = 800  # Kelvin
beta = 1 / (8.617E-5 * T)  # eV

# Boron - Vacancy jump.
elements_after = ['V', 'B']
elements_before  = ['B', 'V']

#rates
E_A_near = 1.92  # eV
E_A_far = 6.02  # eV

rate_constant_near = np.exp(-E_A_near * beta) / (
            4 * np.exp(-E_A_near * beta) + 12 * np.exp(-E_A_far * beta))
rate_constant_far = np.exp(-E_A_far * beta) / (
            4 * np.exp(-E_A_near * beta) + 12 * np.exp(-E_A_far * beta))


# List all the processes
processes = []
processes = processes + substitutional_near_jump(elements_before, elements_after,
                                                 rate_constant_near)
processes = processes + substitutional_far_jump(elements_before, elements_after, rate_constant_far)

# Germanium - Vacancy jump
elements_before = ['Ge', 'V']
elements_after = ['V', 'Ge']

E_a = 0.15
rate_constant_near = np.exp(-E_A_near * beta) / (4 * np.exp(-E_A_near * beta))

processes = processes + substitutional_near_jump(elements_before, elements_after, rate_constant)

# The final interactions object.
interactions = KMCInteractions(
    processes=processes,
    implicit_wildcards=True)
