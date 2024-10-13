# Aerofoil-Generator  
Script to generate n number of aerofoil from a baseline PARSEC parameter.  

Also includes an image generator script which can generate images of aerofoils at various angles of attack 

#Few Baseline PARSEC parameter:  
  PARSEC	R_LE	      x_up	      z_up	    z_xx_up	        x_lo	      z_lo	        z_xx_lo	    z_te	      dz_te  alpha_te	    beta_te  
#NACA2414	0.0216	    0.324	      0.0888	  -0.6363	        0.2365	    -0.0519	      0.3141	    0	          0	     -1.9022	    18.6383  
#NACA0012	0.015	      0.3	        0.06	    -0.45	          0.3	        -0.06	        0.45	      0	          0      0.02	        19.5  
#NACA2411	0.013678116	0.329828126	0.073704988	-0.551671401	0.235726325	-0.036048728	0.113115166	0.001143512	0	     0	          18.6259073  
#NACA1411	0.013433782	0.320854905	0.064120752	-0.482270756	0.29338219	-0.045264073	0.303640714	0.000240859	0	     6.73342E-06	18.6344633  


Example implementation in console  
Define upper and lower limit from the baseline PARSEC parameters along with number of aerofoils to be generated in the main function.  

from airfoil_generator import main  
main()
