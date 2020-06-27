# dependancies
import glob
import matplotlib.pyplot as plt
import numpy as np
import string


# define files containing data for each plot

#1: initial tolerance files
filenames_1 = ["logs/p_0", "logs/p_1", "logs/Ux_0", "logs/Uy_0", "logs/Uz_0", "logs/k_0", "logs/epsilon_0"]

#2: final tolerance files
filenames_2 = ["logs/pFinalRes_0", "logs/pFinalRes_1", "logs/UxFinalRes_0", "logs/UyFinalRes_0", "logs/UzFinalRes_0", "logs/kFinalRes_0", "logs/epsilonFinalRes_0"]

#3: number of iterations files
filenames_3 = ["logs/pIters_0", "logs/pIters_1", "logs/UxIters_0", "logs/UyIters_0", "logs/UzIters_0", "logs/kIters_0", "logs/epsilonIters_0"]

# define seperate plots 
fig, ax = plt.subplots(2,2)



# read each file as useable data:

#1&2: initial tolerance data
for f in filenames_1:
    #read file
    initial_tolerance_data = np.loadtxt(f)
    initial_tolerance_time_steps = initial_tolerance_data[:,0]
    initial_tolerances = initial_tolerance_data[:,1]
    ax[0, 0].plot(initial_tolerance_time_steps, initial_tolerances)
    
#2: final tolerance data
for g in filenames_2:
    #read file
    final_tolerance_data = np.loadtxt(g)
    final_tolerance_time_steps = final_tolerance_data[:,0]
    final_tolerances = final_tolerance_data[:,1]

    # determine where simulation finished if it did
    relative_tolerance_time_steps = list(range(0,1000))
    
    # calculate relative tolerances
    relative_tolerances = (final_tolerances)/(initial_tolerances)

    # plot column 0 (time step / iteration) against (initial) residuals
    ax[0, 1].plot(relative_tolerance_time_steps, relative_tolerances)
    

#3: number iterations data
for h in filenames_3:
    #read file
    number_iterations_data = np.loadtxt(h)
    number_iterations_time_steps = number_iterations_data[:,0]
    number_iterations = number_iterations_data[:,1]

    # plot time step / iteration against relative tolerances
    ax[1, 0].plot(number_iterations_time_steps, number_iterations)
    
    



# relevant calculations before plotting

#2: relative tolerance calculation

# determine where simulation finished if it did
#relative_tolerance_time_steps = list(range(0,np.min(len(initial_tolerance_time_steps), len(final_tolerance_time_steps))))
#relative_tolerance_time_steps = list(range(0,1000))
# calculate relative tolerances
#relative_tolerances = (final_tolerances)/(initial_tolerances)


#!!! Not yet configured combining into single plot window. !!!#
# plot 1 - (initial) residuals time series

# (optional) add horizontal lines to plot for idea of residuals relaxations.
ax[0, 0].axhline(y=1.0e-05, color="black", linestyle='--')
ax[0, 0].axhline(y=1.0e-04, color="black", linestyle='-')
# instantaiate array for legend names
legend_1 = []
# obtain legend names from file names
for string in filenames_1:
    # desired name in legend
    new_string = string.replace("logs/", "")
    #add (to end) of legend
    legend_1.append(new_string)
# title of plot
ax[0, 0].set_title("Residual vs. Iteration")
# x axis label
ax[0, 0].set_xlabel("Iteration")
# y axis label
ax[0, 0].set_ylabel("Residual")
# log scale on y axis since skewed to small residuals
ax[0, 0].set_yscale("log")
# only plot to data range
ax[0, 0].set_xlim(0, len(initial_tolerance_time_steps))
#!!! plt.ylim() - figure this out so no white space in y direction !!!#

# add legend to the plot
ax[0, 0].legend(legend_1)



# plot 2 - relative tol time series

# instantaiate array for legend names
legend_2 = []
# obtain legend names from file names
for string in filenames_2:
    # desired name in legend
    new_string = string.replace("logs/", "")
    #add (to end) of legend
    legend_2.append(new_string)
# title of plot
ax[0, 1].set_title("Relative Tolerances vs. Iteration")
# x axis label
ax[0, 1].set_xlabel("Iteration")
# y axis label
ax[0, 1].set_ylabel("Relative Tolerances")
# log scale on y axis since skewed to small residuals
ax[0, 1].set_yscale("log")
# only plot to data range
ax[0, 1].set_xlim(0, len(relative_tolerance_time_steps))
#!!! plt.ylim() - figure this out so no white space in y direction !!!#

# add legend to the plot
ax[0, 1].legend(legend_2)



# plot 3 - number iterations at each timestep time series

# instantaiate array for legend names
legend_3 = []
# obtain legend names from file names
for string in filenames_3:
    # desired name in legend
    new_string = string.replace("logs/", "")
    #add (to end) of legend
    legend_3.append(new_string)
# title of plot
ax[1, 0].set_title("Number Inner Iterations In SIMPLE Loop vs. Outer Iteration")
# x axis label
ax[1, 0].set_xlabel("Outer Iteration")
# y axis label
ax[1, 0].set_ylabel("Number Inner Iterations")
# log scale on y axis since skewed to small residuals
ax[1, 0].set_yscale("log")
# only plot to data range
ax[1, 0].set_xlim(0, len(number_iterations_time_steps))
#!!! plt.ylim() - figure this out so no white space in y direction !!!#

# add legend to the plot
ax[1, 0].legend(legend_3)


# Generate the plots

# save plot in current directory
plt.savefig('figure.png')
# display plot until closed
plt.show()
