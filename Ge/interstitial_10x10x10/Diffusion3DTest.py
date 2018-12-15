#!/usr/bin/env python

""" Module for testing a 3D diffusion system. """

# Copyright (c)  2014  Mikael Leetmaa
#
# This file is part of the KMCLib project distributed under the terms of the
# GNU General Public License version 3, see <http://www.gnu.org/licenses/>.
#

import unittest
import numpy
import os

# Import the interface.
from KMCLib import *
from KMCLib.Backend import Backend


# Implement the test.
class Diffusion3DTest(unittest.TestCase):
    """ Class for testing 3D diffusion. """

    def testRun(self):
        """ Run the model and check the results. """
        # Load the basic interactions and the initial configuration.
        directory = os.path.abspath(os.path.dirname(__file__))
        p_file    = os.path.join(directory, "processes.py")
        c_file    = os.path.join(directory,"config.py")
        interactions  = KMCInteractionsFromScript(p_file)
        configuration = KMCConfigurationFromScript(c_file)
        append = '_test1'
        traj_file_name = 'traj%s.py' %append
        msd_file_name = 'msd%s.data' %append
        cutoff = 20

        # Set the parameters.
        control_parameters = KMCControlParameters(number_of_steps=300000,
                                                  dump_interval=1000,
                                                  analysis_interval=1,
                                                  seed=1994669)

        # Setup the MSD analysis for tracking vacancy diffusion.
        msd_analysis = OnTheFlyMSD(history_steps=200,
                                   n_bins=100,
                                   t_max=100.0,
                                   track_type="V")

        # Put the model together and run.
        model = KMCLatticeModel(configuration, interactions)
        model.run(control_parameters,
                  trajectory_filename=traj_file_name,
                  analysis=[msd_analysis])

        if Backend.MPICommons.isMaster():
            # Save the analysis data to a file.
            with open(msd_file_name, 'w') as f:
                msd_analysis.printResults(f)
        Backend.MPICommons.barrier()

        # Read in the file content.
        with open(msd_file_name, 'r') as f:
            content = f.readlines()
        raw_data = []

        for row in content[1:]:
            row = [float(r) for r in row.split('\n')[0].split(' ') if r != '']
            raw_data.append(row)
        raw_data = numpy.array(raw_data)

        time = raw_data[:, 0]
        msd_x = raw_data[:, 1]
        msd_y = raw_data[:, 2]
        msd_z = raw_data[:, 3]
        msd_xy = raw_data[:, 4]
        msd_xz = raw_data[:, 5]
        msd_yz = raw_data[:, 6]
        msd_xyz = raw_data[:, 7]
        std_x = raw_data[:, 8]
        std_y = raw_data[:, 9]
        std_z = raw_data[:, 10]
        std_xy = raw_data[:, 11]
        std_xz = raw_data[:, 12]
        std_yz = raw_data[:, 13]
        std_xyz = raw_data[:, 14]
        n_eff = raw_data[:, 15]

        # X direction.
        # Confined dynamics in the X direction. Slope at large time lag
        # significantly smaller than slope at small time lag.
        D_x1 = fit(time[0:15],  msd[0:15],  std[0:15])
        D_x2 = fit(time[16:29], msd[16:29], std[16:29])
        D_x = fit(time[cutoff:], msd_x[cutoff:], std_x[cutoff:])

        # Y direction.
        # Flow motion in the Y direction. Slope is contant.
        D_y1 = fit(time[0:15],  msd[0:15],  std[0:15])
        D_y2 = fit(time[16:29], msd[16:29], std[16:29])
        D_y = fit(time[cutoff:], msd_y[cutoff:], std_y[cutoff:])

        # Z direction.
        # Flow motion in the Z direction. Slope at large time lag
        # significantly larger than slope at small time lag.
        D_z1 = fit(time[0:15],  msd[0:15],  std[0:15])
        D_z2 = fit(time[16:29], msd[16:29], std[16:29])
        D_z = fit(time[cutoff:], msd_z[cutoff:], std_z[cutoff:])

        print ("D_x1, D_x2, D_y1, D_y2, D_z1, D_z2", D_x1, D_x2, D_y1, D_y2, D_z1, D_z2)
        print ("D_x = %.5f, D_y = %.5f, D_z = %.5f" %(D_x, D_y, D_z))


def fit(time, msd, std):
    """ Helper function to get the slope of a msd curve with given errors."""
    # Setup the properly weighted least square fit problem.
    A = numpy.vstack([time, numpy.ones(len(time))]).T
    A = numpy.vstack([A[:,0]/std, A[:,1]/std]).T
    covariance = numpy.linalg.inv(numpy.dot(A.T,A))
    b = msd / std

    # Make the fit.
    fit = numpy.linalg.lstsq(A, b)

    # Get the diffusion coefficient and offset.
    D,offset  = fit[0]
    return D


if __name__ == '__main__':
    unittest.main()
