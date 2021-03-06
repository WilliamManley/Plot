import glob
import matplotlib.pyplot as plt
plt.style.use('seaborn-dark')
import numpy as np
import pandas as pd


#1: initial tolerance files
filenames_1 = ["Processed/Simulation1/logs/p_0", "Processed/Simulation1/logs/p_1", "Processed/Simulation1/logs/Ux_0", "Processed/Simulation1/logs/Uy_0", "Processed/Simulation1/logs/Uz_0", "Processed/Simulation1/logs/k_0", "Processed/Simulation1/logs/epsilon_0"]

#2: final tolerance files
filenames_2 = ["Processed/Simulation1/logs/pFinalRes_0", "Processed/Simulation1/logs/pFinalRes_1", "Processed/Simulation1/logs/UxFinalRes_0", "Processed/Simulation1/logs/UyFinalRes_0", "Processed/Simulation1/logs/UzFinalRes_0", "Processed/Simulation1/logs/kFinalRes_0", "Processed/Simulation1/logs/epsilonFinalRes_0"]

#3: number of iterations files
filenames_3 = ["Processed/Simulation1/logs/pIters_0", "Processed/Simulation1/logs/pIters_1", "Processed/Simulation1/logs/UxIters_0", "Processed/Simulation1/logs/UyIters_0", "Processed/Simulation1/logs/UzIters_0", "Processed/Simulation1/logs/kIters_0", "Processed/Simulation1/logs/epsilonIters_0"]

#read amnd generate dataframe from txt files:
initial_tolerance_df = [pd.read_csv(filename, names=[filename[5:]], sep="\t", engine='python') for filename in filenames_1]
final_tolerance_df = [pd.read_csv(filename, names=[filename[5:]], sep="\t", engine='python') for filename in filenames_2]
num_iterations_df = [pd.read_csv(filename, names=[filename[5:]], sep="\t", engine='python') for filename in filenames_3]

# Combine the dataframes
initial_combined = pd.concat(initial_tolerance_df, ignore_index=False, axis=1)
final_combined = pd.concat(final_tolerance_df, ignore_index=False, axis=1)
num_iterations_combined = pd.concat(num_iterations_df, ignore_index=False, axis=1)

#relative tolerance calculations
#!!!Change range to fit number of simulations!!!
relative_combined = pd.DataFrame(np.random.randint(1, 5, size=(min(len(initial_combined), len(final_combined)), 7)), columns=filenames_1)
relative_combined.index = np.arange(1,len(relative_combined)+1)

for i in range(0, len(initial_tolerance_df)):
    relative_combined.iloc[:, i] = final_combined.iloc[:, i] / initial_combined.iloc[:, i]

#percentage change tolerance calculations
#!!!Change range to fit number of simulations!!!
percentage_combined = pd.DataFrame(np.random.randint(1, 5, size=(min(len(initial_combined), len(final_combined)), 7)), columns=filenames_1)
percentage_combined.index = np.arange(1,len(percentage_combined)+1)

for i in range(0, len(initial_tolerance_df)):
    percentage_combined.iloc[:, i] = ((initial_combined.iloc[:, i] - final_combined.iloc[:, i]) / initial_combined.iloc[:, i]) * 100

# define a figure, with subplots as an array "ax" 
fig, ax = plt.subplots(2,2)


#Generate plots:
ax[0, 0].plot(initial_combined)
ax[0, 1].plot(relative_combined)
ax[1, 0].plot(num_iterations_combined)
ax[1, 1].plot(percentage_combined)

# plot 1 - (initial) residuals time series

# (optional) add horizontal lines to plot for idea of residuals relaxations.
ax[0, 0].axhline(y=1.0e-05, color="black", linestyle='--')
ax[0, 0].axhline(y=1.0e-04, color="black", linestyle='-')
# instantaiate array for legend names
legend_1 = []
# obtain legend names from file names
for string in filenames_1:
    # desired name in legend
    new_string = string.replace("Processed/Simulation1/logs/", "")
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
#!!! fix label issues with starting x axis!!!
ax[0, 0].set_xlim(1, len(initial_combined))

# add legend to the plot
ax[0, 0].legend(legend_1)


# plot 2 - relative tol time series

# title of plot
ax[0, 1].set_title("Relative Tolerances vs. Iteration")
# x axis label
ax[0, 1].set_xlabel("Iteration")
# y axis label
ax[0, 1].set_ylabel("Relative Tolerances")
# log scale on y axis since skewed to small residuals
ax[0, 1].set_yscale("log")
# only plot to data range
ax[0, 1].set_xlim(1, len(relative_combined))

# add legend to the plot
ax[0, 1].legend(legend_1)


# plot 3 - number iterations at each timestep time series

# title of plot
ax[1, 0].set_title("Number Inner Iterations In SIMPLE Loop vs. Outer Iteration")
# x axis label
ax[1, 0].set_xlabel("Outer Iteration")
# y axis label
ax[1, 0].set_ylabel("Number Inner Iterations")
# log scale on y axis since skewed to small residuals
#ax[1, 0].set_yscale("log")
# only plot to data range
ax[1, 0].set_xlim(1, len(num_iterations_combined))


# add legend to the plot
ax[1, 0].legend(legend_1)

# plot 4 - % change in initial to final tolerance time series.

# title of plot
ax[1, 1].set_title("Percentage change")
# x axis label
ax[1, 1].set_xlabel("Iteration")
# y axis label
ax[1, 1].set_ylabel("Percentage Change")
# only plot to data range
ax[1, 1].set_xlim(1, len(percentage_combined))

# add legend to the plot
ax[1, 1].legend(legend_1)


# force plot to display in full-screen
manager = plt.get_current_fig_manager()
manager.resize(*manager.window.maxsize())

# display plot until closed
plt.show()

