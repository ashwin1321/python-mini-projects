import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model

diabetes = datasets.load_diabetes()
# dict_keys(['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename', 'data_module']
print(diabetes.keys())