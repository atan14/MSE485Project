# Copyright (c)  2014  Mikael Leetmaa
#
# This file is part of the KMCLib project distributed under the terms of the
# GNU General Public License version 3, see <http://www.gnu.org/licenses/>.
#

from KMCLib import *
import numpy as np

# -----------------------------------------------------------------------------
# Interactions

# Define functions to generate processes.

def interstitial_near_jump(elements_before, elements_after, rate_constant):
    from KMCLib import KMCProcess
    from operator import add

    basis_points = [[0.0, 0.0, 0.0],  # 0
                    [0.5, 0.5, 0.5],  # 1
                    [0.25, 0.75, 0.75],  # 2
                    [0.25, 0.25, 0.75],  # 3
                    [0.5, 0.0, 0.5],  # 4
                    [0.25, 0.75, 0.25],  # 5
                    [0.0, 0.5, 0.5],  # 6
                    [0.75, 0.75, 0.75],  # 7
                    [0.5, 0.5, 0.0],  # 8
                    [0.75, 0.25, 0.25],  # 9
                    [0.75, 0.25, 0.75],  # 10
                    [0.0, 0.0, 0.5],  # 11
                    [0.75, 0.75, 0.25],  # 12
                    [0.5, 0.0, 0.0],  # 13
                    [0.25, 0.25, 0.25],  # 14
                    [0.0, 0.5, 0.0]]  # 15
    direction1 = [[0.25, 0.25, 0.25],
                  [-0.25, -0.25, 0.25],
                  [-0.25, 0.25, -0.25],
                  [0.25, -0.25, -0.25]]
    direction2 = [[-0.25, -0.25, -0.25],
                  [-0.25, 0.25, 0.25],
                  [0.25, -0.25, 0.25],
                  [0.25, 0.25, -0.25]]

    basis_dir1 = [basis_points[1], basis_points[11], basis_points[13], basis_points[15]]
    basis_dir2 = [basis_points[3], basis_points[5], basis_points[7], basis_points[9]]

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


def interstitial_far_jump(elements_before, elements_after, rate_constant):
    from operator import add, sub, mod
    from KMCLib import KMCProcess

    basis_points = [[0.0, 0.0, 0.0],  # 0
                    [0.5, 0.5, 0.5],  # 1
                    [0.25, 0.75, 0.75],  # 2
                    [0.25, 0.25, 0.75],  # 3
                    [0.5, 0.0, 0.5],  # 4
                    [0.25, 0.75, 0.25],  # 5
                    [0.0, 0.5, 0.5],  # 6
                    [0.75, 0.75, 0.75],  # 7
                    [0.5, 0.5, 0.0],  # 8
                    [0.75, 0.25, 0.25],  # 9
                    [0.75, 0.25, 0.75],  # 10
                    [0.0, 0.0, 0.5],  # 11
                    [0.75, 0.75, 0.25],  # 12
                    [0.5, 0.0, 0.0],  # 13
                    [0.25, 0.25, 0.25],  # 14
                    [0.0, 0.5, 0.0]]  # 15
    direction1 = [[0.25, 0.25, 0.25],
                  [-0.25, -0.25, 0.25],
                  [-0.25, 0.25, -0.25],
                  [0.25, -0.25, -0.25]]
    direction2 = [[-0.25, -0.25, -0.25],
                  [-0.25, 0.25, 0.25],
                  [0.25, -0.25, 0.25],
                  [0.25, 0.25, -0.25]]

    basis_dir1 = [basis_points[1], basis_points[11], basis_points[13], basis_points[15]]
    basis_dir2 = [basis_points[3], basis_points[5], basis_points[7], basis_points[9]]

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

def substitutional_near_jump(elements_before, elements_after, rate_constant):
    from operator import add
    from KMCLib import KMCProcess

    basis_points = [[0.0, 0.0, 0.0],  # 0
                    [0.5, 0.5, 0.5],  # 1
                    [0.25, 0.75, 0.75],  # 2
                    [0.25, 0.25, 0.75],  # 3
                    [0.5, 0.0, 0.5],  # 4
                    [0.25, 0.75, 0.25],  # 5
                    [0.0, 0.5, 0.5],  # 6
                    [0.75, 0.75, 0.75],  # 7
                    [0.5, 0.5, 0.0],  # 8
                    [0.75, 0.25, 0.25],  # 9
                    [0.75, 0.25, 0.75],  # 10
                    [0.0, 0.0, 0.5],  # 11
                    [0.75, 0.75, 0.25],  # 12
                    [0.5, 0.0, 0.0],  # 13
                    [0.25, 0.25, 0.25],  # 14
                    [0.0, 0.5, 0.0]]  # 15

    direction1 = [[0.25, 0.25, 0.25],
                  [-0.25, -0.25, 0.25],
                  [-0.25, 0.25, -0.25],
                  [0.25, -0.25, -0.25]]
    direction2 = [[-0.25, -0.25, -0.25],
                  [-0.25, 0.25, 0.25],
                  [0.25, -0.25, 0.25],
                  [0.25, 0.25, -0.25]]



    basis_dir1 = [basis_points[0], basis_points[4], basis_points[6], basis_points[8]]
    basis_dir2 = [basis_points[2], basis_points[10], basis_points[12], basis_points[14]]

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
    from KMCLib import KMCProcess

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


def combined_near_jump(elements_before, elements_after, rate_constant,
                       start_from_interstitial=True):
    from operator import add, sub, mod
    from KMCLib import KMCProcess

    basis_points = [[0.0, 0.0, 0.0],  # 0
                    [0.5, 0.5, 0.5],  # 1
                    [0.25, 0.75, 0.75],  # 2
                    [0.25, 0.25, 0.75],  # 3
                    [0.5, 0.0, 0.5],  # 4
                    [0.25, 0.75, 0.25],  # 5
                    [0.0, 0.5, 0.5],  # 6
                    [0.75, 0.75, 0.75],  # 7
                    [0.5, 0.5, 0.0],  # 8
                    [0.75, 0.25, 0.25],  # 9
                    [0.75, 0.25, 0.75],  # 10
                    [0.0, 0.0, 0.5],  # 11
                    [0.75, 0.75, 0.25],  # 12
                    [0.5, 0.0, 0.0],  # 13
                    [0.25, 0.25, 0.25],  # 14
                    [0.0, 0.5, 0.0]]  # 15
    direction1 = [[0.25, 0.25, 0.25],
                  [-0.25, -0.25, 0.25],
                  [-0.25, 0.25, -0.25],
                  [0.25, -0.25, -0.25]]
    direction2 = [[-0.25, -0.25, -0.25],
                  [-0.25, 0.25, 0.25],
                  [0.25, -0.25, 0.25],
                  [0.25, 0.25, -0.25]]

    if start_from_interstitial:
        basis_dir2 = [basis_points[1], basis_points[11], basis_points[13], basis_points[15]]
        basis_dir1 = [basis_points[3], basis_points[5], basis_points[7], basis_points[9]]
    else:
        basis_dir2 = [basis_points[0], basis_points[4], basis_points[6], basis_points[8]]
        basis_dir1 = [basis_points[2], basis_points[10], basis_points[12], basis_points[14]]

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


T = 800  # Kelvin
beta = 1 / (8.617E-5 * T)  # eV

# Boron - Vacancy interstitial jump.
Ea_int_near_BVJump = 0.35  # eV
Ea_int_far_BVJump = 2.30  # eV

rate_constant_int_near_BVJump = np.exp(-Ea_int_near_BVJump * beta) / (
        4 * np.exp(-Ea_int_near_BVJump * beta) + 12 * np.exp(-Ea_int_far_BVJump * beta))
rate_constant_int_far_BVJump = np.exp(-Ea_int_far_BVJump * beta) / (
        4 * np.exp(-Ea_int_near_BVJump * beta) + 12 * np.exp(-Ea_int_far_BVJump * beta))

# Boron - Vacancy substitutional jump
Ea_sub_near_BVJump = 1.92
Ea_sub_far_BVJump = 6.02

rate_constant_sub_near_BVJump = np.exp(-Ea_sub_near_BVJump * beta) / (
        4 * np.exp(-Ea_sub_near_BVJump * beta) + 12 * np.exp(-Ea_sub_far_BVJump * beta))
rate_constant_sub_far_BVJump = np.exp(-Ea_sub_far_BVJump * beta) / (
        4 * np.exp(-Ea_sub_near_BVJump * beta) + 12 * np.exp(-Ea_sub_far_BVJump * beta))

# Germanium - Vacancy substitutional jump
Ea_GeVJump = 0.15

rate_constant_GeV = 0.25

# Interstitial-Substitutional jump
Ea_intsubjump = 0.011

rate_constant_intsubjump = 0.25


from config import boron_site

processes = []
processes += interstitial_near_jump(['B', 'V'], ['V', 'B'], rate_constant_int_near_BVJump)
processes += interstitial_far_jump(['B', 'V'], ['V', 'B'], rate_constant_int_far_BVJump)
processes += substitutional_near_jump(['B', 'V'], ['V', 'B'], rate_constant_sub_near_BVJump)
processes += substitutional_far_jump(['B', 'V'], ['V', 'B'], rate_constant_sub_far_BVJump)
processes += substitutional_near_jump(['Ge', 'V'], ['V', 'Ge'], rate_constant_GeV)
# whether the boron atom is at interstitial site or substitutional site
processes += combined_near_jump(['B', 'V'], ['V', 'B'],
                                rate_constant_intsubjump, start_from_interstitial=boron_site%2)


# The final interactions object.
interactions = KMCInteractions(
    processes=processes,
    implicit_wildcards=True)
