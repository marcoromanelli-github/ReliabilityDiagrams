import os
import numpy as np
from matplotlib import pyplot as plt
from ReliabilityDiagrams import compute_quantities as cq

DEBUG = False


def reliability_diagram(y_true, y_prob, n_bins):
    bin_dic_acc = {}
    bin_dic_conf = {}
    #   ordered array: looping over its leangth we name thekeys of all the dictionaries to maintain order correspondence
    #   even if the hash map for dictionaries gets shuffled
    min_bins_borders = np.arange(0., 1., 1. / float(n_bins))
    #   the keys of the dict correspond to the increasing order: beans from left to right have oncreasing index
    for min_border_idx in range(len(min_bins_borders)):
        bin_dic_acc[min_border_idx] = []
        bin_dic_conf[min_border_idx] = []

    if DEBUG:
        for i_ter in range(len(min_bins_borders)):
            if i_ter + 1 < len(min_bins_borders):
                print("sx_border ---> ", min_bins_borders[i_ter], " ### dx_border ---> ", min_bins_borders[i_ter + 1])
            else:
                print("sx_border ---> ", min_bins_borders[i_ter], " ### dx_border ---> ", 1.)

    list_acc_per_bin = cq.compute_bin_acc(y_true=y_true, y_prob=y_prob, bin_dic_acc=bin_dic_acc,
                                          min_bins_borders=min_bins_borders)

    list_conf_per_bin, elements_in_bin = cq.compute_bin_conf(soft_probabilities_matrix=y_prob,
                                                             min_bins_borders=min_bins_borders,
                                                             bin_dic_conf=bin_dic_conf)

    return [min_bins_borders, list_acc_per_bin, list_conf_per_bin, elements_in_bin]


def plot_reliabiblity_diagram(y_true, y_pred, n_bins, rel_diag_folder=None):
    x_data = None

    min_bins_borders, list_acc_per_bin, list_conf_per_bin, elements_in_bin = reliability_diagram(y_true=y_true,
                                                                                                 y_prob=y_pred,
                                                                                                 n_bins=n_bins)
    if x_data is None:
        x_data = min_bins_borders

    y_data = list_acc_per_bin
    conf_per_bin_list = list_conf_per_bin
    elements_in_bin_list = elements_in_bin

    if DEBUG:
        print(len(y_data))
        print(len(conf_per_bin_list))
        print(len(elements_in_bin_list))

    ECE = cq.compute_ECE(y_data=y_data, conf_per_bin_list=conf_per_bin_list, elements_in_bin_list=elements_in_bin_list,
                         y_true=y_true)

    fig, ax = plt.subplots()

    y_data_acc = y_data
    if DEBUG:
        a = np.array(y_data).reshape((len(y_data), len(y_data[0])))
        b = np.array(conf_per_bin_list).reshape((len(y_data), len(y_data[0])))
        print(y_data[0])
        print(a.shape)
        print(y_data_acc)

    y_data_conf = conf_per_bin_list

    y_data_gap_top = []
    y_data_gap_bottom = []

    for i_ter in range(len(y_data)):
        max_ = max(y_data_conf[i_ter], y_data_acc[i_ter])
        min_ = min(y_data_conf[i_ter], y_data_acc[i_ter])
        y_data_gap_top.append(max_ - min_)
        y_data_gap_bottom.append(min_)

    ax.bar(x_data, height=y_data_gap_top, bottom=y_data_gap_bottom, width=1. / float(n_bins), color=(1.0, 0.0, 0.0, 0.2),
           label='Gap', hatch="///", edgecolor='black', align='edge')
    ax.bar(x_data, height=y_data_acc, width=1. / float(n_bins), color=(0.0, 0.0, 1.0, 0.2), label='Output',
           edgecolor='black', align='edge')

    ax.set_xlabel("Confidence intervals")
    ax.set_ylabel("Outputs")

    ax.legend(["Gap", "Output"], loc='best')

    ax.text(0.02, 0.8, "ECE = " + str(round(ECE[0], 3)))

    plt.xlim(0, 1)

    plt.plot([0, 1], [0, 1], linestyle='--', color='r', linewidth=2)

    if rel_diag_folder is None:
        plt.show()
    else:
        if rel_diag_folder[-1] != "/":
            rel_diag_folder += "/"
        try:
            os.makedirs(rel_diag_folder)
        except FileExistsError:
            # directory already exists
            pass
        plt.savefig(rel_diag_folder + "RED.png", dpi=300)
