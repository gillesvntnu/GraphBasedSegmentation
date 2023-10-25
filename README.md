# Graph Based Segmentation

This repository contains code for using graph based architectures for
segmentation. The code is extracted as a modular entity and can be 
used directly in PyTorch. The code is based on the work "
[Towards Robust Cardiac Segmentation using Graph Convolutional Networks](
https://arxiv.org/pdf/2310.01210v2.pdf)".

For the full framework used in the publication, see https://github.com/gillesvntnu/GCN_multistructure


## Contents
[CNN_GCN.py](./CNN_GCN.py) contains the code for single structure segmentation architecture.

[GCN_multistructure.py](./GCN_multistructure.py) contains the code for multi structure segmentation architecture.

[GCN_multi_displacement.py](./GCN_multi_displacement.py) contains the code for multi structure segmentation with
displacement method architecture.




## Acknowledgements
This work extends the architecture provided by 
- S. Thomas, A. Gilbert, and G. Ben-Yosef: “Light-weight spatio-temporal
graphs for segmentation and ejection fraction prediction in cardiac
ultrasound” in Medical Image Computing and Computer Assisted
Intervention–MICCAI 2022: 25th International Conference, Singapore
https://github.com/guybenyosef/EchoGraphs.git



## Contact
For questions, please contact:
[gilles.van.de.vyver@ntnu.no](mailto:gilles.van.de.vyver@ntnu.no)



