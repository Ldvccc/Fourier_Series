import numpy as np

def apply_1q(gate, state) -> list:

    return np.array(gate) @ np.array(state)

def expval_z(state):
    psi = np.array(state)
    z = np.array([[1,0], [0, -1]])

    return np.real(np.vdot(psi, z @ psi))