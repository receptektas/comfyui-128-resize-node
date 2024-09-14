import torch
import numpy as np
from PIL import Image

class ImageResizer:
    @classmethod
    def INPUT_TYPES(cls):
        """
        Defines the input types for the node.
        
        Returns:
            dict: A dictionary specifying the required input types.
        """
        return {"required": {"image": ("IMAGE",)}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "resize_image"
    CATEGORY = "image/transform"

    def resize_image(self, image: torch.Tensor) -> torch.Tensor:
        """
        Resize the input image to 128x128 pixels.
        
        Args:
            image (torch.Tensor): Input image tensor of shape (C, H, W) or (B, C, H, W).
        
        Returns:
            torch.Tensor: Resized image tensor of shape (1, C, 128, 128).
        """
        image_np = self._tensor_to_numpy(image)
        image_pil = Image.fromarray((image_np * 255).astype(np.uint8))
        resized_image = image_pil.resize((128, 128), Image.LANCZOS)
        return self._numpy_to_tensor(np.array(resized_image))

    @staticmethod
    def _tensor_to_numpy(tensor: torch.Tensor) -> np.ndarray:
        """
        Convert a PyTorch tensor to a NumPy array.
        
        Args:
            tensor (torch.Tensor): Input tensor of shape (C, H, W) or (B, C, H, W).
        
        Returns:
            np.ndarray: NumPy array of shape (H, W, C).
        """
        return tensor.squeeze().permute(1, 2, 0).cpu().numpy()

    @staticmethod
    def _numpy_to_tensor(array: np.ndarray) -> torch.Tensor:
        """
        Convert a NumPy array to a PyTorch tensor.
        
        Args:
            array (np.ndarray): Input array of shape (H, W, C).
        
        Returns:
            torch.Tensor: PyTorch tensor of shape (1, C, H, W).
        """
        return torch.from_numpy(array.astype(np.float32) / 255.0).permute(2, 0, 1).unsqueeze(0)

# ComfyUI node mappings
NODE_CLASS_MAPPINGS = {"ImageResizer": ImageResizer}
NODE_DISPLAY_NAME_MAPPINGS = {"ImageResizer": "Image Resizer (128x128)"}