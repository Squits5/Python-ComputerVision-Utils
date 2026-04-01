# Python-ComputerVision-Utils

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)

A comprehensive collection of essential utility functions for various computer vision tasks. This repository provides tools for image loading, preprocessing, augmentation, and basic feature extraction, leveraging popular libraries like OpenCV and Pillow.

## Features

-   **Image I/O:** Functions to load and save images in different formats and color modes.
-   **Image Resizing:** Efficient resizing with various interpolation methods.
-   **Image Rotation:** Rotate images by arbitrary angles.
-   **Filtering:** Apply Gaussian blur and other common image filters.
-   **Color Conversion:** Convert images between RGB and grayscale.
-   **Edge Detection:** Implement Canny edge detection for feature extraction.

## Project Structure

```
Python-ComputerVision-Utils/
├── src/
│   └── cv_utils.py
├── README.md
└── requirements.txt
```

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Squits5/Python-ComputerVision-Utils.git
    cd Python-ComputerVision-Utils
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

```python
from src.cv_utils import load_image, resize_image, save_image
import numpy as np
import os

# Create a dummy image for demonstration
dummy_path = "sample_image.png"
dummy_img_data = np.zeros((100, 100, 3), dtype=np.uint8)
dummy_img_data[20:80, 20:80] = [255, 0, 0] # Red square
save_image(dummy_img_data, dummy_path)

try:
    img = load_image(dummy_path)
    resized_img = resize_image(img, (50, 50))
    save_image(resized_img, "sample_image_resized.png")
finally:
    if os.path.exists(dummy_path):
        os.remove(dummy_path)
```

## Contributing

Contributions are highly encouraged! Please submit issues or pull requests for new features or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
