"""Top-level package for node_crop_image_by_mask."""

__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
    "WEB_DIRECTORY",
]

__author__ = """comfy-node-crop-image-by-mask"""
__email__ = "liuihaodong666@gmail.com"
__version__ = "1.0.0"

from .src.node_crop_image_by_mask.nodes import NODE_CLASS_MAPPINGS
from .src.node_crop_image_by_mask.nodes import NODE_DISPLAY_NAME_MAPPINGS

WEB_DIRECTORY = "./web"
