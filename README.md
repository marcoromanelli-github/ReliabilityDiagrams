[![build_package](https://github.com/marcoromanelli-github/ReliabilityDiagrams/workflows/build_package/badge.svg)](https://github.com/marcoromanelli-github/ReliabilityDiagrams/actions)
[![Documentation](https://img.shields.io/badge/Dcoumentation-yes-blue)](https://img.shields.io/badge/Dcoumentation-yes-blue)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://img.shields.io/badge/License-MIT-yellow.svg)

# ReliabilityDiagrams
Create reliability diagrams to quantify ML calibration.

<div align="center">
    <img src=".icon/REID_icon.jpeg" width="300" height=300/>
</div>

Package that can be used to create reliability diagrams according to the 
definition in the paper 
[On Calibration of Modern Neural Networks](https://arxiv.org/pdf/1706.04599.pdf).
It also computes the Expected Calibration Error (ECE).

To install the package and use it in your python project follow these steps:
1. download the package from this page in a folder
2. navigate to the folder and install with 
```console
foo@bar:~$ pip install reid-reliability-diagrams/
```
3. import the package in your project with 
```python
import REliability_Diagram_pkg as rdp
```
    
The following code:
```python  
import pandas as pn
import REliability_Diagram_pkg as rdp
y_true = pn.read_pickle("<path_to_toy_data>/y_true.pkl")
y_pred = pn.read_pickle("<path_to_toy_data>/y_pred.pkl")

rdp.plot_reliabiblity_diagram(y_true=y_true, 
			      y_pred=y_pred, 
			      n_bins=10, 
			      rel_diag_folder=<path_to_rel_diag_folder>)
```
produces the plot
![rel_diag_img](/res_folder/REID.png)
   
