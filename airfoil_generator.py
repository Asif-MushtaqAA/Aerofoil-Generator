import math
import matplotlib.pyplot 
import numpy as np
import sys
import os
import random

module_path = os.path.abspath(os.path.join('..', 'libairfoil'))
if module_path not in sys.path:
    sys.path.append(module_path)

import libairfoil.parsec
# The libairfoil.parsec module is from the repository by mbodmer on GitHub
# GitHub repository: https://github.com/mbodmer/libairfoil/tree/master

def generate_jfoil_string(upper_limits, lower_limits):
    '''
    Generate a random jfoil_string with values within the provided limits.
    
    upper_limits: List of upper limits for the 11 variables.
    lower_limits: List of lower limits for the 11 variables.
    '''
    params = []
    for upper, lower in zip(upper_limits, lower_limits):
        params.append(random.uniform(lower, upper))
    
    jfoil_string = 'Parsec-11 [' + ':'.join(map(str, params)) + ']'
    return jfoil_string, params

def create_and_save_airfoil(jfoil_string, airfoil_number, params):
    '''
    Create an airfoil from the jfoil_string and save its coordinates to a file.
    
    jfoil_string: The string containing the airfoil parameters.
    airfoil_number: The number of the airfoil to label the file.
    '''
    params_obj = libairfoil.parsec.Parameters()
    params_obj.load_from_javafoil_parsec11(jfoil_string)
    
    airfoil = libairfoil.parsec.Airfoil(params_obj)
    
    theta_up = np.linspace(np.pi, 0, 87) # Change number of points as required
    x = 0.5 * (1 - np.cos(theta_up))     # Change number of points as required
    
    theta_lo = np.linspace(0, np.pi, 89)
    y = 0.5 * (1 - np.cos(theta_lo))
    y = y[1:-1]
    
    z_up = airfoil.Z_up(x)
    z_lo = airfoil.Z_lo(y)
    
    matplotlib.pyplot.figure()
    z = np.linspace(0.0, 1.0, 87)
    matplotlib.pyplot.plot(z, airfoil.Z_up(z), 'r--', z, airfoil.Z_lo(z), 'b--')
    matplotlib.pyplot.grid(True)
    matplotlib.pyplot.show()
    
    # Save the coordinates to a text file
    filename = f'./data_geometry/{airfoil_number}.txt'
    with open(filename, 'w') as f:
       
        for coord in zip(x, z_up):
            f.write(f"{coord[0]}     {coord[1]}\n")
        
        for coord in zip(y, z_lo):
            f.write(f"{coord[0]}     {coord[1]}\n")
    
    print(f"Coordinates saved to {filename}")
    
    # Append the PARSEC parameters to the parsec_parameters.txt file
    with open('parsec_parameters.txt', 'a') as f:
        f.write(f"Airfoil {airfoil_number}:\n")
        f.write(', '.join(map(str, params)) + '\n')
        
def main():
    
    upper_limits = [0.02376,0.3564,0.09768,-0.69993,0.26015,-0.05709,0.34551,0,0,-2.09242,20.50213] #NACA2414 10% from baseline
    lower_limits = [0.01944,0.2916,0.07992,-0.57267,0.21285,-0.04671,0.28269,0,0,-1.71198,16.77447] #NACA2414 105 from baseline
    num_airfoils = 50  # Change this to the number of airfoils to be generated

    for i in range(num_airfoils):
        jfoil_string, params = generate_jfoil_string(upper_limits, lower_limits)
        create_and_save_airfoil(jfoil_string, i+1, params)


#Allows to generate n number of aerofoil from a baseline PARSEC parameter.
#Few Baseline PARSEC parameter:
# PARSEC	R_LE	    x_up	    z_up	    z_xx_up	        x_lo	    z_lo	        z_xx_lo	    z_te	    dz_te  alpha_te	    beta_te
#NACA2414	0.0216	    0.324	    0.0888	    -0.6363	        0.2365	    -0.0519	        0.3141	    0	        0	   -1.9022	    18.6383
#NACA0012	0.015	    0.3	        0.06	    -0.45	        0.3	        -0.06	        0.45	    0	        0      0.02	        19.5
#NACA2411	0.013678116	0.329828126	0.073704988	-0.551671401	0.235726325	-0.036048728	0.113115166	0.001143512	0	   0	        18.6259073
#NACA1411	0.013433782	0.320854905	0.064120752	-0.482270756	0.29338219	-0.045264073	0.303640714	0.000240859	0	   6.73342E-06	18.6344633


#Example implementation in console
# Define upper and lower limit from the baseline PARSEC parameters along with number of aerofoils to be generated in the main function.
# from airfoil_generator import main
# main()