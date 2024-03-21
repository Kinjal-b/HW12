import numpy as np

def softmax(x):
    """Computing softmax values for each sets of scores in x"""
    e_x = np.exp(x - np.max(x))  # Subtract max for numerical stability
    return e_x / e_x.sum(axis=0)  # Divide by sum along the axis

# Example usage
scores = np.array([3.0, 1.0, 0.2])
softmax_scores = softmax(scores)
softmax_scores