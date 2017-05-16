# Experiment.py
# Last modified: 16/05/2017
# Bradley Kavanagh

import numpy as np
import sys
from scipy.interpolate import interp1d

base_dir = '../../detectors/'

class Experiment:
    
    #Initialisation
    def __init__(self, expt_name, run_label):
        
        self.expt_name = expt_name
        self.run_label = run_label
        
        #Read in data
        runs_data = np.genfromtxt(base_dir + expt_name +'/' + expt_name +'_runs.dat',
            names=True, comments='-', missing_values='-1', \
            dtype=None)
        
        #List column headings
        names = runs_data.dtype.names
        

        #Determine which row we want
        Nrows = len(runs_data)
        row_num = -1
        for i in range(Nrows):
            if (run_label in runs_data[i]):
                row_num = i
        if (row_num == -1):
            print " Experiment.py: Run label '" + run_label+ "' not found..."
            sys.exit()
 
        #Create a dictionary for the different column headings
        self.run_info = dict((x, y) for x, y in zip(names, runs_data[row_num]))
        #You can now access 'exposure', 'E_min', 'E_max', 'N_obs' as you like
        #using run_info['exposure'], etc.

        #Load in other data files
        
        #Efficiency
        eff_data = np.loadtxt(base_dir + expt_name + '/' + self.run_info["Efficiency_file"])
        self.efficiency = interp1d(eff_data[:,0], eff_data[:,1], bounds_error=False, fill_value=0.0)
    
        
    