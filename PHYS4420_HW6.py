"""
Title: PHYS 4420 HW6
Author: Jake R. Anderson
Professor: Dr. Steve Wasserbaech

Description:
A) Plot the Phase Velocity and Group Velocity as functions of Wavelength covering the Wavelength range from 10**-4 to
10**2 meters. Use log scales on both axes. Plot Phase Velocity vs Wavelength and plot Group Velocity vs Wavelength
individually.

B) Find the wavelength at which the Phase and Group velocities are equal. Plot both Phase and Group Velocities vs
Wavelength on the same figure and find their intersection point.

Function:
A) Given an equation using
. omega = [function]
. gravity = 9.8
. wave_number = unknown
. surface_tension = 0.0720
We are given a range of "lambda" values
Use the relation "lambda = (2 * pi) / wave_num" to find list of wave_num values
Now use relations:
1) Phase Velocity = Frequency / wave_num
2) Group Velocity = d(Frequency) / d(wave_num)
to find (1) and (2) vs lambda
Plot (1) vs Wavelength
Plot (2) vs Wavelength

B)
Plot both (1) and (2) vs Wavelength on the same figure

"""
import numpy as np
import matplotlib.pyplot as plt


def deep_water_waves(gravity, surface_tension, density, wave_number_list):
    ang_freq_list = []
    for wave_num in wave_number_list:
        ang_freq_list.append(np.sqrt((gravity * wave_num) + ((surface_tension * wave_num ** 3) / density)))
    return ang_freq_list


def wave_number(wavelengths):
    wave_num_list = []
    for wavelength in wavelengths:
        wave_num_list.append(2 * np.pi / wavelength)
    return wave_num_list


def phase_velocity(omega_freq, wave_number_list):
    velocity_list = []
    for index in range(len(omega_freq)):
        velocity_list.append(omega_freq[index] / wave_number_list[index])
    return velocity_list


def group_velocity(gravity, surface_tension, density, wave_number_list):
    group_velocity_list = []
    for wave_num in wave_number_list:
        denom = (gravity * wave_num) + ((surface_tension * wave_num ** 3) / density)
        vel_group = (1 / 2) * (1 / np.sqrt(denom)) * (gravity + (3 * surface_tension * wave_num ** 2) / density)
        group_velocity_list.append(vel_group)
    return group_velocity_list


# Define constants
sur_tension_a = 0.0720  # kg / s ** 2
grav_a = 9.8  # m / s ** 2
density_water_a = 1000  # kg / m ** 3
wavelength_list_a = np.logspace(-4, 2)

# Find wave number values then use them to find omega, phase, and group velocity
wave_numbers_a = wave_number(wavelength_list_a)
water_waves_omega_a = deep_water_waves(grav_a, sur_tension_a, density_water_a, wave_numbers_a)
phase_velocity_a = phase_velocity(water_waves_omega_a, wave_numbers_a)
group_velocity_a = group_velocity(grav_a, sur_tension_a, density_water_a, wave_numbers_a)

# Plot phase velocity vs wavelength
plt.figure(1)
plt.title('HW6(A.1) Phase Velocity vs Wavelength')
plt.xscale('log')
plt.yscale('log')
plt.plot(wavelength_list_a, phase_velocity_a)
plt.xlabel('wavelength (m)')
plt.ylabel('phase velocity')

# Plot group velocity vs wavelength
plt.figure(2)
plt.title('HW6(A.2) Group Velocity vs Wavelength')
plt.xscale('log')
plt.yscale('log')
plt.plot(wavelength_list_a, group_velocity_a)
plt.xlabel('wavelength (m)')
plt.ylabel('group velocity')
plt.show()

# Plot both phase and group velocities vs wavelength
plt.title('HW6(B) Phase Velocity and Group Velocity vs Wavelength')
plt.xscale('log')
plt.yscale('log')
plt.plot(wavelength_list_a, phase_velocity_a)
plt.plot(wavelength_list_a, group_velocity_a)
plt.figlegend(['Phase Velocity', 'Group Velocity'])
plt.xlabel('wavelength (m)')
plt.ylabel('phase and group velocities')
plt.show()
