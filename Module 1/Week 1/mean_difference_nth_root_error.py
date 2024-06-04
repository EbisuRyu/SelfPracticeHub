def mean_differential_nre_single_sample(y_true, y_pred, power_root, exponent):
    """
    Compute the Mean Differential Non-Relative Error (MD-NRE) for a single sample.

    Parameters:
        y_true (float): The true value.
        y_pred (float): The predicted value.
        power_root (int): The root to which the difference of values will be raised.
        exponent (int): The exponent to which the differential will be raised.

    Returns:
        float: The mean differential non-relative error.
    """
    differential = abs(y_true ** (1 / power_root) - y_pred ** (1 / power_root))
    return differential ** exponent

# Test Cases
print(mean_differential_nre_single_sample(y_true=100, y_pred=99.5, power_root=2, exponent=1))
print(mean_differential_nre_single_sample(y_true=50, y_pred=49.5, power_root=2, exponent=1))
print(mean_differential_nre_single_sample(y_true=20, y_pred=19.5, power_root=2, exponent=1))
print(mean_differential_nre_single_sample(y_true=0.6, y_pred=0.1, power_root=2, exponent=1))