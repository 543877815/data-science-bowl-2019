import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.rc('figure', figsize=(10, 6))
np.set_printoptions(precision=4, suppress=True)

def plot_distribution(data, name):
    plt.title('distribution of {0}'.format(name))
    plt.ylabel('number')
    plt.xlabel('count')
    plt.scatter(range(len(data)), data)