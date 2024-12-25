import numpy as np

def calculate(list):
    matrix = np.array(list).reshape(3, 3)
    flatMatrix = matrix.flatten()
    means = np.array([matrix.mean(axis=0), matrix.mean(axis=1), flatMatrix.mean()])
    stDevs = np.array([matrix.stdev(axis=0), matirx.stdev(axis=1), flatMatrix.stdev()])
    variances = np.array([matrix.var(axis=0), matrix.var(axis=1), flatMatrix.var()])
    mins = np.array([matrix.min(axis=0), matrix.min(axis=1), flatMatrix.min()])
    maxs = np.array([matrix.max(axis=0), matrix.max(axis=1), flatMatrix.max()])


    return calculations