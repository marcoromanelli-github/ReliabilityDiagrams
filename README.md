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

### Intallation
1. Install required packages by running
```console
foo@bar:~$ python -m pip install -U -r <path>/requirements.txt
```
2. Download the deplyed package as the artifact created by the last action in [Actions](https://github.com/marcoromanelli-github/MLToolsShed/actions) and unzip it.
3. Run the command below
```console
foo@bar:~$ python -m pip install -U <path>/built_pkg/<filename>.whl
    
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
   
