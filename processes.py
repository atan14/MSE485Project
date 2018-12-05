# Copyright (c)  2014  Mikael Leetmaa
#
# This file is part of the KMCLib project distributed under the terms of the
# GNU General Public License version 3, see <http://www.gnu.org/licenses/>.
#

from KMCLib import *
# -----------------------------------------------------------------------------
# Interactions


# Boron - Vacancy jump.
elements_before = ['V', 'B']
elements_after  = ['B', 'V']

# Only on Oxygen sites.
basis_sites     = [1, 3, 5, 7, 9, 11, 13, 15]


#rates
rate_constant        = 1.0

# Fill the list of processes.
processes = []

coordinates = [[0.0, 0.0, 0.0],
               [0.25, 0.25, 0.25]]
processes.append( KMCProcess(coordinates=coordinates,
                             elements_before=elements_before,
                             elements_after=elements_after,
                             basis_sites=basis_sites,
                             rate_constant=rate_constant) )
coordinates = [[0.0, 0.0, 0.0],
               [-0.25, 0.25, -0.25]]
processes.append( KMCProcess(coordinates=coordinates,
                             elements_before=elements_before,
                             elements_after=elements_after,
                             basis_sites=basis_sites,
                             rate_constant=rate_constant) )
coordinates = [[0.0, 0.0, 0.0],
               [-0.25,-0.25, 0.25]]
processes.append( KMCProcess(coordinates=coordinates,
                             elements_before=elements_before,
                             elements_after=elements_after,
                             basis_sites=basis_sites,
                             rate_constant=rate_constant) )
coordinates = [[0.0, 0.0, 0.0],
               [0.25, -0.25, -0.25]]
processes.append( KMCProcess(coordinates=coordinates,
                             elements_before=elements_before,
                             elements_after=elements_after,
                             basis_sites=basis_sites,
                             rate_constant=rate_constant) )

# coordinates = [[0.5, 0.5, 0.5],
#                [0.75, 0.25, 0.25]]
# processes.append( KMCProcess(coordinates=coordinates,
#                              elements_before=elements_before,
#                              elements_after=elements_after,
#                              basis_sites=basis_sites,
#                              rate_constant=rate_constant) )
# coordinates = [[0.5, 0.5, 0.5],
#                [0.75, 0.75, 0.75]]
# processes.append( KMCProcess(coordinates=coordinates,
#                              elements_before=elements_before,
#                              elements_after=elements_after,
#                              basis_sites=basis_sites,
#                              rate_constant=rate_constant) )
# coordinates = [[0.5, 0.5, 0.5],
#                [0.25, 0.75, 0.25]]
# processes.append( KMCProcess(coordinates=coordinates,
#                              elements_before=elements_before,
#                              elements_after=elements_after,
#                              basis_sites=basis_sites,
#                              rate_constant=rate_constant) )
# coordinates = [[0.5, 0.5, 0.5],
#                [0.25, 0.25, 0.75]]
# processes.append( KMCProcess(coordinates=coordinates,
#                              elements_before=elements_before,
#                              elements_after=elements_after,
#                              basis_sites=basis_sites,
#                              rate_constant=rate_constant) )
#
# coordinates = [[0.25, 0.25, 0.25],
#                [0.5, 1.0, 0.0]]
# processes.append( KMCProcess(coordinates=coordinates,
#                              elements_before=elements_before,
#                              elements_after=elements_after,
#                              basis_sites=basis_sites,
#                              rate_constant=rate_constant) )
# coordinates = [[0.25, 0.25, 0.25],
#                [0.0, 0.5, 0.0]]
# processes.append( KMCProcess(coordinates=coordinates,
#                              elements_before=elements_before,
#                              elements_after=elements_after,
#                              basis_sites=basis_sites,
#                              rate_constant=rate_constant) )
# coordinates = [[0.25, 0.25, 0.25],
#                [0.0, 1.0, 0.5]]
# processes.append( KMCProcess(coordinates=coordinates,
#                              elements_before=elements_before,
#                              elements_after=elements_after,
#                              basis_sites=basis_sites,
#                              rate_constant=rate_constant) )
# coordinates = [[0.25, 0.25, 0.25],
#                [0.5, 0.5, 0.5]]
# processes.append( KMCProcess(coordinates=coordinates,
#                              elements_before=elements_before,
#                              elements_after=elements_after,
#                              basis_sites=basis_sites,
#                              rate_constant=rate_constant) )
#
# coordinates = [[0.25, 0.25, 0.75],
#                [0.5, 0.5, 0.5]]
# processes.append( KMCProcess(coordinates=coordinates,
#                              elements_before=elements_before,
#                              elements_after=elements_after,
#                              basis_sites=basis_sites,
#                              rate_constant=rate_constant) )
# coordinates = [[0.25, 0.25, 0.75],
#                [0.0, 0.5, 1.0]]
# processes.append( KMCProcess(coordinates=coordinates,
#                              elements_before=elements_before,
#                              elements_after=elements_after,
#                              basis_sites=basis_sites,
#                              rate_constant=rate_constant) )
# coordinates = [[0.25, 0.25, 0.75],
#                [0.0, 0.0, 0.5]]
# processes.append( KMCProcess(coordinates=coordinates,
#                              elements_before=elements_before,
#                              elements_after=elements_after,
#                              basis_sites=basis_sites,
#                              rate_constant=rate_constant) )
# coordinates = [[0.25, 0.25, 0.75],
#                [0.5, 0.0, 1.0]]
# processes.append( KMCProcess(coordinates=coordinates,
#                              elements_before=elements_before,
#                              elements_after=elements_after,
#                              basis_sites=basis_sites,
#                              rate_constant=rate_constant) )
#
# coordinates = [[0.75, 0.75, 0.75],
#                [0.5, 0.5, 0.5]]
# processes.append( KMCProcess(coordinates=coordinates,
#                              elements_before=elements_before,
#                              elements_after=elements_after,
#                              basis_sites=basis_sites,
#                              rate_constant=rate_constant) )
# coordinates = [[0.75, 0.75, 0.75],
#                [1.0, 0.5, 1.0]]
# processes.append( KMCProcess(coordinates=coordinates,
#                              elements_before=elements_before,
#                              elements_after=elements_after,
#                              basis_sites=basis_sites,
#                              rate_constant=rate_constant) )
# coordinates = [[0.75, 0.75, 0.75],
#                [0.5, 1.0, 1.0]]
# processes.append( KMCProcess(coordinates=coordinates,
#                              elements_before=elements_before,
#                              elements_after=elements_after,
#                              basis_sites=basis_sites,
#                              rate_constant=rate_constant) )
# coordinates = [[0.75, 0.75, 0.75],
#                [1.0, 1.0, 0.5]]
# processes.append( KMCProcess(coordinates=coordinates,
#                              elements_before=elements_before,
#                              elements_after=elements_after,
#                              basis_sites=basis_sites,
#                              rate_constant=rate_constant) )
#
# coordinates = [[0.75, 0.25, 0.25],
#                [0.5, 0.5, 0.5]]
# processes.append( KMCProcess(coordinates=coordinates,
#                              elements_before=elements_before,
#                              elements_after=elements_after,
#                              basis_sites=basis_sites,
#                              rate_constant=rate_constant) )
# coordinates = [[0.75, 0.25, 0.25],
#                [1.0, 0.5, 0.0]]
# processes.append( KMCProcess(coordinates=coordinates,
#                              elements_before=elements_before,
#                              elements_after=elements_after,
#                              basis_sites=basis_sites,
#                              rate_constant=rate_constant) )
# coordinates = [[0.75, 0.25, 0.25],
#                [0.5, 0.0, 0.0]]
# processes.append( KMCProcess(coordinates=coordinates,
#                              elements_before=elements_before,
#                              elements_after=elements_after,
#                              basis_sites=basis_sites,
#                              rate_constant=rate_constant) )
# coordinates = [[0.75, 0.25, 0.25],
#                [1.0, 0.0, 0.5]]
# processes.append( KMCProcess(coordinates=coordinates,
#                              elements_before=elements_before,
#                              elements_after=elements_after,
#                              basis_sites=basis_sites,
#                              rate_constant=rate_constant) )
#
# coordinates = [[0.0, 0.0, 0.5],
#                [0.25, 0.25, 0.75]]
# processes.append( KMCProcess(coordinates=coordinates,
#                              elements_before=elements_before,
#                              elements_after=elements_after,
#                              basis_sites=basis_sites,
#                              rate_constant=rate_constant) )
# coordinates = [[0.0, 0.0, 0.5],
#                [-0.25, 0.25, 0.25]]
# processes.append( KMCProcess(coordinates=coordinates,
#                              elements_before=elements_before,
#                              elements_after=elements_after,
#                              basis_sites=basis_sites,
#                              rate_constant=rate_constant) )
# coordinates = [[0.0, 0.0, 0.5],
#                [0.25, -0.25, 0.25]]
# processes.append( KMCProcess(coordinates=coordinates,
#                              elements_before=elements_before,
#                              elements_after=elements_after,
#                              basis_sites=basis_sites,
#                              rate_constant=rate_constant) )
# coordinates = [[0.0, 0.0, 0.5],
#                [-0.25, -0.25, 0.75]]
# processes.append( KMCProcess(coordinates=coordinates,
#                              elements_before=elements_before,
#                              elements_after=elements_after,
#                              basis_sites=basis_sites,
#                              rate_constant=rate_constant) )
#
# coordinates = [[0.5, 0.0, 0.0],
#                [0.75, 0.25, 0.25]]
# processes.append( KMCProcess(coordinates=coordinates,
#                              elements_before=elements_before,
#                              elements_after=elements_after,
#                              basis_sites=basis_sites,
#                              rate_constant=rate_constant) )
# coordinates = [[0.5, 0.0, 0.0],
#                [0.25, 0.25, 0.0]]
# processes.append( KMCProcess(coordinates=coordinates,
#                              elements_before=elements_before,
#                              elements_after=elements_after,
#                              basis_sites=basis_sites,
#                              rate_constant=rate_constant) )
# coordinates = [[0.5, 0.0, 0.0],
#                [0.25, -0.25, 0.25]]
# processes.append( KMCProcess(coordinates=coordinates,
#                              elements_before=elements_before,
#                              elements_after=elements_after,
#                              basis_sites=basis_sites,
#                              rate_constant=rate_constant) )
# coordinates = [[0.5, 0.0, 0.0],
#                [0.75, -0.25, 0.75]]
# processes.append( KMCProcess(coordinates=coordinates,
#                              elements_before=elements_before,
#                              elements_after=elements_after,
#                              basis_sites=basis_sites,
#                              rate_constant=rate_constant) )
#
# coordinates = [[0.0, 0.5, 0.0],
#                [0.25, 0.75, 0.25]]
# processes.append( KMCProcess(coordinates=coordinates,
#                              elements_before=elements_before,
#                              elements_after=elements_after,
#                              basis_sites=basis_sites,
#                              rate_constant=rate_constant) )
# coordinates = [[0.0, 0.5, 0.0],
#                [-0.25, 0.75, -0.25]]
# processes.append( KMCProcess(coordinates=coordinates,
#                              elements_before=elements_before,
#                              elements_after=elements_after,
#                              basis_sites=basis_sites,
#                              rate_constant=rate_constant) )
# coordinates = [[0.0, 0.5, 0.0],
#                [-0.25, 0.25, 0.25]]
# processes.append( KMCProcess(coordinates=coordinates,
#                              elements_before=elements_before,
#                              elements_after=elements_after,
#                              basis_sites=basis_sites,
#                              rate_constant=rate_constant) )
# coordinates = [[0.0, 0.5, 0.0],
#                [0.25, 0.25, -0.25]]
# processes.append( KMCProcess(coordinates=coordinates,
#                              elements_before=elements_before,
#                              elements_after=elements_after,
#                              basis_sites=basis_sites,
#                              rate_constant=rate_constant) )

# The final interactions object.
interactions = KMCInteractions(
    processes=processes,
    implicit_wildcards=True)
