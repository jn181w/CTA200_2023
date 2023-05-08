import numpy as np

def iter(z0, c, iteations):
    ze = np.abs(z0)**2 + c
    print(np.abs(ze) < np.abs(z0))
    i = 0
    while (np.abs(ze) > np.abs(z0)) and (i<iteations):
        i += 1 
        z0 = ze
        ze = np.abs(z0)**2 + c
        if np.isinf(np.abs(ze)):
            return 0

    if np.abs(ze) > np.abs(z0):
        return 0
    else:
        return 1