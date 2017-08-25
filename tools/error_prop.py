#Branching ratio calculation and error propagation calculation for the alpha lab
#BR = 0.5(counts_sf_1 + counts_sf_2)/(0.5(counts_sf_1 + counts_sf_2) + counts_a)
import numpy as np

#Input values, counts and errors from TUKAN
type = 1 #type of calculation, 1 sf measurement or 2

if type == 2:
    counts_sf_1 = 5228/2
    counts_sf_2 = 5228/2
    counts_a = 202741

    perc_err = 0.1
    
    #Branching ratio calculation
    num = 0.5*(counts_sf_1 + counts_sf_2)
    den = 0.5*(counts_sf_1 + counts_sf_2) + counts_a
    BR = num/den
    
    #Error calculation
    err_sf_1 = perc_err*counts_sf_1
    err_sf_2 = perc_err*counts_sf_2
    err_a = perc_err*counts_a
    
    err_num = np.sqrt(err_sf_1**2 + err_sf_2**2)
    err_den = np.sqrt(err_sf_1**2 + err_sf_2**2 + err_a**2)
    
    err_BR = BR*np.sqrt( (err_num/num)**2 + (err_den/den)**2 )
    
    #print the result
    print 'Branching ratio = %f %% +/- %f' % (BR*100, err_BR*100)

elif type == 1:
    counts_sf_1 = 5228
    counts_a = 202741

    perc_err = 0.1
    
    #Branching ratio calculation
    num = 0.5*(counts_sf_1)
    den = 0.5*(counts_sf_1) + counts_a
    BR = num/den
    
    #Error calculation
    err_sf_1 = perc_err*counts_sf_1
    err_a = perc_err*counts_a
    
    err_num = np.sqrt(err_sf_1**2)
    err_den = np.sqrt(err_sf_1**2 + err_a**2)
    
    err_BR = BR*np.sqrt( (err_num/num)**2 + (err_den/den)**2 )
    
    #print the result
    print 'Branching ratio = %f %% +/- %f' % (BR*100, err_BR*100)
