import numpy as np

EPS = 1e-12
AXIS = (1, 2, 3)


def iou(y_true, y_pred):
    intersection = np.sum(y_true * y_pred, axis=AXIS)
    sum_ = np.sum(y_true + y_pred, axis=AXIS)
    jac = (intersection + EPS) / (sum_ - intersection + EPS)
    
    return np.mean(jac)

    