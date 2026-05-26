import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    return np.array([np.percentile(np.array(x), percentile) for percentile in q])
        