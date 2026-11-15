import numpy as np
from src.gates import rx
from src.simulator import apply_1q, expval_z

def test_apply_1q():
    porte = rx(np.pi)
    vecteur = np.array([ 1,0])

    resultat = apply_1q(porte, vecteur)

    attendu = np.array([0, -1j])
    assert np.allclose(resultat, attendu)

def test_expval_z():

    val_ket0 = expval_z([1,0])
    assert np.allclose(val_ket0, 1.0)

    val_ket1 = expval_z([0,1])
    assert np.allclose(val_ket1, -1.0)

    val_ket0_1 = val_ket0 + val_ket1
    assert np.allclose(val_ket0_1, 0.0)

