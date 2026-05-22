import time

from imagecorruptions import corrupt, get_corruption_names
from PIL import Image
import numpy as np

PLOT_RESULT = False

image = np.asarray(Image.open('test_image.jpg'))

for corruption in get_corruption_names('all'):
    tic = time.time()
    for severity in range(5):
        corrupted = corrupt(image, corruption_name=corruption, severity=severity+1)
        if PLOT_RESULT:
            import matplotlib.pyplot as plt
            plt.imshow(corrupted)
            plt.show()
    print(corruption, time.time() - tic)