import glob
import numpy as np
import matplotlib.pyplot as plt

for fname in glob.glob('data/city*.csv'):
    year = fname[23:27]
    print('Loading data for year ', year)
    data = np.loadtxt(fname, delimiter=',')

    fig = plt.figure(figsize=(10.0, 3.0))

    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel('average')
    axes1.plot(np.mean(data, axis=0), 'rs')

    axes2.set_ylabel('max')
    axes2.plot(np.max(data, axis=0), 'b--')

    axes3.set_ylabel('min')
    axes3.plot(np.min(data, axis=0), 'go')

    fig.tight_layout()

plt.show()