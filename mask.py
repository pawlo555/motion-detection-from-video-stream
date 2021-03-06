import numpy as np
from PIL import Image


class Mask:
    def __init__(self, img=None, size=(720, 540)):
        self.mask = None
        self.size = size
        if img:
            self.set_mask(img)

    def set_size(self, size):
        """
        Setting the size of the mask to the size of the frame
        :param size: size of the frame
        """
        if len(size) != 2:
            raise ValueError("size must be 2 dimensional")

        self.size = size

    def set_mask(self, img):
        """
        Setting mask with path to B&W image,
        where white pixels pass frame pixels through, 
        and black ones do not.
        :param img: path to mask image
        """
        try:
            image = Image.open(img).convert("L").resize(self.size)
            self.mask = np.array(image)[:, :] // 255
        except:
            print("Image should be have an image extension. Mask not loaded")

    def add_mask(self, frame):
        """ 
        Add mask to a frame
        :param frame: frame to be masked
        """
        return frame if self.mask is None else np.multiply(frame, self.mask)
