import numpy as np
from src.gates import rx, ry, rz


def test_rx_zero():
    # Appel de la fonction avec une valeur connue (ex: angle 0)
    resultat = rx(0.0)
    attendu = np.array([[1.0, 0.0], [0.0, 1.0]])

    # Vérification (Assertion)
    assert np.allclose(resultat, attendu)

def test_rx_vecteur_pi():
    # 1. Appel de la fonction avec une valeur connue (ex: angle 0)
    porte = rx(np.pi)
    vecteur = np.array([ 1,0])
    resultat = porte @ vecteur

    attendu = np.array([0, -1j])

    # 3. Vérification (Assertion)
    assert np.allclose(resultat, attendu)

def test_rx_unitary():
    porte = np.array(rx(2.0))
    unitary = porte @ porte.conj().T

    attendu = [1,0], [0,1]

    assert np.allclose(unitary, attendu)

def test_ry_unitary():
    porte = np.array(ry(2.0))
    unitary = porte @ porte.conj().T

    attendu = [1,0], [0,1]

    assert np.allclose(unitary, attendu)

def test_rz_unitary():
    porte = np.array(rz(2.0))
    unitary = porte @ porte.conj().T

    attendu = [1,0], [0,1]

    assert np.allclose(unitary, attendu)

