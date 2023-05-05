import numpy as np
import matplotlib.pyplot as plt
N, M, R = 1000, 100, 1.0
plt.hist([print(i) or np.mean(4 * np.sum(np.sqrt(R**2 - np.random.uniform(0, R, (N, M))**2) > np.random.uniform(0, R, (N, M)), axis=0) / N) for i in range(M)], bins=np.linspace(3.12, 3.17, M))
plt.show()
 