from inspect import cleandoc


class MaskCropperNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        """
            Return a dictionary which contains config for all input fields.
            Some types (string): "MODEL", "VAE", "CLIP", "CONDITIONING", "LATENT", "IMAGE", "INT", "STRING", "FLOAT".
            Input types "INT", "STRING" or "FLOAT" are special values for fields on the node.
            The type can be a list for selection.

            Returns: `dict`:
                - Key input_fields_group (`string`): Can be either required, hidden or optional. A node class must have property `required`
                - Value input_fields (`dict`): Contains input fields config:
                    * Key field_name (`string`): Name of a entry-point method's argument
                    * Value field_config (`tuple`):
                        + First value is a string indicate the type of field or a list for selection.
                        + Secound value is a config for type "INT", "STRING" or "FLOAT".
        """
        return {
            "required": {
                "image": ("IMAGE", {"tooltip": "This is an image"}),
                "mask": ("MASK", {"tooltip": "mask that used to crop image"}),
                "border_width": ("INT", {"tooltip": "border width"}),
                "border_height": ("INT", {"tooltip": "border height"})
            },
        }

    RETURN_TYPES = ("IMAGE", 'MASK')
    # RETURN_NAMES = ("image_output_name",)
    # DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "do_crop_by_mask"

    # OUTPUT_NODE = False
    # OUTPUT_TOOLTIPS = ("",) # Tooltips for the output node

    CATEGORY = "image"

    def do_crop_by_mask(self, image, mask, border_width=0, border_height=0):
        # image [B,H,W,3] -> [B,3,H,W]
        # mask [B,H,W]
        print('mask shape', mask.shape)
        print('image shape', image.shape)
        mask = mask[0]
        # print(mask)
        left, right, top, bottom = mask.shape[1], 0, mask.shape[0], 0
        for i in range(mask.shape[0]):
            for j in range(mask.shape[1]):
                pex = mask[i, j].item()
                if pex != 0:
                    left = min(left, j)
                    right = max(right, j)
                    top = min(top, i)
                    bottom = max(bottom, i)

        print(left, right, top, bottom)

        top, bottom = max(0, top-border_height), min(mask.shape[0], bottom+border_height)
        left, right = max(0, left-border_width), min(mask.shape[1], right+border_width)

        cropped_mask = mask[top:bottom, left:right]
        cropped_mask = cropped_mask.float()

        cropped_image = image[:, top:bottom, left:right, :]
        cropped_image = cropped_image.float()
        return cropped_image, cropped_mask

    """
        The node will always be re executed if any of the inputs change but
        this method can be used to force the node to execute again even when the inputs don't change.
        You can make this node return a number or a string. This value will be compared to the one returned the last time the node was
        executed, if it is different the node will be executed again.
        This method is used in the core repo for the LoadImage node where they return the image hash as a string, if the image hash
        changes between executions the LoadImage node is executed again.
    """
    # @classmethod
    # def IS_CHANGED(s, image, string_field, int_field, float_field, print_to_screen):
    #    return ""


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "MaskCropperNode": MaskCropperNode
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "MaskCropperNode": "Crop Image By Mask"
}
