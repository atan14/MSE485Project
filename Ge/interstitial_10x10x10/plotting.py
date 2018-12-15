import numpy as np
import matplotlib.pyplot as plt

append = '3_rate_constant_0_25'
filename = 'msd%s.data' %append
data = np.loadtxt(filename, skiprows=1)

time = data[:, 0]
msd_x = data[:, 1]
msd_y = data[:, 2]
msd_z = data[:, 3]
msd_xy = data[:, 4]
msd_xz = data[:, 5]
msd_yz = data[:, 6]
msd_xyz = data[:, 7]
std_x = data[:, 8]
std_y = data[:, 9]
std_z = data[:, 10]
std_xy = data[:, 11]
std_xz = data[:, 12]
std_yz = data[:, 13]
std_xyz = data[:, 14]
n_eff = data[:, 15]

fig, (ax1, ax2, ax3) = plt.subplots(1, 3)

ax1.plot(time, msd_x)
ax2.plot(time, msd_y)
ax3.plot(time, msd_z)

ax1.set_title('MSD_X')
ax2.set_title('MSD_Y')
ax3.set_title('MSD_Z')

ax2.set_xlabel('Time lag')
ax1.set_ylabel('MSD')

fig.set_size_inches((12, 3))

fig.savefig('interstitial%s.png' %append)
plt.show()