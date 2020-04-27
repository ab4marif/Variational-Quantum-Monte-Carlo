import numpy as np

def trialWaveFunction(alpha, r):

    r1 = np.linalg.norm(r[:,:3], axis = 1, keepdims = True)
    r2 = np.linalg.norm(r[:,3:], axis = 1, keepdims = True)
    r12 =  np.linalg.norm(r[:, :3]-r[:, 3:], axis = 1, keepdims = True)

    wf = np.exp(-2*r1)*np.exp(-2*r2)*np.exp(r12/(2*(1+alpha*r12)))
    return wf


def E_loc(alpha, r):
    r1_unit = r[:,:3] / np.linalg.norm(r[:, :3], axis = 1, keepdims = True)

    r2_unit = r[:,3:] / np.linalg.norm(r[:, 3:], axis = 1, keepdims = True)
    r12_unit = r1_unit - r2_unit
    r12 = np.linalg.norm(r[:, :3] - r[:, 3:], axis = 1, keepdims = True)
    E_loc = -4 + np.sum(r12_unit * (r[:, :3] - r[:, 3:]), axis = 1, keepdims = True) * 1/(r12*(1+alpha*r12)**2) - 1/(r12*(1+alpha*r12)**3) - 1/(4*(1+alpha*r12)**4) + 1/r12
    return E_loc

alpha = np.arange(0.05, 0.25, 0.025)

dimension = 6
