# ComfyUI Image Resizer Node

## Overview

This repository contains a custom node for ComfyUI that resizes input images to a fixed size of 128x128 pixels. The node is designed to be efficient, easy to use, and seamlessly integrate with existing ComfyUI workflows.

## Features

- Resizes any input image to 128x128 pixels
- Utilizes PyTorch for efficient tensor operations
- Implements the high-quality Lanczos resampling algorithm via Pillow
- Fully compatible with ComfyUI's node system

## Requirements

- ComfyUI
- PyTorch
- NumPy
- Pillow (PIL)

## Installation

1. Ensure you have ComfyUI installed and set up.
2. Clone this repository or download the `image_resizer_128.py` file.
3. Place the `image_resizer_128.py` file in the `custom_nodes` directory of your ComfyUI installation.
4. Restart ComfyUI to load the new node.

## Usage

After installation, the "Image Resizer (128x128)" node will be available in the ComfyUI interface under the "image/transform" category.

1. In your ComfyUI workflow, find the "Image Resizer (128x128)" node in the "image/transform" category.
2. Connect an image output from another node to the input of the Image Resizer node.
3. The output of the Image Resizer node will be the input image resized to 128x128 pixels.

## Technical Details

The `ImageResizer` class implements the following key methods:

- `INPUT_TYPES`: Defines the input type as an IMAGE.
- `resize_image`: The main method that performs the resizing operation.
- `_tensor_to_numpy`: Converts PyTorch tensors to NumPy arrays.
- `_numpy_to_tensor`: Converts NumPy arrays back to PyTorch tensors.

The resizing process uses the Lanczos algorithm, which provides high-quality results for both upscaling and downscaling operations.

## Contributing

Contributions to improve the Image Resizer node are welcome. Please feel free to submit issues or pull requests.

## License

[MIT License](LICENSE)

## Acknowledgments

This node was created for use with ComfyUI, an open-source project. Special thanks to the ComfyUI community for their continuous support and innovation in the field of AI-powered image generation and manipulation.
