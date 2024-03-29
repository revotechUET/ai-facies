import numpy as np


def compute_number_of_changing_direction_time(arr):
    diff = np.diff(arr)
    n_samples = diff.shape[0]
    upward = True
    count = 0
    i = 0
    while i < n_samples and diff[i] == 0:
        i += 1
    if i < n_samples and diff[i] < 0:
        upward = False
    for j in range(i + 1, n_samples):
        if (upward and diff[j] < 0) or ((not upward) and diff[j] > 0):
            count += 1
            upward = not upward
    return count


def compute_number_of_time_crossing_slope_line(arr):
    n_samples = arr.shape[0]
    avg_first = np.average(arr[:2])
    avg_last = np.average(arr[-2:])
    base_line = np.linspace(avg_first, avg_last, n_samples, endpoint=True)
    difference = (arr - base_line)
    # count = ((difference[:-1] * difference[1:]) < 0).sum()
    upward = True
    count = 0
    i = 0
    while i < n_samples and difference[i] == 0:
        i += 1
    if i < n_samples and difference[i] < 0:
        upward = False
    for j in range(i + 1, n_samples):
        if (upward and difference[j] < 0) or ((not upward) and difference[j] > 0):
            count += 1
            upward = not upward
    return count


def compute_slope(arr):
    return (np.average(arr[:2]) - np.average(arr[-2:])) / arr.shape[0]


def compute_variance_base_on_slope_line(arr):
    n_samples = arr.shape[0]
    avg_first = np.average(arr[:2])
    avg_last = np.average(arr[-2:])
    base_line = np.linspace(avg_first, avg_last, n_samples, endpoint=True)
    return np.mean((arr - base_line) ** 2)
