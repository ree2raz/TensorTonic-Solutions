import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    sample_size = len(x) - 1
    x_mean = np.mean(x)
    deviation_sum = 0
    for num in x:
        deviation_sum += (num - x_mean)**2
    variance = deviation_sum / sample_size
    return (variance, np.sqrt(variance))