import numpy as np

def rx(theta) -> list:
    "Rotation Rx. Prend un angle en entrée et renvoie la matrice Rx"

    matrice = [[np.cos(theta/2), -1j*np.sin(theta/2)],[-1j*np.sin(theta/2), np.cos(theta/2)]]

    return matrice

def ry(theta) -> list:
    "Rotation Ry. Prend un angle en entrée et renvoie la matrice Ry"

    matrice = [[np.cos(theta/2), np.sin(theta/2)],[-np.sin(theta/2), np.cos(theta/2)]]

    return matrice

def rz(theta) -> list:
    "Rotation Rz. Prend un angle en entrée et renvoie la matrice Rz"

    matrice = [[np.cos(theta/2) -1j*np.sin(theta/2), 0],[0, np.cos(theta/2) + 1j*np.sin(theta/2)]]

    return matrice

def rotation(a,b,c): 

    return rz(c) @ ry(b) @ rz(a)

