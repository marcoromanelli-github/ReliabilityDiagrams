import pandas as pn
from ReliabilityDiagrams import compute_quantities, plot_reliability_diagram


def test_0():
    y_true = pn.read_pickle("/tmp/RED/toy_data/y_true.pkl")
    y_pred = pn.read_pickle("/tmp/RED/toy_data/y_pred.pkl")

    plot_reliability_diagram.plot_reliabiblity_diagram(y_true=y_true,
                                                       y_pred=y_pred,
                                                       n_bins=10,
                                                       rel_diag_folder="/tmp/RED")

    if __name__ == '__main__':
        test_0()
