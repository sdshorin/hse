

DEBUG_PRINT_DYNAMIC_ARR = False


def linear_distance(x, y):
    return abs(x - y)


def dynamic_time_warping(time_series_1, time_series_2):
    return DTW(time_series_1, time_series_2, linear_distance)


class DTW_Exception(BaseException):
    pass


def DTW(time_series_1, time_series_2, distance_func):
    if not len(time_series_1) or not len(time_series_2):
        raise DTW_Exception
    dynamic_warping_cost = []
    for _ in range(len(time_series_1)):  # create dynamic array
        dynamic_warping_cost.append([0] * len(time_series_2))
    dynamic_warping_cost[0][0] = distance_func(
        time_series_1[0], time_series_2[0])
    for i in range(1, len(time_series_1)):  # fill first column
        dynamic_warping_cost[i][0] = dynamic_warping_cost[i - 1][0] +\
            distance_func(time_series_1[i], time_series_2[0])
    for i in range(1, len(time_series_2)):  # fill first row
        dynamic_warping_cost[0][i] = dynamic_warping_cost[0][i - 1] +\
            distance_func(time_series_1[0], time_series_2[i])
    # main loop - fill all dynamic  array
    for x in range(1, len(time_series_1)):
        for y in range(1, len(time_series_2)):
            dynamic_warping_cost[x][y] =\
                distance_func(time_series_1[x], time_series_2[y]) +\
                min(
                dynamic_warping_cost[x][y - 1],
                dynamic_warping_cost[x - 1][y - 1],
                dynamic_warping_cost[x - 1][y],
            )
    restored_path = _dtw_restore_path(dynamic_warping_cost)
    result_cost = dynamic_warping_cost[-1][-1]
    if DEBUG_PRINT_DYNAMIC_ARR:
        for line in dynamic_warping_cost:
            print(line)
    return restored_path, result_cost


def _dtw_restore_path(dynamic_warping_cost):
    x = len(dynamic_warping_cost) - 1
    y = len(dynamic_warping_cost[0]) - 1
    restored_path = [[x, y]]
    # restore path from dynamic array - find min elements
    while x > 0 or y > 0:
        previous_x = x - 1
        previous_y = y - 1
        min_elem = None
        # check up left element first
        if y >= 1 and x >= 1 and (
                min_elem is None or
                dynamic_warping_cost[x - 1][y - 1] < min_elem):
            min_elem = dynamic_warping_cost[x - 1][y - 1]
            previous_x, previous_y = x - 1, y - 1
        # check up element
        if x >= 1 and (min_elem is None or
                       dynamic_warping_cost[x - 1][y] < min_elem):
            min_elem = dynamic_warping_cost[x - 1][y]
            previous_x, previous_y = x - 1, y
        # check left element
        if y >= 1 and (min_elem is None or
                       dynamic_warping_cost[x][y - 1] < min_elem):
            min_elem = dynamic_warping_cost[x][y - 1]
            previous_x, previous_y = x, y - 1
        x, y = previous_x, previous_y
        restored_path.append([x, y])
    restored_path.reverse()
    return restored_path
