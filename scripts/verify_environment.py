"""Verify the EN3160 Python environment."""
import cv2
import matplotlib
import numpy
import PIL
import scipy
import skimage

packages = {"NumPy": numpy.__version__, "Matplotlib": matplotlib.__version__, "OpenCV": cv2.__version__, "SciPy": scipy.__version__, "scikit-image": skimage.__version__, "Pillow": PIL.__version__}
print("EN3160 environment verification passed:")
for name, version in packages.items():
    print(f"  {name}: {version}")
