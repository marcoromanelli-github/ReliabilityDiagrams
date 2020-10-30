import numpy as np

DEBUG=False
#   compute the confidence bin by bin
#   soft_probabilities_matrix: #_of_samples x #_of_classes
def compute_bin_conf(soft_probabilities_matrix, min_bins_borders, bin_dic_conf):
    """
    :param soft_probabilities_matrix: matrix output by the model at prediction time
    :param min_bins_borders: separtor coordinates for the bins
    :param bin_dic_conf: dictionary of the confidence bin by bin
    :return: list of the confidence bin by bin and list of elements for each bin
    """
    #   loop over the soft-probabilities for each sample
    for row_idx in range(soft_probabilities_matrix.shape[0]):
        #   get the highest element as the confidence
        confidence = np.max(soft_probabilities_matrix[row_idx, :])

        #   min_bins_borders in ascending order
        #   check which bin the confidence belongs to
        #   assign each confidence to its bin
        for min_border_idx in range(len(min_bins_borders)):
            if min_border_idx + 1 < len(min_bins_borders):
                if min_bins_borders[min_border_idx] < confidence <= min_bins_borders[min_border_idx + 1]:
                    bin_dic_conf[min_border_idx].append(confidence)
                    break
            else:
                bin_dic_conf[len(min_bins_borders) - 1].append(confidence)

    #   list of list: each element is a bin and each bin can have elements inside
    list_conf_per_bin = []
    elements_in_bin = []

    for key in range(len(bin_dic_conf)):
        tmp = bin_dic_conf[key]
        elements_in_bin.append(len(tmp))
        if len(tmp) == 0:
            list_conf_per_bin.append(0)
        else:
            list_conf_per_bin.append(float(np.mean(np.array(tmp).reshape(len(tmp), 1), axis=0)[0]))

    return [list_conf_per_bin, elements_in_bin]


def compute_bin_acc(y_true, y_prob, min_bins_borders, bin_dic_acc):
    for row_idx in range(y_prob.shape[0]):
        pred_class = np.argmax(y_prob[row_idx, :])
        confidence = np.max(y_prob[row_idx, :])
        real_class = y_true[row_idx]

        for min_border_idx in range(len(min_bins_borders)):
            if min_border_idx + 1 < len(min_bins_borders):
                if min_bins_borders[min_border_idx] < confidence <= min_bins_borders[min_border_idx + 1]:
                    if pred_class == real_class:
                        #   element in the dictionary always corresponding to the bin since it is its key
                        bin_dic_acc[min_border_idx].append(1)
                    else:
                        bin_dic_acc[min_border_idx].append(0)
                    break
            else:
                if pred_class == real_class:
                    bin_dic_acc[len(min_bins_borders) - 1].append(1)
                else:
                    bin_dic_acc[len(min_bins_borders) - 1].append(0)

    list_acc_per_bin = []

    for key in range(len(bin_dic_acc)):
        tmp = bin_dic_acc[key]
        if len(tmp) == 0:
            list_acc_per_bin.append(0)
        else:
            list_acc_per_bin.append(float(np.mean(np.array(tmp).reshape(len(tmp), 1), axis=0)[0]))

    return list_acc_per_bin


def compute_ECE(y_data, conf_per_bin_list, elements_in_bin_list, y_true):
    ECE_list = []

    current_y_data = y_data
    # print current_y_data

    current_conf_per_bin_list = conf_per_bin_list
    # print current_conf_per_bin_list

    current_elements_in_bin_list = elements_in_bin_list
    # print current_elements_in_bin_list

    current_ECE = 0

    n = len(y_true)
    # print "n, ", n

    for bin_idx in range(len(current_elements_in_bin_list)):
        a = current_elements_in_bin_list[bin_idx] / float(n)
        b = abs(current_y_data[bin_idx] - current_conf_per_bin_list[bin_idx])
        c = a * b
        current_ECE += c

    ECE_list.append(current_ECE)

    ECE = np.mean(np.array(ECE_list).reshape((len(ECE_list), 1)), axis=0)

    return ECE
