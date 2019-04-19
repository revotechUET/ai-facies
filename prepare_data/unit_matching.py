import numpy as np
import pandas as pd
import seaborn as sns

sns.set()


def compute_rate_of_change(arr):
    n_samples = arr.shape[0]
    avg_first = np.average(arr[:2])
    avg_last = np.average(arr[-2:])
    base_line = np.linspace(avg_first, avg_last, n_samples, endpoint=True)
    difference = (arr - base_line)
    upward = True
    count = 0
    i = 0
    while difference[i] == 0 and i < n_samples:
        i += 1
    if difference[i] < 0 and i < n_samples:
        upward = False
    for j in range(i + 1, n_samples):
        if (upward and difference[j] < 0) or ((not upward) and difference[j] > 0):
            count += 1
            upward = not upward
    return count / n_samples


def compute_slope(arr):
    return (np.average(arr[:2]) - np.average(arr[-2:])) / arr.shape[0]


def compute_variance_base_on_slope_line(arr):
    n_samples = arr.shape[0]
    avg_first = np.average(arr[:2])
    avg_last = np.average(arr[-2:])
    base_line = np.linspace(avg_first, avg_last, n_samples, endpoint=True)
    return np.mean((arr - base_line) ** 2)


def unit_matching():
    # Importing the dataset
    dataset = pd.read_csv('csv/initial_data.csv')

    gr = dataset.GR.values
    tvd = dataset.TVD.values
    boundary_flag = dataset.Boundary_flag.values
    gr_shape_code = dataset.GR_shape_code.values
    lithofacies = dataset.Lithofacies_major.values

    # Unit index
    n_samples = gr.shape[0]
    unit_index = np.zeros(n_samples).astype(np.int32)
    sequence_number = 0
    idx_set = []
    for i in range(n_samples):
        idx_set.append(i)
        if boundary_flag[i] != 0 or i == n_samples - 1:
            unit_index[idx_set] = sequence_number
            sequence_number += 1
            idx_set = []

    # Statistical measures
    idx_set = []
    n_samples = gr.shape[0]
    zcr = np.zeros(n_samples)
    thickness = np.zeros(n_samples)
    slope = np.zeros(n_samples)
    mean_unit = np.zeros(n_samples)
    variance_1 = np.zeros(n_samples)
    variance_2 = np.zeros(n_samples)

    for i in range(0, n_samples):
        idx_set.append(i)
        if boundary_flag[i] == 1 or i == n_samples - 1:
            gr_set = gr[idx_set].copy()
            zcr[idx_set] = compute_rate_of_change(gr_set)
            thickness[idx_set] = tvd[idx_set[-1]] - tvd[idx_set[0]]
            slope[idx_set] = compute_slope(gr[idx_set])
            mean_unit[idx_set] = np.average(gr_set)
            variance_1[idx_set] = np.var(gr_set)
            variance_2[idx_set] = compute_variance_base_on_slope_line(gr_set)
            idx_set = []

    # Threshold
    zcr_threshold = 0.5
    slope_threshold = 0.5
    mean_threshold = 10
    variance_1_threshold = 15
    variance_2_threshold = 15
    rms_threshold = 6

    weights = {'zcr': 1, 'slope': 5, 'mean': 1, 'variance1': 1, 'variance2': 2, 'rms': 3}
    score_threshold = 10

    n_samples = gr.shape[0]
    idx_set = []
    number_of_similar_pattern50 = np.zeros(n_samples)
    number_of_similar_pattern100 = np.zeros(n_samples)
    similar_unit_list50 = []
    similar_unit_list100 = []

    for i in range(n_samples):
        idx_set.append(i)
        if boundary_flag[i] != 0 or i == n_samples - 1:
            sub_idx_set = []
            similar_unit_index = []
            for j in range(i + 1, n_samples):
                sub_idx_set.append(j)
                if boundary_flag[j] != 0 or j == n_samples - 1:
                    current_unit_id = idx_set[0]
                    comparison_unit_id = sub_idx_set[0]
                    if abs(tvd[comparison_unit_id] - tvd[current_unit_id]) <= 50:
                        if lithofacies[current_unit_id] == lithofacies[comparison_unit_id] and gr_shape_code[
                            current_unit_id] == gr_shape_code[comparison_unit_id]:
                            if thickness[current_unit_id] * 0.5 < thickness[comparison_unit_id] < thickness[
                                current_unit_id] * 1.5:
                                score = 0
                                n_current_unit_samples = len(idx_set)
                                n_comparision_unit_samples = len(sub_idx_set)
                                current_unit_resamples = np.array(
                                    [gr[idx_set[0]],
                                     gr[idx_set[int(n_current_unit_samples * 0.25)]],
                                     gr[idx_set[int(n_current_unit_samples * 0.5)]],
                                     gr[idx_set[int(n_current_unit_samples * 0.75)]],
                                     gr[idx_set[-1]]])

                                comparison_unit_resamples = np.array(
                                    [gr[sub_idx_set[0]],
                                     gr[sub_idx_set[int(n_comparision_unit_samples * 0.25)]],
                                     gr[sub_idx_set[int(n_comparision_unit_samples * 0.5)]],
                                     gr[sub_idx_set[int(n_comparision_unit_samples * 0.75)]],
                                     gr[sub_idx_set[-1]]])

                                rms = np.sqrt(np.mean((current_unit_resamples - comparison_unit_resamples) ** 2))
                                if rms < rms_threshold:
                                    score += weights['rms']
                                if abs(zcr[current_unit_id] - zcr[comparison_unit_id]) < zcr_threshold:
                                    score += weights['zcr']
                                if abs(slope[current_unit_id] - slope[comparison_unit_id]) < slope_threshold:
                                    score += weights['slope']
                                if abs(mean_unit[current_unit_id] - mean_unit[comparison_unit_id]) < mean_threshold:
                                    score += weights['mean']
                                if abs(variance_1[current_unit_id] - variance_1[
                                    comparison_unit_id]) < variance_1_threshold:
                                    score += weights['variance1']
                                if abs(variance_2[current_unit_id] - variance_2[
                                    comparison_unit_id]) < variance_2_threshold:
                                    score += weights['variance2']
                                if score > score_threshold:
                                    number_of_similar_pattern50[idx_set] += 1
                                    number_of_similar_pattern50[sub_idx_set] += 1
                                    similar_unit_index.append(unit_index[comparison_unit_id])
                    else:
                        break
                    sub_idx_set = []
            similar_unit_list50.append(similar_unit_index)
            idx_set = []

    for i in range(len(similar_unit_list50)):
        for j in range(len(similar_unit_list50[i])):
            if similar_unit_list50[i][j] > i:
                similar_unit_list50[similar_unit_list50[i][j]].append(i)

    for i in range(n_samples):
        idx_set.append(i)
        if boundary_flag[i] != 0 or i == n_samples - 1:
            sub_idx_set = []
            similar_unit_index = []
            for j in range(i + 1, n_samples):
                sub_idx_set.append(j)
                if boundary_flag[j] != 0 or j == n_samples - 1:
                    current_unit_id = idx_set[0]
                    comparison_unit_id = sub_idx_set[0]
                    if 50 < abs(tvd[comparison_unit_id] - tvd[current_unit_id]) <= 100:
                        if lithofacies[current_unit_id] == lithofacies[comparison_unit_id] and gr_shape_code[
                            current_unit_id] == gr_shape_code[comparison_unit_id]:
                            if thickness[current_unit_id] * 0.5 < thickness[comparison_unit_id] < thickness[
                                current_unit_id] * 1.5:
                                score = 0
                                n_current_unit_samples = len(idx_set)
                                n_comparision_unit_samples = len(sub_idx_set)
                                current_unit_resamples = np.array(
                                    [gr[idx_set[0]],
                                     gr[idx_set[int(n_current_unit_samples * 0.25)]],
                                     gr[idx_set[int(n_current_unit_samples * 0.5)]],
                                     gr[idx_set[int(n_current_unit_samples * 0.75)]],
                                     gr[idx_set[-1]]])

                                comparison_unit_resamples = np.array(
                                    [gr[sub_idx_set[0]],
                                     gr[sub_idx_set[int(n_comparision_unit_samples * 0.25)]],
                                     gr[sub_idx_set[int(n_comparision_unit_samples * 0.5)]],
                                     gr[sub_idx_set[int(n_comparision_unit_samples * 0.75)]],
                                     gr[sub_idx_set[-1]]])

                                rms = np.sqrt(np.mean((current_unit_resamples - comparison_unit_resamples) ** 2))
                                if rms < rms_threshold:
                                    score += weights['rms']
                                if abs(zcr[current_unit_id] - zcr[comparison_unit_id]) < zcr_threshold:
                                    score += weights['zcr']
                                if abs(slope[current_unit_id] - slope[comparison_unit_id]) < slope_threshold:
                                    score += weights['slope']
                                if abs(mean_unit[current_unit_id] - mean_unit[comparison_unit_id]) < mean_threshold:
                                    score += weights['mean']
                                if abs(variance_1[current_unit_id] - variance_1[
                                    comparison_unit_id]) < variance_1_threshold:
                                    score += weights['variance1']
                                if abs(variance_2[current_unit_id] - variance_2[
                                    comparison_unit_id]) < variance_2_threshold:
                                    score += weights['variance2']
                                if score > score_threshold:
                                    number_of_similar_pattern100[idx_set] += 1
                                    number_of_similar_pattern100[sub_idx_set] += 1
                                    similar_unit_index.append(unit_index[comparison_unit_id])
                    elif abs(tvd[comparison_unit_id] - tvd[current_unit_id]) > 100:
                        break
                    sub_idx_set = []
            similar_unit_list100.append(similar_unit_index)
            idx_set = []

    for i in range(len(similar_unit_list100)):
        for j in range(len(similar_unit_list100[i])):
            if similar_unit_list100[i][j] > i:
                similar_unit_list100[similar_unit_list100[i][j]].append(i)

    dataset['Unit_index'] = unit_index
    dataset['Number_of_similar_units_50'] = number_of_similar_pattern50
    dataset['Index_of_similar_units_50'] = ''
    for i in range(len(similar_unit_list50)):
        dataset.loc[dataset.Unit_index == i, 'Index_of_similar_units_50'] = str(similar_unit_list50[i])

    dataset['Number_of_similar_units_100'] = number_of_similar_pattern100
    dataset['Index_of_similar_units_100'] = ''
    for i in range(len(similar_unit_list100)):
        dataset.loc[dataset.Unit_index == i, 'Index_of_similar_units_100'] = str(similar_unit_list100[i])

    dataset.Boundary_flag = dataset.Boundary_flag.astype(np.int8)
    dataset.Number_of_similar_units_50 = dataset.Number_of_similar_units_50.astype(np.int64)
    dataset.Number_of_similar_units_100 = dataset.Number_of_similar_units_100.astype(np.int64)
    dataset.Sharp_boundary = dataset.Sharp_boundary.astype(np.int8)
    dataset.dtypes
    dataset = dataset[['Depth', 'GR', 'MUD_VOLUME', 'TVD', 'Boundary_flag', 'Unit_index', 'GR_shape_code',
                       'Lithofacies_major', 'Sharp_boundary', 'Stacking_pattern',
                       'Biostratigraphy', 'Reliability', 'Special_lithology', 'Core_depofacies', 'Lateral_proximity',
                       'Number_of_similar_units_50', 'Index_of_similar_units_50', 'Number_of_similar_units_100',
                       'Index_of_similar_units_100']]
    dataset.to_csv('csv/data.csv', index=False)
