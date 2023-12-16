import numpy as np
import example


arr = np.array([1.0, 2.0, 3.0, 4.0])
example.modify_array(arr)

print(arr)  # Expected output: [2.0, 4.0, 6.0, 8.0]