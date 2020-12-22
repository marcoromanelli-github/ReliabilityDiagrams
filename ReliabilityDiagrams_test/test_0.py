import pandas as pn
from ReliabilityDiagrams import plot_reliability_diagram


def test_0():
    #   load the numpy array with the true classes
    #   m = number of samples
    #   the numbers correspond to the class IDs
    y_true = pn.read_pickle("/tmp/RelDiag/toy_data/y_true.pkl")
    print(y_true)

    #   load the numpy array with the probability matrices m X n
    #   m = number of samples
    #   n = number of classes
    y_pred = pn.read_pickle("/tmp/RelDiag/toy_data/y_pred.pkl")
    print(y_pred[0])

    plot_reliability_diagram.plot_reliabiblity_diagram(y_true=y_true,
                                                       y_pred=y_pred,
                                                       n_bins=10,
                                                       rel_diag_folder="/tmp/RelDiag")

    if __name__ == '__main__':
        test_0()
