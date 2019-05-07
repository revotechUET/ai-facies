from .core.units import UnitBreaker
from .core.smoothing_functions import window_smooth
from .core import utils
import numpy as np


def select_boundary(gr, tvd):
    gr_smooth = window_smooth(gr, window_len=14, window='hamming')
    changing_direction_point_flag = UnitBreaker().detect_changing_direction_point(x=gr_smooth, epsilon=0.05,
                                                                                  multiplier=7)
    refined_peak = UnitBreaker().refine_peak(x=gr, flags=changing_direction_point_flag)
    refined_peak_2 = UnitBreaker().refine_peak(x=gr, flags=refined_peak)
    boundary_flags = UnitBreaker().select_boundary(gr=gr, flags=refined_peak_2, tvd=tvd,
                                                   min_thickness=1, gr_shoulder_threshold=10)
    return boundary_flags


def detect_lithofacies(gr, v_mud, tvd):
    gr_smooth = window_smooth(gr, window_len=14, window='hamming')
    changing_direction_point_flag = UnitBreaker().detect_changing_direction_point(x=gr_smooth, epsilon=0.05,
                                                                                  multiplier=7)
    refined_peak = UnitBreaker().refine_peak(x=gr, flags=changing_direction_point_flag)
    refined_peak_2 = UnitBreaker().refine_peak(x=gr, flags=refined_peak)
    boundary_flags = UnitBreaker().select_boundary(gr=gr, flags=refined_peak_2, tvd=tvd,
                                                   min_thickness=1, gr_shoulder_threshold=10)
    lithofacies = UnitBreaker().detect_lithofacies(boundary_flags=boundary_flags, mud_volume=v_mud, method='major')
    return lithofacies


def detect_sharp_boundary(gr, tvd):
    print(len(gr))
    print(len(tvd))
    gr_smooth = window_smooth(gr, window_len=14, window='hamming')
    changing_direction_point_flag = UnitBreaker().detect_changing_direction_point(x=gr_smooth, epsilon=0.05,
                                                                                  multiplier=7)
    refined_peak = UnitBreaker().refine_peak(x=gr, flags=changing_direction_point_flag)
    refined_peak_2 = UnitBreaker().refine_peak(x=gr, flags=refined_peak)
    boundary_flags = UnitBreaker().select_boundary(gr=gr, flags=refined_peak_2, tvd=tvd,
                                                   min_thickness=1, gr_shoulder_threshold=10)
    sharp_boundary = UnitBreaker().detect_sharp_boundary(gr=gr, boundary_flags=boundary_flags, min_diff=40)
    return sharp_boundary


def detect_label_shape_code(gr, v_mud, tvd):
    gr_smooth = window_smooth(gr, window_len=14, window='hamming')
    changing_direction_point_flag = UnitBreaker().detect_changing_direction_point(x=gr_smooth, epsilon=0.05,
                                                                                  multiplier=7)
    refined_peak = UnitBreaker().refine_peak(x=gr, flags=changing_direction_point_flag)
    refined_peak_2 = UnitBreaker().refine_peak(x=gr, flags=refined_peak)
    boundary_flags = UnitBreaker().select_boundary(gr=gr, flags=refined_peak_2, tvd=tvd,
                                                   min_thickness=1, gr_shoulder_threshold=10)
    lithofacies = UnitBreaker().detect_lithofacies(boundary_flags=boundary_flags, mud_volume=v_mud, method='major')

    def compute_variance_base_on_slope_line(arr):
        n_samples = arr.shape[0]
        avg_first = np.average(arr[:2])
        avg_last = np.average(arr[-2:])
        base_line = np.linspace(avg_first, avg_last, n_samples, endpoint=True)
        return np.mean((arr - base_line) ** 2)

    n_samples = gr.shape[0]
    variance_2 = np.zeros(n_samples)

    idx_set = []
    for i in range(0, n_samples):
        idx_set.append(i)
        if boundary_flags[i] == 1 or i == n_samples - 1:
            gr_set = gr[idx_set].copy()
            variance_2[idx_set] = compute_variance_base_on_slope_line(gr_set)
            idx_set = []

    labels = UnitBreaker().label_shape_code(gr=gr, boundary_flags=boundary_flags, tvd=tvd, lithofacies=lithofacies,
                                            variance=variance_2, gr_threshold=8, gr_avg_threshold=6,
                                            tvd_threshold=2,
                                            roc_threshold=0.2, variance_threshold=40, change_sign_threshold=2)
    return labels


def detect_stacking_pattern(gr, tvd):
    # Detect unit boundary
    gr_smooth = window_smooth(gr, window_len=14, window='hamming')
    changing_direction_point_flag = UnitBreaker().detect_changing_direction_point(x=gr_smooth, epsilon=0.05,
                                                                                  multiplier=7)
    refined_peak = UnitBreaker().refine_peak(x=gr, flags=changing_direction_point_flag)
    refined_peak_2 = UnitBreaker().refine_peak(x=gr, flags=refined_peak)
    boundary_flags = UnitBreaker().select_boundary(gr=gr, flags=refined_peak_2, tvd=tvd,
                                                   min_thickness=1, gr_shoulder_threshold=10)
    # Detect stack boundary
    gr_smooth = window_smooth(gr, window_len=50, window='hamming')

    stacking_patterns = UnitBreaker().stack_unit(gr_smooth=gr_smooth, units_boundary=boundary_flags,
                                                 min_samples=15, gr_smooth_threshold=5)

    return stacking_patterns


def detect_unit_length(boundary_flags, tvd):
    unit_thick = []
    bound = 0
    for i in range(len(boundary_flags)):
        if boundary_flags[i] == 1:
            thick = tvd[i] - tvd[bound]
            for j in range(bound + 1 if bound > 0 else 0, i + 1):
                unit_thick.append(thick)
                bound = i
    return unit_thick


def detect_unit_index(boundary_flags):
    return UnitBreaker.assign_unit_index(boundary_flags)


def find_similar_unit(gr, tvd, boundary_flags, lithofacies, gr_shape_code, thickness, unit_index, max_depth,
                      min_depth):
    idx_set = []
    n_samples = gr.shape[0]
    zcr = np.zeros(n_samples)
    slope = np.zeros(n_samples)
    mean_unit = np.zeros(n_samples)
    variance_1 = np.zeros(n_samples)
    variance_2 = np.zeros(n_samples)

    for i in range(0, n_samples):
        idx_set.append(i)
        if boundary_flags[i] == 1 or i == n_samples - 1:
            gr_set = gr[idx_set].copy()
            zcr[idx_set] = utils.compute_rate_of_change(gr_set)
            slope[idx_set] = utils.compute_slope(gr[idx_set])
            mean_unit[idx_set] = np.average(gr_set)
            variance_1[idx_set] = np.var(gr_set)
            variance_2[idx_set] = utils.compute_variance_base_on_slope_line(gr_set)
            idx_set = []

    return UnitBreaker().find_similar_units(gr, tvd, boundary_flags, lithofacies, gr_shape_code, thickness, zcr, slope,
                                            mean_unit, variance_1, variance_2, max_depth, min_depth, unit_index)
